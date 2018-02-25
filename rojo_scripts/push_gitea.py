#!/usr/bin/python3
import subprocess
import time
import os
import re
import socket
import getpass


"""
Make and Push Gitea Commit Data
(Rojo)

This script runs the gitea dump command to generate
a dump of the gitea database. It then parses logs of 
all resulting git repositories and assembles the data.

For this script to run, need to be able to execute
the gitea executable. To do that, make sure you're in
the git group and that executable is g+x.

Then you should be able to do all the stuff you need.

Tasks:
- run gitea dump as user gitea
- unzip repos zip file
- run (already written) script to extract commit data
- git add csv to charlesreid1.com repository
- git commit csv
- git push csv
"""


def dbg(msg):
    print(msg)


class PushGitea(object):
    def __init__(self):
        self.tmpdir = ""
        self.reposdir = ""
        self.statusdir = "status"
        self.csvname = "commit_counts.csv"

    def doit(self):
        self.make_gitea_data()
        self.push_gitea_data()

    def make_gitea_data(self):
        """
        Driver:
        Make a temporary directory, generate git commit data in it,
        copy that to the git data repo, and push the latest commit data.
        """
        dbg("- making temp dir")
        self.tmpdir = tempfile.mkdtemp()

        # Generate the csv in tmpdir:

        dbg("- dump contents of gitea and unzip repos")
        self.gitea_dump()

        dbg("- extract commit data from repos")
        self.extract_commit_data()

        dbg("- generating csv in temp dir")
        self.make_git_csv()

        dbg("- committing csv into git data repo")
        self.commit_csv()

        dbg("- clean up zipped data")
        self.cleanup()


    def gitea_dump(self):
        """
        Run gitea dump as user gitea into tmpdir:
    
            cd /tmp/tmp08eeo940
    
            sudo -H -u git /www/gitea/bin/gitea dump
    
        Find the zip file:
    
            ls -1 -t gitea*.zip
    
        Change ownership:
    
            sudo chmod 770 <zip>
    
        Unzip resulting repo zip file:
    
            unzip <zip>
    
        """
        tmpdir = self.tmpdir 
    
        giteabin = "/www/gitea/bin/gitea"
        sudo_prefix = ["sudo","-H","-u","git"]
    
        # Run gitea dump as user gitea
        dbg("    - running gitea dump as user gitea")
        gitea_dump  = [giteabin,"dump"]
        subprocess.call(sudo_prefix + gitea_dump, cwd=tmpdir)
        
        # Find the zip file
        dbg("    - finding the zip file")
        proc = subprocess.Popen(["ls","-1","-t","gitea*.zip"],
                cwd=tmpdir,
                stdout=subprocess.PIPE)
        ls = proc.stdout.read().decode('utf-8').split("\n")
        giteazipfile = ls[0]
        
        # Unzip the resulting file
        dbg("    - unzipping gitea*.zip")
        giteazipdir = "giteazip"
        outputdir = tmpdir+giteazipdir
        mkdir_cmd = ["mkdir",outputdir]
        unzip_cmd = ["unzip","-d",outputdir,giteazipfile]
        subprocess.call(sudo_prefix + mkdir_cmd, cwd=tmpdir)
        subprocess.call(sudo_prefix + unzip_cmd, cwd=tmpdir)
    
        # Unzip the repo zip file
        dbg("    - unzipping gitea-repos.zip")
        repozipdir = "repositories"
        repozip = "gitea-repo.zip"
        unzip_cmd = ["unzip","-d",repozipdir,repozip]
        subprocess.call(sudo_prefix + unzip_cmd, cwd=outputdir)
    
        self.reposdir = outputdir + repozipdir
    
    
    def extract_commit_data(self):
        """
        Extract commit data from each repo 
        in the given gitea dump directory
        """
        tmpdir = self.tempdir
        reposdir = self.reposdir
        status_dir = self.status_dir
    
        filter_flags = "--author=Charles"
    
        subprocess.call(['mkdir','-p',st], cwd=tmpdir)
        status_dir = tmpdir + "/" + st
    
        orgs = glob.glob(reposdir+"/*")
        for org in orgs:
    
            base_org = os.path.basename(org)
            repos = glob(org+"/*")
    
            for repo in repos:
    
                # Print out the org and repo name
                base_repo = re.sub('.git','',os.path.basename(repo))
                log_file = base_org + "." + base_repo + ".log"
                dbg("    - %s : %s"%(base_org,base_repo))
    
                log_file = base_org + "." + base_repo + ".log"
                #pretty_arg = "--pretty=%n%n%h%n%an%n%ae%n%ai%n%s"
                pretty_arg = "--pretty=%H %ai %s"
                full_log_file = status_dir + "/" + log_file
    
                with open(full_log_file,'w') as f:
    
                    cmd = ["git","log",filter_flags,pretty_arg]
    
                    print("    - calling git log command: %s"%(" ".join(cmd)))
                    subprocess.call(cmd, cwd=repo, stdout=f)

    def make_git_csv(self):
        """
        Load the extracted commit data
        in the dump directory into Pandas,
        and compile the CSV.
        """
        tmpdir = self.tempdir
        reposdir = self.reposdir
        statusdir = self.statusdir
        csvname = self.csvname

        orgs = glob.glob(reposdir+"/*")
        for org in orgs:
    
            base_org = os.path.basename(org)
            repos = glob(org+"/*")
    
            for repo in repos:
    
                # Print out the org and repo name
                base_repo = re.sub('.git','',os.path.basename(repo))
                log_file = base_org + "." + base_repo + ".log"
                dbg("    - %s : %s"%(base_org,base_repo))

                # Get each commit
                with open(status_dir + "/" + log_file, 'r', encoding="ISO-8859-1") as f:
                    lines = f.readlines()

                for line in lines:
                    tokens = line.split(" ")
                    commit_id = tokens[0]
                    date = tokens[1]
                    time = tokens[2]
                    msg = tokens[4:]

                    df = df.append( 
                                    dict(   
                                            commit_id = tokens[0],
                                            date = tokens[1],
                                            time = tokens[2],
                                            commits = 1,
                                            msg = " ".join(msg)
                                         ),
                                    ignore_index=True
                                    )

        ag = df.groupby(['date']).agg({'commits':sum})

        ag['commits'] = ag['commits'].apply(int)
        ag.to_csv(statusdir + "/" + csvname)


    def commit_csv(self):
        tmpdir = self.tmpdir
        statusdir = self.statusdir
        csvname = self.csvname
        csvfile = statusdir + "/" + csvname

        # clone the git data repo
        dbg("    - cloning git data repo")
        clonecmd = ["git","clone","https://charlesreid1.com:3000/data/git.git"]
        subprocess.call(clonecmd, cwd=tmpdir)

        # copy the csv file into the git data repo
        dbg("    - copying csv file to git repo")
        gitdir = tmpdir + "/" + git
        cpcmd = ["/bin/cp",csvfile,"."]
        subprocess.call(cpcmd, cwd=gitdir)

        # add commit push
        dbg("    - git add")
        addcmd = ["git","add",csvname]
        subprocss.call(addcmd, cwd=gitdir)

        commitcmd = ["git","commit",csvname,"-m","'[SCRIPT] updating gitea commit counts'"]
        dbg("    - git commit")
        subprocss.call(commitcmd, cwd=gitdir)

        pushcmd = ["git","push","origin","master"]
        dbg("    - git push")
        subprocss.call(pushcmd, cwd=gitdir)

    def cleanup(self):
        cleancmd = ["rm","-rf",self.tmpdir]
        #subprocess.call(cleancmd)
        print("-"*40)
        print("Cleanup command:")
        print("    %s"%(" ".join(cleancmd)))
        print("-"*40)



if __name__=="__main__":

    host = socket.gethostname()
    user = getpass.getuser()

    if(host!="rojo"):
        print("You aren't on rojo - you probably didn't mean to run this script!")
    elif(user!="root"):
        print("You aren't root - you must be root to run gitea dump!")
    else:
        #one_day = 24*3600
        while True:
            make_gitea_data()
            #time.sleep(one_day)
            exit()


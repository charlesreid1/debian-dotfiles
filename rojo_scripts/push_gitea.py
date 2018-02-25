#!/usr/bin/python3
import pandas
import glob
import tempfile
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
        self.statusdirname = "status"
        self.csvname = "commit_counts.csv"

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

        dbg("- cleaning up zipped data")
        self.cleanup()

        dbg("*"*60)
        dbg("\t\t\tALL DONE")
        dbg("*"*60)


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

        # make temp dir writable by git user
        chowncmd = ["sudo","chown","git:git",tmpdir]
        subprocess.call(chowncmd)
    
        giteabin = "/www/gitea/bin/gitea"
        sudo_prefix = ["sudo","-H","-u","git"]

        # Run gitea dump as user gitea
        dbg("    - running gitea dump as user gitea")
        gitea_dump  = [giteabin,"dump","-t",tmpdir]
        subprocess.call(sudo_prefix + gitea_dump, cwd=tmpdir)

        # Find the zip file
        dbg("    - finding the zip file")
        zz = sorted([(os.path.getctime(f), f) for f in glob.glob(tmpdir+"/*.zip")])
        giteazipfile = zz[-1][1]

        # Unzip the resulting file
        dbg("    - unzipping gitea*.zip")
        giteazipdir = "giteazip"
        outputdir = tmpdir+"/"+giteazipdir
        mkdir_cmd = ["mkdir",outputdir]
        unzip_cmd = ["unzip","-qq","-d",outputdir,giteazipfile]
        subprocess.call(sudo_prefix + mkdir_cmd, cwd=tmpdir)
        subprocess.call(sudo_prefix + unzip_cmd, cwd=tmpdir)
    
        # Unzip the repo zip file
        dbg("    - unzipping gitea-repos.zip")
        repozipdir = "repositories"
        repozip = "gitea-repo.zip"
        unzip_cmd = ["unzip","-qq","-d",".",repozip]
        subprocess.call(sudo_prefix + unzip_cmd, cwd=outputdir)
    
        self.reposdir = outputdir + "/" + repozipdir
    
    
    def extract_commit_data(self):
        """
        Extract commit data from each repo 
        in the given gitea dump directory
        """
        tmpdir = self.tmpdir
        reposdir = self.reposdir
        self.statusdir = tmpdir +"/"+ self.statusdirname
        statusdir = self.statusdir
    
        filter_flags = "--author=Charles"
    
        subprocess.call(['mkdir','-p',statusdir], cwd=tmpdir)
        
        orgs = glob.glob(reposdir+"/*")
        for org in orgs:
    
            base_org = os.path.basename(org)
            repos = glob.glob(org+"/*")
    
            for repo in repos:
    
                # Print out the org and repo name
                base_repo = re.sub('.git','',os.path.basename(repo))
                logfile = base_org + "." + base_repo + ".log"
                dbg("    - %s : %s"%(base_org,base_repo))
    
                logfile = base_org + "." + base_repo + ".log"
                #pretty_arg = "--pretty=%n%n%h%n%an%n%ae%n%ai%n%s"
                pretty_arg = "--pretty=%H %ai %s"
                full_logfile = statusdir + "/" + logfile
    
                with open(full_logfile,'w') as f:
    
                    cmd = ["git","log",filter_flags,pretty_arg]
    
                    print("    - calling git log command: %s"%(" ".join(cmd)))
                    subprocess.call(cmd, cwd=repo, stdout=f)

    def make_git_csv(self):
        """
        Load the extracted commit data
        in the dump directory into Pandas,
        and compile the CSV.
        """
        tmpdir = self.tmpdir
        reposdir = self.reposdir
        statusdir = self.statusdir
        csvname = self.csvname

        df = pandas.DataFrame()

        orgs = glob.glob(reposdir+"/*")
        for org in orgs:
    
            base_org = os.path.basename(org)
            repos = glob.glob(org+"/*")
    
            for repo in repos:
    
                # Print out the org and repo name
                base_repo = re.sub('.git','',os.path.basename(repo))
                logfile = base_org + "." + base_repo + ".log"
                dbg("    - %s : %s"%(base_org,base_repo))

                # Get each commit
                with open(statusdir + "/" + logfile, 'r', encoding="ISO-8859-1") as f:
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
        gitdir = tmpdir + "/git"

        # clone the git data repo
        dbg("    - cloning git data repo")
        clonecmd = ["git","clone","git@git.charlesreid1.com:data/git.git",gitdir]
        subprocess.call(clonecmd, cwd=tmpdir)

        # copy the csv file into the git data repo
        dbg("    - copying csv file to git repo")
        cpcmd = ["/bin/cp",csvfile,"."]
        subprocess.call(cpcmd, cwd=gitdir)

        # add commit push
        dbg("    - git add")
        addcmd = ["git","add",csvname]
        subprocess.call(addcmd, cwd=gitdir)

        commitcmd = ["git","commit",csvname,"-m","[SCRIPT] updating gitea commit counts"]
        dbg("    - git commit")
        subprocess.call(commitcmd, cwd=gitdir)

        pushcmd = ["git","push","origin","master"]
        dbg("    - git push")
        subprocess.call(pushcmd, cwd=gitdir)


    def cleanup(self):
        cleancmd = ["rm","-rf",self.tmpdir]
        subprocess.call(cleancmd)



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
            p = PushGitea()
            p.make_gitea_data()
            #time.sleep(one_day)
            exit()


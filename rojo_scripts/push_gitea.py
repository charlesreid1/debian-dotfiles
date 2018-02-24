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


def make_gitea_data():
    dbg("- making temporary directory")
    tmpdir = tempfile.mkdtemp()

    # this will generate the csv in tmpdir
    make_git_csv(tmpdir)

    # this will copy the csv into git data repo and push
    push_git_csv(tmpdir)


def make_git_csv(tmpdir):
    # dump contents of gitea and unzip repos
    gitea_dump(tmpdir)

    extract_commit_data(tmpdir)
    cleanup(tmpdir)
    

def gitea_make_bin():
    """
    Re-make gitea binary
    (mainly here for utility/reference)
    """
    gitea_src_dir = "/home/charles/gocode/src/code.gitea.io/gitea"
    subprocess.call(["eval","\"$(goenv init -)\"","&&","TAGS=\"bindata sqlite\"","make","generate","build"], cwd=gitea_src_dir)
    subprocess.call(["chmod","g+x","gitea"], cwd=gitea_src_dir)
    subprocess.call(["cp","gitea","/www/gitea/bin/."], cwd=gitea_src_dir)


def gitea_dump(tmpdir):
    """
    Run gitea dump as user gitea into tmpdir:

        cd /tmp

        sudo -H -u git /www/gitea/bin/gitea dump

    Find the zip file:

        ls -1 -t gitea*.zip

    Change ownership:

        sudo chmod 770 <zip>

    Unzip resulting repo zip file:

        unzip <zip>

    """
    giteabin = "/www/gitea/bin/gitea"
    sudo_prefix = ["sudo","-H","-u","git"]

    # Run gitea dump as user gitea
    dbg("- running gitea dump as user gitea")
    gitea_dump  = [giteabin,"dump"]
    subprocess.call(sudo_prefix + gitea_dump, cwd=tmpdir)
    
    # Find the zip file
    dbg("- finding the zip file")
    proc = subprocess.Popen(["ls","-1","-t","gitea*.zip"],
            cwd=tmpdir,
            stdout=subprocess.PIPE)
    ls = proc.stdout.read().decode('utf-8').split("\n")
    zipfile = ls[0]
    
    # Unzip the resulting file
    dbg("- unzipping")
    giteazip = "giteazip"
    outputdir = tmpdir+giteazip
    mkdir_cmd = ["mkdir",outputdir]
    unzip_cmd = ["unzip","-d",outputdir,zipfile]
    subprocess.call(sudo_prefix + mkdir_cmd, cwd=tmpdir)
    subprocess.call(sudo_prefix + unzip_cmd, cwd=tmpdir)

    # Unzip the repo zip file
    dbg("- extracting repos")
    repozip = "gitea-repo.zip"
    unzip_cmd = ["unzip",repozip]
    subprocess.call(sudo_prefix + unzip_cmd, cwd=outputdir)


def extract_commit_data(tmpdir):
    """
    Extract commit data from each repo 
    in the given gitea dump directory
    """
    # cd repos
    # for each org
    # for each repo
    # log search for charlesreid1
    # compile final log file
    # assemble final log file into commit csv
    # final commit csv is in tmpdir
    pass


def cleanup(tmpdir):
    """
    Clean up the files
    """
    pass


if __name__=="__main__":

    host = socket.gethostname()
    user = getpass.getuser()

    if(host!="rojo"):
        print("You aren't on rojo - you probably didn't mean to run this script!")
    elif(user!="root"):
        print("You aren't root - you must be root to run gitea dump!")
    else:
        one_day = 24*3600
        while True:
            make_gitea_data()
            time.sleep(one_day)


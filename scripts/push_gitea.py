#!/usr/bin/python3
import subprocess
import time
import os
import re
import socket


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


def make_gitea_data():
    tmpdir = ""
    gitea_dump(tmpdir)
    extract_commit_data(tmpdir)
    cleanup(tmpdir)
    

def gitea_make_bin():
    """
    Re-make gitea binary
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
    tmp = "/tmp"
    giteabin = "/www/gitea/bin/gitea"
    sudo_prefix = ["sudo","-H","-u","git"]

    # Run gitea dump as user gitea
    gitea_dump  = [giteabin,"dump"]
    subprocess.call(sudo_prefix + gitea_dump, cwd=tmp)
    
    # Find the zip file
    proc = subprocess.Popen(["ls","-1","-t","gitea*.zip"],
            cwd=tmp,
            stdout=subprocess.PIPE)
    ls = proc.stdout.read().decode('utf-8').split("\n")
    zipfile = ls[0]
    
    # Unzip the resulting file
    outputdir = tmp+"/zipoutput"
    mkdir_cmd = ["mkdir",output]
    unzip_cmd = ["unzip","-d",outputdir,zipfile]
    subprocess.call(sudo_prefix + mkdir_cmd, cwd=tmp)
    subprocess.call(sudo_prefix + unzip_cmd, cwd=tmp)

    # Unzip the repo zip file
    repozip = "gitea-repo.zip"
    unzip_cmd = ["unzip",repozip]
    subprocess.call(sudo_prefix + unzip_cmd, cwd=outputdir)


def extract_commit_data(tmpdir):
    """
    Extract commit data from each repo 
    in the given gitea dump directory
    """
    pass


def cleanup(tmpdir):
    """
    Clean up the files
    """
    pass


if __name__=="__main__":

    host = socket.gethostname()

    if(host=="rojo"):
        one_day = 24*3600
        while True:
            make_gitea_data()
            time.sleep(one_day)
    else:
        print("You aren't rojo - you probably didn't mean to run this script!")

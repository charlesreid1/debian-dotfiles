#!/usr/bin/python3
import pywikibot
import time
import tempfile
import socket
import subprocess
from datetime import datetime

from os.path import join

from wiki_history import edit_history_database
from wiki_history import edit_history_to_csv

from wiki_graph import graphdb
from wiki_graph import graphdb_to_json


"""
Push Wiki Data
(Jupiter)

This script runs commands to create the database of 
charlesreid1.com wiki edits and assemble the page graph.
The resulting data goes into a MongoDB database on Jupiter,
and is also added to a CSV file.

This script creates the CSV data and checks it into 
version control.
"""


def dbg(msg):
    print(msg)


def push_wiki():
    """
    Push wiki edit data to the charlesreid1.com repo.
    """
    # Make a place to contain the mess
    dbg("- making temporary directory")
    tmpdir = tempfile.mkdtemp()
    dbg("          %s"%(tmpdir))

    # Update the page history database
    dbg("- updating page history database")
    edit_history_database()

    # Extract page history data to CSV
    dbg("- extracting page history data")
    edit_history_to_csv(tmpdir)

    ### # Update the page graph database
    ### dbg("- updating page graph database")
    ### graphdb()

    ### # Extract page graph to JSON
    ### dbg("- extracting page graph json")
    ### graphdb_to_json(tmpdir)

    # Git add/commit/push changes
    dbg("- push changes")
    push_changes(tmpdir)
    

def push_changes(tmpdir):
    """
    Commit changes to data/wiki repo
    """
    # clone the charlesreid1 data repo
    dbg("    - cloning charlesreid1 data repo")
    reponame = "charlesreid1-data"
    repodir = tmpdir + "/" + reponame
    clonecmd =  ["git","clone"]
    clonecmd += ["--recursive"]
    clonecmd += ["git@git.charlesreid1.com:data/%s.git"%(reponame)]
    clonecmd += [repodir]
    subprocess.call(clonecmd, cwd=tmpdir)

    # copy the page_edits.csv file to the repo
    edits_repopath = "page_edits.csv"
    edits_cpcmd = ["/bin/cp","page_edits.csv", join(reponame,edits_repopath)]
    subprocess.call(edits_cpcmd, cwd=tmpdir)

    ### # copy the page_graph.json file to the repo
    ### graph_repopath = "page_graph.json"
    ### graph_cpcmd = ["/bin/cp","page_graph.json", join(reponame,graph_repopath)]
    ### subprocess.call(graph_cpcmd, cwd=tmpdir)

    # add commit push
    dbg("    - git add")
    addcmd = ["git","add","git"]
    subprocess.call(addcmd, cwd=repodir)

    ### commitcmd = ["git","commit",edits_repopath,graph_repopath,"-m","[push_wiki.py] updating charlesreid1 wiki edit data"]
    commitcmd = ["git","commit",edits_repopath,"-m","[push_wiki.py] updating charlesreid1 wiki edit data"]
    dbg("    - git commit")
    subprocess.call(commitcmd, cwd=repodir)

    pushcmd = ["git","push","origin","master"]
    dbg("    - git push")
    subprocess.call(pushcmd, cwd=repodir)

    cleancmd = ["rm","-rf",tmpdir]
    dbg("    - clean up")
    subprocess.call(cleancmd)



if __name__=="__main__":

    host = socket.gethostname()

    if(host!="jupiter"):
        print("You aren't on jupiter - you probably didn't mean to run this script!")
    else:
        push_wiki()


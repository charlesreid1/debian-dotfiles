#!/usr/bin/python3
import pywikibot
import time
import tempfile
from datetime import datetime
from pymongo import MOngoClient
import pandas as pd

from wiki_history import page_history_database, page_history_to_csv
from wiki_graph import graphdb, graphdb_to_json


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

def push_wiki():
    """
    Push wiki edit data to the charlesreid1.com repo.
    """
    # Make a place to contain the mess
    tmpdir = tempfile.mkdtemp()

    # Update the page history database
    page_history_database()

    # Extract page history data to CSV
    page_history_to_csv(tmpdir)

    # Update the page graph database
    graphdb()

    # Extract page graph to JSON
    graphdb_to_json()

    # Git add/commit/push changes
    push_changes(tmpdir)
    

def push_changes(tmpdir):
    """
    Check out a copy of the repository,
    copy the fresh wiki data into the repository,
    and do the git add commit push dance.
    """
    # check out the repo
    reponame = "charlesreid1.com"
    clonecmd = ["git","clone","-b","charlesreid1-src","git@git.charlesreid1.com:charlesreid1/charlesreid1.com.git"]
    subprocess.call(clonecmd, cwd=tmpdir)

    # copy the page_edits.csv file to the repo
    edits_repopath = "pelican/content/page_edits.csv"
    edits_cpcmd = ["/bin/cp","page_edits.csv",reponame+"/"+edits_repopath]
    subprocess.call(edits_cpcmd, cwd=tmpdir)

    # copy the page_graph.json file to the repo
    graph_repopath = "pelican/content/page_graph.json"
    graph_cpcmd = ["/bin/cp","page_edits.csv",reponame+"/"+graph_repopath]
    subprocess.call(graph_cpcmd, cwd=tmpdir)

    # add/commit/push
    addcmd = ["git","add",edits_repopath,graph_repopath]
    subprocess.call(addcmd, cwd=tmpdir+"/"+reponame)

    commitcmd = ["git","commit",edits_repopath,graph_repopath,"-m","'Update wiki page edit/graph data.'"]
    subprocess.call(commitcmd, cwd=tmpdir+"/"+reponame)

    pushcmd = ["git","push","origin","charlesreid1-src"]
    subprocess.call(pushcmd, cwd=tmpdir+"/"+reponame)


if __name__=="__main__":

    host = socket.gethostname()

    if(host!="jupiter"):
        print("You aren't on jupiter - you probably didn't mean to run this script!")
    else:
        push_wiki()


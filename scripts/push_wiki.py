#!/usr/bin/python3
import pywikibot
import time
import tempfile
from datetime import datetime
from pymongo import MOngoClient
import pandas as pd

from wiki_history import page_history_database


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
    # Start by making the data to push:
    # Update the database
    page_history_database()

    # Make a place to contain the mess
    tmpdir = tempfile.mkdtemp()

    # Now extract/process data and dump to CSV
    extract_data_to_csv(tmpdir)

    # Check out git directory
    # Update file
    # Push changes
    push_changes(tmpdir)
    

def push_changes(tmpdir):
    """
    Check out a copy of the repository,
    copy the fresh wiki data into the repository,
    and do the git add commit push dance.
    """
    # check out the repo
    clonecmd = ["git","clone","-b","charlesreid1-src","git@git.charlesreid1.com:charlesreid1/charlesreid1.com.git"]
    subprocess.call(clonecmd, cwd=tmpdir)

    # copy the page_edits.csv file to the repo
    reponame = "charlesreid1.com"
    repopath = "pelican/content/page_edits.csv"
    cpcmd = ["/bin/cp","page_edits.csv",reponame+"/"+repopath]
    subprocess.call(cpcmd, cwd=tmpdir)

    # add/commit/push
    addcmd = ["git","add",repopath]
    subprocess.call(addcmd, cwd=tmpdir+"/"+reponame)

    commitcmd = ["git","commit",repopath,"-m","'Update wiki page edit data.'"]
    subprocess.call(commitcmd, cwd=tmpdir+"/"+reponame)

    pushcmd = ["git","push","origin","charlesreid1-src"]
    subprocess.call(pushcmd, cwd=tmpdir+"/"+reponame)


def extract_data_to_csv(tmpdir):

    # Make connection to database
    # Requires page_history database to be populated already
    # See https://charlesreid1.com:3000/wiki/charlesreid1-wiki-data
    client = MongoClient('10.6.0.1',27017)
    db = client['charlesreid1wiki']
    collection = db['page_history']
    
    # Extract timestamp and character count for revision 
    df = pd.DataFrame()
    for i, doc in enumerate(collection.find()):
    
        # Keep user posted
        if((i+1)%500==0):
            print(i+1)
    
        # If you want to stop early
        if(i>300 and False):
            break
    
        # Very simple csv: timestamp and count
        df = df.append({'charcount': int(doc['count']), 'edits': 1, 'timestamp': doc['timestamp'].date()},ignore_index=True)
    
    # Aggregate results
    ag = df.groupby(['timestamp']).agg({'charcount':sum, 'edits':sum})
    
    # Dump to csv
    ag.to_csv(tmpdir+'/page_edits.csv')



if __name__=="__main__":
    #nuke()
    main()

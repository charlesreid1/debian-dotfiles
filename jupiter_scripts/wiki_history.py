#!/usr/bin/python3
import socket
import pywikibot
import time
from pymongo import MongoClient
from datetime import datetime


"""
Page History

Create a database of charlesreid1.com wiki 
page edits on jupiter's MongoDB.

You should log into the wiki being scraped
with pywikibot.

You should also connect to the VPN so 
Jupiter MongoDB is at 10.6.0.1

Pseudocode:

    get pages generator
    for page in pages:
        get page revisions generator
        for revision in page revisions:
            drop old doc from database
            insert new doc into database
            update record 

Database schema:
    * Page history table
        * Revision sha1 hash (id)
        * Page title
        * Namespace/type/category
        * Page revision timestamp
        * Page revision character count
    * Page history meta table
        * Records hash table
        * Key is page title
        * Value is timestamp when db doc was last updated
"""


def page_history_to_csv(tmpdir):

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




def page_history_database():
    """Run the algorithm that iterates through
    each page and each revision, creating a document
    for each revision.
    """
    N = 0
    sleepytime = 0.1

    # Get connection/database/collections objects
    prefix = 'page_history'
    client, db, page_history_collection = get_collection(prefix)

    # Get the site
    site = get_site()

    # Get the iterator returning pages to process
    page_generator = get_page_generator(site, N)

    # If page has been scraped more than threshold seconds ago, skip it...
    threshold = 0

    # Run the algorithm:
    for page in page_generator:

        page_title = page.title()

        print("Now parsing page: %s"%(page_title))

        rev_generator = page.revisions(content=count_chars)

        for rev in rev_generator:

            # Assemble the document
            doc = {}
            doc['_id'] = rev.sha1
            doc['title'] = page_title
            doc['timestamp'] = rev.timestamp
            doc['count'] = len(rev.text)

            # Remove the old document
            page_history_collection.delete_one({"_id": rev.sha1})

            # Insert the new document
            page_history_collection.insert_one(doc)

        time.sleep(sleepytime)

    # Fin.
    client.close()



"""
Collections, Sites, Pages methods follow.

These functions provide methods to return
various pywikibot objects representing 
db connections, dbs, collections, wiki sites,
and wiki pages.
"""

def get_collection(collections_label):
    """Create a connection to the database,
    and get the collection labeled collections_label,
    AND its corresponding meta collection.
    """
    client = MongoClient('10.6.0.1', 27017)
    db = client['charlesreid1wiki']

    # Collections:
    #   page_history
    #   page_history_meta
    col = db[collections_label]

    return client, db, col


def get_site():
    """Get the Site object representing charlesreid1.com
    """
    return pywikibot.Site()


def get_page_generator(s,max_items=0):
    """Get the generator that returns the Page objects 
    that we're interested in, from Site s.
    """
    page_generator = s.allpages()
    if(max_items>0):
        page_generator.set_maximum_items(max_items)
    return page_generator


def nuke():
    """Nuke everybody"""
    # Get connection/database/collections objects
    client, db, page_history_collection = get_collections()
    page_history_collection.drop()
    client.close()


if __name__=="__main__":
    print("Don't call this script directly: call push_wiki.py instead")


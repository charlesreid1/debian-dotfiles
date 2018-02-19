#!/usr/bin/python3
import pywikibot
import time
from datetime import datetime
from collections_sites_pages import get_collections, get_site, get_page_generator, get_records_table, update_records_table

"""
Make and push Wiki Edit Data 
(Jupiter)

This script runs commands to re-create the 
database of charlesreid1.com wiki edits.
The resulting data goes into a MongoDB 
database on Jupiter. The resulting data
is then parsed and assembled for visualization.


Tasks:
- page generator
- for each edit of each page, create new db entry
- extract data from db
- groupby date, sum on edit
- git add csv to charlesreid1.com repository
- git commit csv
- git push csv
"""

def make_history():
    """Run the algorithm that iterates through
    each page and each revision, creating a document
    for each revision.
    """
    N = 0
    sleepytime = 0.1

    count_chars = True

    # Get connection/database/collections objects
    prefix = 'page_history'
    client, db, page_history_collection, meta_collection = get_collections(prefix)

    # Get records of prior scrapes
    records = get_records_table(meta_collection)

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

        # Should we update this page?
        update = False
        if(page in records.keys()):
            old_time = records[page_title]
            new_time = datetime.now()
            if( (new_time-old_time) > threshold ):
                update = True
        else:
            update = True

        if update:
            rev_generator = page.revisions(content=count_chars)

            for rev in rev_generator:

                # Assemble the document
                doc = {}
                doc['_id'] = rev.sha1
                doc['title'] = page_title
                doc['timestamp'] = rev.timestamp

                if(count_chars):
                    doc['count'] = len(rev.text)

                # Remove the old document
                page_history_collection.delete_one({"_id": rev.sha1})

                # Eventually, change content=True
                # and add the character count

                # Insert the new document
                page_history_collection.insert_one(doc)

            # Update records
            update_records_table(meta_collection, page_title, datetime.now())

            time.sleep(sleepytime)

    # Fin.
    client.close()

def nuke():
    # Get connection/database/collections objects
    client, db, page_history_collection, meta_collection = get_collections()

    page_history_collection.drop()
    meta_collection.drop()

    client.close()

if __name__=="__main__":
    #nuke()
    main()

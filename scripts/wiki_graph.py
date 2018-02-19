#!/usr/bin/python3
import socket
import pywikibot
import time
from pymongo import MongoClient
from datetime import datetime
import pandas as pd
import json

from mongo_graph import MongoGraph
from wiki_history import get_collection, get_site, get_page_generator


"""
Page Graph

Create a graph database with link data for charlesreid1.com wiki.

You should log into the wiki being scraped with pywikibot.

You should also connect to the VPN so Jupiter MongoDB is at 10.6.0.1
"""


def json_export(tmpdir):
    g = main_import()
    
    vertices = []
    edges    = []

    for vertex in g.vertices():
        item = {'id': vertex.element()}
        vertices.append(item)

    for edge in g.edges():
        item = {}
        (u,v) = edge.endpoints()
        item['source'] = u.element()
        item['target'] = v.element()
        edges.append(item)

    result = {}
    result['nodes'] = vertices
    result['links'] = edges

    with open(tmpdir+'/wiki_graph.json','w') as f:
        json.dump(result, f, indent=4)



def mongo_export(tmpdir):
    """This runs pywikibot to step through each page
    and construct nodes and edges for the wiki link 
    graph. Once the graph is completely constructed, 
    all edges are added to the MongoDB database.

    Returns nothing - the graph is in the database.
    """
    N = 0

    # Get connection/database/collections objects
    prefix = 'page_graph'
    client, db, collection = get_collection(prefix)

    # Get the site
    site = get_site()

    # Get the iterator returning pages to process
    page_generator = get_page_generator(site, N)

    # Graph:
    g = MongoGraph(directed=True)

    # Run the algorithm:
    for page in page_generator:

        page_title = page.title()

        try:
            u = g.insert_vertex(page_title)
        except KeyError:
            print("XXXXXXXXXXXXX Insertion failed for page %s XXXXXXXXXXXX"%(page_title))
            pass

        print("Now parsing page: %s"%(page_title))

        for page2 in page.linkedPages():
            
            try:
                page2_title = page2.title()
                v = g.insert_vertex(page2_title)
                e = g.insert_edge(u,v)
            except KeyError:
                print("XXXXXXXXXXXXX Insertion failed for page %s XXXXXXXXXXXX"%(page_title))
                pass

    # Export the graph to MongoDB
    g.export_graph(collection)


if __name__=="__main__":

    host = socket.gethostname()

    if(host!="jupiter"):
        print("You aren't on jupiter - you probably didn't mean to run this script!")
    else:
        t = '/tmp/ioeuirweoriuw'
        subprocess.call(["mkdir","-p",t])
        mongo_export(t)
        json_export(t)


#!/usr/bin/python3
import socket
import pywikibot
import time
from pymongo import MongoClient
from datetime import datetime


"""
Page Graph

Create a graph database with link data for charlesreid1.com wiki.

You should log into the wiki being scraped with pywikibot.

You should also connect to the VPN so Jupiter MongoDB is at 10.6.0.1
"""


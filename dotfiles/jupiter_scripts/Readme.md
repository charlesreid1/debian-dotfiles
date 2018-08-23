# Jupiter Scripts

The main task run on Jupiter is scraping the wiki.

Main driver:

* `push_wiki.py` - This is the main entrypoint. This script will
  first scrape pages for links and edits and populate 
  that information in MongoDB. It will then compile a CSV file
  for data visualization and commit that to the data repo at
  <https://git.charlesreid1.com/data/charlesreid1-data>

Main functions:

* `wiki_history.py` - Create a database containing page history
  data for the charlesreid1.com wiki

* `wiki_graph.py` - Create a graph database with link data
  for the charlesreid1.com wiki

MediaWiki:

* `user-config.py` - configuration for pywikibot

* (notes on [family file](https://www.mediawiki.org/wiki/Manual:Pywikibot/Use_on_third-party_wikis))

Graphs:

* `graph.py` - Graph object, useful for dealing with page graphs.

* `mongo_graph.py` - extended Graph object that has additional
  methods for serializing the graph into something that can be
  stored in a MongoDB database table.

* `graph_algorithms.py` - Graph algorithms useful for analyzing the
  wiki page graph.


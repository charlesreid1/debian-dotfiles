#!/usr/bin/python3

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


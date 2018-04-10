import os

"""
Directory structure:

NOTE: in case there is a week 5,
    don't hard code 4; check the month.

NOTE: largest number indicates most recent.

NOTE: both weekly and monthly backup dates fall on sundays.

junkinthetrunk/

    backups/

        daily/
            daily.7.tar.gz  --> daily.2018-01-31.tar.gz
            daily.6.tar.gz  --> daily.2018-01-30.tar.gz
            daily.5.tar.gz  --> daily.2018-01-29.tar.gz
            daily.4.tar.gz  --> daily.2018-01-28.tar.gz
            daily.3.tar.gz  --> daily.2018-01-27.tar.gz
            daily.2.tar.gz  --> daily.2018-01-26.tar.gz
            daily.1.tar.gz  --> daily.2018-01-25.tar.gz

        weekly/
            weekly.4.tar.gz --> weekly.2018-01-28.tar.gz
            weekly.3.tar.gz --> weekly.2018-01-21.tar.gz
            weekly.2.tar.gz --> weekly.2018-01-14.tar.gz
            weekly.1.tar.gz --> weekly.2018-01-07.tar.gz

          monthly/
              monthly.6.tar.gz --> monthly.2018-01-07.tar.gz
              monthly.5.tar.gz --> monthly.2017-12-03.tar.gz
              monthly.4.tar.gz --> monthly.2017-11-05.tar.gz
              monthly.3.tar.gz --> monthly.2017-10-01.tar.gz
              monthly.2.tar.gz --> monthly.2017-09-03.tar.gz
              monthly.1.tar.gz --> monthly.2017-08-06.tar.gz
"""

ROOTDIR   = "/junkinthetrunk/backups"
DAILYDIR  = os.path.join(ROOTDIR,"daily")
WEEKLYDIR = os.path.join(ROOTDIR,"weekly")


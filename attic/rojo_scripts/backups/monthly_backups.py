"""
Monthly Backups

Description:

This script is run weekly on Sunday at 2 AM and generates weekly backups.

On Rojo we keep weekly backups going back 1 month,
we keep monthly backups going back 6 months,
and we put older backups into cold storage.


Directory Stucture:

    junkinthetrunk/
    
        backups/

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



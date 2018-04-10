"""
Daily Backups


Description:

This script is run daily at 2 AM and generates daily backups. 
On Rojo we keep daily backups going back 7 days.
Script logic is to generate the lastest backup,
remove the oldest backup file, shift everybody back,
and move the latest backup into the latest slot.


Directory Structure:

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

"""


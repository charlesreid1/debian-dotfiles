# rojo backups

Backup schedule is as follows:
* Daily backups, storing last 7 days
* Weekly backups, storing last 6 months and archiving older stuff to Glacier

most of the backups dump to `/junkinthetrunk`.

## daily backups

Daily backups are scheduled to occur daily at 2 AM.

Daily backups are rotating, with up to 7 days stored.

If it is Sunday, get things ready for the weekly backup.

Older than 7 days, it gets deleted.

## weekly backups

Weekly backups occur on weekly on Sunday.

Weekly backups are rotating, with up to 6 months stored.

Last 1 month is stored weekly.

Last 6 months (minus 1) is stored monthly.

Older than 6 months, it gets archived to Amazon Glacier.

## rando shotgun scripts

back up bash history:

```
./backup_bashhist.py
```

back up site (config files and wiki files):

```
./backup_charlesreid1.py
```

back up database (wiki only, and everything):

```
./backup_wiki.py
./backup_mysql.py
```

(Need a backup gitea script)


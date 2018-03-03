# rojo scripts

## updating site

update git commit data and push to git data repo:

```
./push_gitea.py
```

pull latest changes to charlesreid1, make htdocs, and deploy:

```
./pull_charlesreid1.py
```

pull latest data to charlesreid1.com/data:

```
./pull_charlesreid1_data.py
```

## running stuff

run bots in screen:

```
./screen_run_bots.sh
```

run gitea server in screen:

```
./screen_run_gitea.sh
```

## crontabs

The rojo crontab is intended to be installed for the regular non-root user (charles).
It will install the latest charlesreid1.com theme and update charlesreid1.com weekly,
and it will update charlesreid1.com/data repos daily.

The sudo crontab will dump the gitea repositories to generate a new commit count
for the git.charlesreid1.com commit calendar.

## backups

most of the backups dump to `/junkinthetrunk`.

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

## databases

To change the root password for MySQL:

```
mysql < change_mysql_root.sql
```

## firewall

open a port:

(edit file first)

```
./fw_open_port.sh
```

close a fw port:

(edit file first)

```
./fw_close_port.sh
```


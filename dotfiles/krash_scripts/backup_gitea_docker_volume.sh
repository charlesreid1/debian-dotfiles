#!/bin/sh
# 
# this container contains a handy volume-backup script:
# https://github.com/loomchild/volume-backup
#
# usage:
# docker run --rm -v some_volume:/volume -v /tmp:/backup loomchild/volume-backup backup some_archive
# docker run --rm -v some_volume:/volume -v /tmp:/backup loomchild/volume-backup restore some_archive
set -x
set -e


###########
# Note:
# unfortunately the path you specify
# is always relative to /tmp, so
# even when you specify an absolute path
# it just ends up in /tmp.
#
# :massive_eye_roll: 
#################

GITEAVOL="podcharlesreid1_stormy_gitea_data"
TS=$(date +"%Y-%m-%d")
BACKUPDIR=/junkinthetrunk/backups/monthly/gitea_dockervolume_${TS}

mkdir -p ${BACKUPDIR}

# backup:
docker run --rm -v ${GITEAVOL}:/volume -v /tmp:/backup loomchild/volume-backup backup ${BACKUPDIR}/gitea_snapshot

set +x
echo "Gitea volume ${GITEAVOL} backed up to file /tmp/${BACKUPDIR}/"

# restore:
#docker run --rm -v ${GITEAVOL}:/volume -v /tmp:/backup loomchild/volume-backup restore ${BACKUPDIR}/gitea_snapshot

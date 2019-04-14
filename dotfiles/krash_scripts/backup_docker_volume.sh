#!/bin/sh
# 
# this container contains a handy volume-backup script:
# https://github.com/loomchild/volume-backup
#
# usage:
# docker run --rm -v some_volume:/volume -v /tmp:/backup loomchild/volume-backup backup some_archive
# docker run --rm -v some_volume:/volume -v /tmp:/backup loomchild/volume-backup restore some_archive

GITEAVOL="podcharlesreid1_stormy_gitea_data"
TS=$(date +"%Y-%m-%d")
BACKUPDIR=/junkinthetrunk/monthly/gitea_dockervolume_${TS}

mkdir -p ${BACKUPDIR}

# backup:
docker run --rm -v ${GITEAVOL}:/volume -v /tmp:/backup loomchild/volume-backup backup ${BACKUPDIR}/gitea_snapshot

# restore:
#docker run --rm -v ${GITEAVOL}:/volume -v /tmp:/backup loomchild/volume-backup restore ${BACKUPDIR}/gitea_snapshot

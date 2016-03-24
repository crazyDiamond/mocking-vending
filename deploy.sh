#!/bin/bash

shopt -s extglob
# Totally not the right host, fix that before deploy
DEST_HOST=172.24.25.82

GROUPNAME=${1:-`echo $USER`}
TARFILE=${GROUPNAME}.tgz
TARPATH=/tmp/${TARFILE}
tar czf ${TARPATH} --exclude-from exclusions.txt . || exit 1
echo "If prompted for a password enter \"raspberry\""
ssh -i pi.key pi@${DEST_HOST} "mkdir ${GROUPNAME} 2>/dev/null"
scp -i pi.key ${TARPATH} pi@${DEST_HOST}:~/${GROUPNAME} && echo "Transferred ${TARFILE} to remote folder ${GROUPNAME}"
rm ${TARPATH}

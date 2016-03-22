#!/bin/bash

# Totally not the right host, fix that before deploy
DEST_HOST=172.24.25.82

GROUPNAME=${1:-`echo $USER`}
TARFILE=${GROUPNAME}.tgz
TARPATH=/tmp/${TARFILE}
tar czf ${TARPATH} --exclude '*deploy.sh' . || exit 1
echo "If prompted for a password enter \"raspberry\""
scp ${TARPATH} pi@${DEST_HOST}:~/ && echo "Transferred ${TARFILE}"


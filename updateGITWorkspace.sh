#!/bin/bash
############################################################################
## This script is used for updating all the GIT Repo under the executing directory path
## For Example: myfolder +-----> updateGITWorkspace.sh
##                       |-----> Git_Repo_2
##                       +-----> Git_Repo_1
##
## In this case, if executed from my folder path, it will update both of the 
##   GIT repositories: Git_Repo_2 and Git_Repo_1. Its just finding Git repos 
##   under executing directory path and then git pull.
############################################################################


file=".git"

DIRS=`ls -l | egrep '^d' | awk '{print $NF}'`
for DIR in $DIRS
do
if [ -e ${DIR}/$file ]
then
    echo ""
    echo "Updating local git repo from remote, for folders:"
    echo "#############"
    echo "## " ${DIR}
    echo "#############"

    cd ${DIR}
    git pull
    cd ..

    echo "#############"
    echo ""
fi;

done

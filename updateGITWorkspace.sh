#!/bin/bash

############################################################################
## This script is used for updating all the GIT Repo under the executing directory path
## For Example: myfolder +-----> updateGITWorkspace.sh
##                       |-----> Git_Repo_1
##                       +-----> Git_Repo_2
##                       +-----> DIR1/Git_Repo_3
##                       +-----> DIR2/DIR3/Git_Repo_4
##                       +-----> DIR2/DIR3/Git_Repo_5
##
##
## In this case, if executed from my folder path, it will update both of the 
##   GIT repositories: Git_Repo_2 and Git_Repo_1. Its just finding Git repos 
##   under executing directory path and then git pull.
############################################################################

ORG_DIR=`pwd`
DIRS=`find . -type d -name .git | awk -F".git" '{print $1}'`
for DIR in $DIRS
do

    echo ""
    echo "## Updating local git repo from remote, for folders:"
    echo "##-----------"
    echo "## " ${DIR}
    echo "##-----------"

    cd ${DIR}
    git pull
    cd ${ORG_DIR}

    echo "##-----------"
    echo ""

done

#!/bin/bash

# Exit immediately if any command exits with a nonzero exit value
set -e

# Fast-downward planner with the desired version
PLANNER_NAME=fast-downward-24.06.1

TARBALL="${PLANNER_NAME}.tar.gz"
TARBALL_URL="https://www.fast-downward.org/latest/files/release24.06/${TARBALL}"

# Install paths
INSTALL_DIR_ROOT="bin"
INSTALL_DIR_NAME="fast-downward"
INSTALL_DIR=$INSTALL_DIR_ROOT/$INSTALL_DIR_NAME

# Pre-install cleanup
if [ -d $INSTALL_DIR ]; then
  echo "Removing existing planner from ${INSTALL_DIR} ..."
  rm -rf $INSTALL_DIR
fi

# Fresh Installation
echo "Installing LAMA planner"
cd $INSTALL_DIR_ROOT
wget $TARBALL_URL -O $TARBALL
tar -xzvf $TARBALL
mv $PLANNER_NAME $INSTALL_DIR_NAME
rm -f $TARBALL
python3 $INSTALL_DIR_NAME/build.py

#!/bin/bash

RECIPE_PATH=$1

REPO=$(basename $(dirname $RECIPE_PATH))
RECIPE_FILENAME=$(basename $RECIPE_PATH)
SHORTNAME=${RECIPE_FILENAME#Apptainer.}
VAGRANT_PATH=$(cd $(dirname $0); pwd)

# Vagrant mounts a specific directory containing all submissions. We can only build images from there.
SUBMISSIONS_DIR=$(cd "$VAGRANT_PATH/../../submissions"; pwd)
if [[ $(realpath --relative-base="$SUBMISSIONS_DIR" -- "$RECIPE_PATH")  =~ ^/ ]]; then
    echo "The recipe file is not in the directory '$SUBMISSIONS_DIR' that is mounted in the vagrant VM."
    exit 1
fi

cd $VAGRANT_PATH
vagrant up

# We cannot build the container in /images directly, because
# Apptainer uses mmap on the container and this is not
# supported accros synchronized folders by vagrant.
vagrant ssh -c "(\
    cd /submissions/$REPO; \
    apptainer --version; \
    apptainer build "/tmp/$SHORTNAME.img" "$RECIPE_FILENAME"; \
    mv "/tmp/$SHORTNAME.img" /images \
    ) > >(tee /images/$SHORTNAME.log) 2> >(tee /images/$SHORTNAME.err >&2)"


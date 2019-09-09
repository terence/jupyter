#!/bin/bash
source ./_vars.sh
# ================================================================
# Command-line Assistant - run.sh
# ================================================================


echo =============================================================
echo run.sh -a [action] -b [label] -c [container]
echo -------------------------------------------------------------
echo -a install : Jupyter Install
echo -a notebook : Jupyter notebook
echo =============================================================

#Defaults
#ACTION="up"
LABEL="latest"
CONTAINER=mybasec
IMAGE=mybase
TARGET=prod
SCRIPT=dev.yml

while getopts "a:b:c:t:s:" opt; do
  case "${opt}" in 
    "a" )
      ACTION="${OPTARG}"
      echo "Action:" $ACTION
      ;;
    "b" )
      LABEL="${OPTARG}"
      echo "Label:" $LABEL
      ;;

    "c" )
      CONTAINER="${OPTARG}"
      echo "Container:" $CONTAINER
      ;;

    "t" )
      TARGET="${OPTARG}"
      echo "Target:" $TARGET
      ;;
    "s" )
      SCRIPT="${OPTARG}"
      echo "Script:" $SCRIPT
      ;;
  esac
done


case "$ACTION" in
  "install" )
    echo ===========================================================
    echo Install Jupyter
    echo ===========================================================
    pip3 install jupyter
    ;;

  "notebook" )
    echo ===========================================================
    echo Run Jupyter notebook
    echo ===========================================================
    jupyter notebook
    ;;

  * )
    # Default option.
    # Empty input (hitting RETURN) fits here, too.
    echo
    echo "Please use a recognized option."
    ;;
esac






#!/bin/sh

if [ $# != 1 ]; then
  echo "Usage: "
  echo "  $0 [options] <new project name>"
  echo "e.g.:"
  echo " $0 mycorpus"
  exit 1;
fi

# read the new project name
BASE_DIR=~/kaldi/egs
PROJECT_DIR=${BASE_DIR}/$1

# create a new directory for the new project
[ ! -d ${PROJECT_DIR} ] && echo "project $PROJECT_DIR does not exist.." && \
	echo "creating new project folder..." && mkdir -p ${PROJECT_DIR}

# create necessary folders
WAV_DIR=${PROJECT_DIR}/wav
EXP_DIR=${PROJECT_DIR}/exp
CONF_DIR=${PROJECT_DIR}/conf
DATA_DIR=${PROJECT_DIR}/data
TRAIN_DIR=${DATA_DIR}/train
WAV_SCP_FILE=${TRAIN_DIR}/wav.scp
LANG_DIR=${TRAIN_DIR}/lang
LOCAL_DIR=${TRAIN_DIR}/local
LCL_LANG_DIR=${LOCAL_DIR}/lang
UTT_SPK_FILE=${TRAIN_DIR}/utt2spk

[ ! -d "$WAV_DIR" ] && echo "Directory /WAV_DIR/ DOES NOT exists."
[ ! -d "$WAV_DIR" ] && echo "Creating wav dir" && mkdir -p "$WAV_DIR"

[ ! -d "$DATA_DIR" ] && echo "Directory /DATA_DIR/ DOES NOT exists."
[ ! -d "$DATA_DIR" ] && echo "Creating data dir" && mkdir -p "$DATA_DIR"

[ ! -d "$EXP_DIR" ] && echo "Directory /EXP_DIR/ DOES NOT exists."
[ ! -d "$EXP_DIR" ] && echo "Creating exp dir" && mkdir -p "$EXP_DIR"

[ ! -d "$CONF_DIR" ] && echo "Directory /CONF_DIR/ DOES NOT exists."
[ ! -d "$CONF_DIR" ] && echo "Creating conf dir" && mkdir -p "$CONF_DIR"

[ ! -d "$TRAIN_DIR" ] && echo "Directory /TRAIN_DIR/ DOES NOT exists."
[ ! -d "$TRAIN_DIR" ] && echo "Creating train dir" && mkdir -p "$TRAIN_DIR"

[ ! -d "$LANG_DIR" ] && echo "Directory /LANG_DIR/ DOES NOT exists."
[ ! -d "$LANG_DIR" ] && echo "Creating lang dir" && mkdir -p "$LANG_DIR"

[ ! -d "$LOCAL_DIR" ] && echo "Directory /LOCAL_DIR/ DOES NOT exists."
[ ! -d "$LOCAL_DIR" ] && echo "Creating local dir" && mkdir -p "$LOCAL_DIR"

[ ! -d "$LCL_LANG_DIR" ] && echo "Directory /LOCAL_DIR/ DOES NOT exists."
[ ! -d "$LCL_LANG_DIR" ] && echo "Creating local dir" && mkdir -p "$LCL_LANG_DIR"

# copy prepare project script
cp ./prepare_project.sh ${PROJECT_DIR}/.
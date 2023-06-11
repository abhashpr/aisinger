#!/bin/sh

WAV_DIR=wav
TRAIN_DIR=data/train
WAV_SCP_FILE=data/train/wav.scp
LANG_DIR=data/train/lang
LOCAL_DIR=data/train/local
LCL_LANG_DIR=${LOCAL_DIR}/lang
UTT_SPK_FILE=data/train/utt2spk
CONF_DIR=conf

echo "---------------------------------------------"
echo "Wave file directory => ${WAV_DIR}"
echo "Wave scp file => ${WAV_SCP_FILE}"
echo "Lang directory => ${LANG_DIR}"
echo "Local file directory => ${LOCAL_DIR}"
echo "Local lang directory => ${LCL_LANG_DIR}"
echo "utt2spk file => ${UTT_SPK_FILE}"


# create softlinks from existing directories
echo "---------------------------------------------"
echo "creating softlinks from existing directories..."
ln -s ../wsj/s5/steps .
ln -s ../wsj/s5/utils .
ln -s ../../src .    
cp ../wsj/s5/path.sh .


# copy dict directory from egs/hindi
echo "---------------------------------------------"
echo "copying dict directory from egs/hindi..."
[ ! -d "$DATA_DIR"/local/dict ] && cp -r ../hindi/data/local/dict/ ./data/local/dict


# copy scripts
echo "---------------------------------------------"
echo "copying scripts files..."
cp ../hindi/*sh .
cp ../scripts/* scripts/


# create utt2spk file from wav directory
echo "---------------------------------------------"
echo "create utt2spk file from wav directory..."
for e in `find -L $WAV_DIR/*`; do [ ! -d $e ] && echo $(basename $e .wav) " " $(basename $e | awk -F '_' '{print $1}'); done > $UTT_SPK_FILE


# create wav.scp file from wav directory
echo "---------------------------------------------"
echo "create wav.scp file from wav directory..."
# for FILENAME in $WAVDIR/*; do echo $(basename $FILENAME .wav) " " $FILENAME; done > $WAV_SCP_FILE
for e in `find -L $WAVDIR`; do [ ! -d $e ] && echo -e $(basename $e .wav)"\t"`pwd`$e; done > $WAV_SCP_FILE


# create corpus.txt in ./data/local from text file
echo "---------------------------------------------"
echo "create corpus.txt in ./data/local from text file..."
cat ${TRAIN_DIR}/text | awk -F "\t" '{print $2}' > ${DATA_DIR}/local/corpus.txt


# run utils/fix_data_dir.sh
echo "---------------------------------------------"
echo "run utils/fix_data_dir.sh..."
utils/fix_data_dir.sh data/train


# create mfcc.conf
echo "---------------------------------------------"
echo "create mfcc.conf..."                 
echo "--use-energy=false" > ${CONF_DIR}/mfcc.conf
echo "--sample-frequency=16000" >> ${CONF_DIR}/mfcc.conf


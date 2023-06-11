
#dirs=( mono mono_ali tri1 )
#for d in "${dirs[@]}";
#do \
# for i in  exp/${d}/ali.*.gz;
#   do ${KALDI_ROOT}src/bin/ali-to-phones --ctm-output exp/${d}/final.mdl ark:"gunzip -c $i|" -> ${i%.gz}.ctm;
#   echo ${i%.gz}.ctm
#   done;
#done;

KALDI_ROOT=`pwd`/../../
WORK_DIR=`pwd`
OUT_DIR=`pwd`/output

mkdir -p ${OUT_DIR}

for i in exp/tri1/ali.*.gz;
    do 
        ${KALDI_ROOT}src/bin/ali-to-phones --ctm-output exp/tri1/final.mdl ark:"gunzip -c $i|" -> ${i%.gz}.ctm;
    done;

cat exp/tri1/*.ctm > ${OUT_DIR}/merged_alignment.txt

# create segment file
python3 scripts/create_segments.py

# create final alignments
echo "Running id2phone.py script ...."
python3 scripts/id2phone.py

# id2phone.py returns a modified version of merged_alignment.txt called final_ali.txt
# Split final_ali.txt by file
python3 scripts/splitAlignments.py

echo "Running phons2pron.py"
python3 scripts/phons2pron.py

echo "Running pron2words.py"
python3 scripts/pron2words.py











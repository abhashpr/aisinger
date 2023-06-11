import sys
import re
import glob
import os

WORK_DIR = os.getcwd()
OUTPUT_DIR = WORK_DIR + "/output"
TARGET_DIR = OUTPUT_DIR + "/utterances"

pron_ali = open(os.path.join(OUTPUT_DIR, "pron_alignment.txt"),'w')
pron = []

files = glob.glob(TARGET_DIR + '/*.txt')

count = 0
# process each file
for filei in files:
    # print(filei)
    f = open(filei, 'r')
    header = True
    if count > 0:
       pron_ali.write('\n')
    for line in f:
        if header:
            header = False
            continue
        line = line.split("\t")
        # print(f"line: {line}")
        file = line[1]
        file = file.strip()
        phon_pos = line[6]
        if phon_pos == "sil":
            phon_pos = "sil_S"
        phon_pos = phon_pos.split("_")
        phon = phon_pos[0]
        pos = phon_pos[1]
        if pos == "B":
            start = line[9]
            pron.append(phon)
        if pos == "S":
            start = line[9]
            end = line[10]
            pron.append(phon)
            pron_ali.write(file + '\t' + ' '.join(pron) +'\t'+ str(start) + '\t' + str(end))
            pron = []
        if pos == "E":
            end = line[10]
            pron.append(phon)
            pron_ali.write(file + '\t' + ' '.join(pron) +'\t'+ str(start) + '\t' + str(end))
            pron = []
        if pos == "I":
            pron.append(phon)
        count += 1

#  phons2words.py
#
#
#  Created by Eleanor Chodroff on 2/07/16.

# https://www.eleanorchodroff.com/tutorial/kaldi/scripts/phons2pron.py

# import sys,re,glob

# pron_ali=open("pron_alignment.txt",'w')
# pron=[]

# files = glob.glob('[1-9]*.txt')

# # process each file
# for filei in files:
#     print filei
#     f = open(filei, 'r')
#     header = True
#     pron_ali.write('\n')
#     for line in f:
#     	if header:
#     		header = False
#     		continue
#         line=line.split("\t")
#         file=line[1]
#         file = file.strip()
#         phon_pos=line[6]
#         #print phon_pos
#         if phon_pos == "SIL":
#             phon_pos = "SIL_S"
#         phon_pos=phon_pos.split("_")
#         phon=phon_pos[0]
#         pos=phon_pos[1]
#         #print pos
#         if pos == "B":
#             start=line[9]
#             pron.append(phon)
#         if pos == "S":
#             start=line[9]
#             end=line[10]
#             pron.append(phon)
#             pron_ali.write(file + '\t' + ' '.join(pron) +'\t'+ str(start) + '\t' + str(end))
#             pron=[]
#         if pos == "E":
#             end=line[10]
#             pron.append(phon)
#             pron_ali.write(file + '\t' + ' '.join(pron) +'\t'+ str(start) + '\t' + str(end))
#             pron=[]
#         if pos == "I":
#             pron.append(phon)
import sys
import csv
import os
import re
import codecs

WORK_DIR = os.getcwd()
OUTPUT_DIR = WORK_DIR + "/output"
LOCAL_DIR = WORK_DIR + "/data/local/dict"

LEXICON_TEXT_FILE = os.path.join(LOCAL_DIR, "lexicon.txt")
PRON_ALIGNMENT_FILE = os.path.join(OUTPUT_DIR, "pron_alignment.txt")
WORD_ALIGNMENT_FILE = os.path.join(OUTPUT_DIR, "word_alignment.txt")

# make dictionary of word: prons
lex = {}

with codecs.open(LEXICON_TEXT_FILE, "rb", "utf-8") as f:
    for line in f:
        line = line.strip()
        columns = line.split("\t")
        # print(columns)
        word = columns[0]
        pron = columns[1]
        #print pron
        try:
            lex[pron].append(word)
        except:
            lex[pron] = list()
            lex[pron].append(word)

# open file to write

word_ali = codecs.open(WORD_ALIGNMENT_FILE, "wb", "utf-8")

# read file with most information in it
with codecs.open(PRON_ALIGNMENT_FILE, "rb", "utf-8") as f:
    for line in f:
        line = line.strip()
        line = line.split("\t")
        # get the pronunciation
        pron = line[1]
        # look up the word from the pronunciation in the dictionary
        word = lex.get(pron)
        if word is None:
           print(pron)
        word = word[0]
        file = line[0]
        start = line[2]
        end = line[3]
        word_ali.write(file + '\t' + word + '\t' + start + '\t' + end + '\n')
import os
import csv

WORK_DIR = os.getcwd()
OUTPUT_DIR = WORK_DIR + "/output"
TARGET_DIR = OUTPUT_DIR + "/utterances"

results = []
labels = []
final_aligned = os.path.join(OUTPUT_DIR, "final_ali.txt")

if not os.path.exists(TARGET_DIR):
    print(f"{TARGET_DIR} does not exist. Creating {TARGET_DIR}..")
    os.mkdir(TARGET_DIR)

name_prev = None
name = None
i = 0

try:
    with open(final_aligned) as f:
        print(f"Final alignment file: {final_aligned} exists and contents will be read fron this file..")    
        for line in f:
            if i == 0:
                header = line.strip("\n").split("\t")
                i += 1
                continue
            columns = line.strip("\n").split("\t")
            if name is not None:
                name_prev = name
                name = columns[0]
                if (name_prev != name):
                    # print(name, name_prev)
                    # print(results)
                    try:
                        with open(os.path.join(TARGET_DIR, name_prev+".lab"),'w') as fwrite:
                            writer = csv.writer(fwrite)
                            fwrite.write("\n".join(labels))
                            fwrite.close()
                        
                        with open(os.path.join(TARGET_DIR, name_prev+".txt"),'w') as fwrite:
                            writer = csv.writer(fwrite)
                            fwrite.write("\n".join(results))
                            fwrite.close()
                    except FileNotFoundError:
                        print("Failed to write file")
                        sys.exit(2)
                    del results[:]
                    del labels[:]
                    results.append("\t".join(header[0:]))
                    labels.append("\t".join(header[-3:]))
                    # results.append(line[0:-1])
                    labels.append("\t".join(columns[-3:]))
                    results.append("\t".join(columns[0:]))
                else:
                    # results.append(line[0:-1])
                    labels.append("\t".join(columns[-3:]))
                    results.append("\t".join(columns[0:]))
            else:
                name = columns[0]
                # results.append(line[0:-1])
                results.append("\t".join(header[0:]))
                labels.append("\t".join(header[-3:]))
                
                results.append("\t".join(columns[0:]))
                labels.append("\t".join(columns[-3:]))
except FileNotFoundError:
    print("Failed to read file")
    sys.exit(1)

try:
    with open(os.path.join(TARGET_DIR, name_prev+".txt"),'w') as fwrite:
        writer = csv.writer(fwrite)
        fwrite.write("\n".join(results))
        fwrite.close()
    
    with open(os.path.join(TARGET_DIR, name_prev+".lab"),'w') as fwrite:
        writer = csv.writer(fwrite)
        fwrite.write("\n".join(labels))
        fwrite.close()

except FileNotFoundError:
    print("Failed to write file")
    sys.exit(2)


#!/bin/sh

# https://www.eleanorchodroff.com/tutorial/kaldi/scripts/splitAlignments.py

#  splitAlignments.py
#  
#
#  Created by Eleanor Chodroff on 3/25/15.
#
#
#
# import sys,csv
# results=[]

#name = name of first text file in final_ali.txt
#name_fin = name of final text file in final_ali.txt

# name = "110236_20091006_82330_F"
# name_fin = "120958_20100126_97016_M"
# try:
#     with open("final_ali.txt") as f:
#         next(f) #skip header
#         for line in f:
#             columns=line.split("\t")
#             name_prev = name
#             name = columns[1]
#             if (name_prev != name):
#                 try:
#                     with open((name_prev)+".txt",'w') as fwrite:
#                         writer = csv.writer(fwrite)
#                         fwrite.write("\n".join(results))
#                         fwrite.close()
#                 #print name
#                 except Exception, e:
#                     print "Failed to write file",e
#                     sys.exit(2)
#                 del results[:]
#                 results.append(line[0:-1])
#             else:
#                 results.append(line[0:-1])
# except Exception, e:
#     print "Failed to read file",e
#     sys.exit(1)
# # this prints out the last textfile (nothing following it to compare with)
# try:
#     with open((name_prev)+".txt",'w') as fwrite:
#         writer = csv.writer(fwrite)
#         fwrite.write("\n".join(results))
#         fwrite.close()
                #print name
# except Exception, e:
#     print "Failed to write file",e
#     sys.exit(2)
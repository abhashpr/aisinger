# Version 1.1
import pandas as pd
import os
import numpy as np

OUTPUT_DIR=os.path.join(os.getcwd(), "output")
DATA_DIR=os.path.join(os.getcwd(), "data")
EXP_DIR=os.path.join(os.getcwd(), "exp")

phones_names = ["phone", "phone_id"]
ctm_names = ["uttr_id", "utt", "start", "dur", "phone_id"]
segments_names = ["uttr_id", "file", "start_utt", "end_utt"]

phones_file = os.path.join(EXP_DIR, "tri1", "phones.txt")
ali_file = os.path.join(OUTPUT_DIR, "merged_alignment.txt")
segments_file = os.path.join(OUTPUT_DIR, "segments.txt")

phones = pd.read_table(phones_file, sep=" ", names=phones_names)
segments = pd.read_table(segments_file, sep = "\t", header='infer')
segments['file'] = segments['file'].astype(object)

ctm = pd.read_table(ali_file, sep=" ", names=ctm_names)
ctm["file"] = ctm["uttr_id"]

ctm2 = pd.merge(ctm, phones, on="phone_id")
ctm3 = pd.merge(ctm2, segments, on=["uttr_id","file"])
# ctm3["start_real"] = ctm3["start"] + ctm3["uttr_start"]
# ctm3["end_real"] = ctm3["start_real"] + ctm3["dur"]

ctm3["st"] = np.round(ctm3["start"] + ctm3["uttr_start"], 5)
ctm3["ed"] = np.round(ctm3["st"] + ctm3["dur"], 5)

ctm3["st"] = np.round(ctm3["st"] * 1e7, 7)
ctm3["ed"] = np.round(ctm3["ed"] * 1e7, 7)

ctm3["st"] = ctm3["st"].astype('int')
ctm3["ed"] = ctm3["ed"] .astype('int')

ctm3["ph"] = ctm3["phone"].apply(lambda x: x.split("_")[0])

ctm3 = ctm3.sort_values(by=["uttr_id", "start"])
# print(ctm3.head())
ctm3.to_csv(os.path.join(OUTPUT_DIR, "final_ali.txt"), sep="\t", header=True, index=False)



# -------------
# Version 1.0
# -------------

# import pandas as pd
# import os
# import numpy as np

# OUTPUT_DIR=os.path.join(os.getcwd(), "output")
# DATA_DIR=os.path.join(os.getcwd(), "data")
# EXP_DIR=os.path.join(os.getcwd(), "exp")

# phones_names = ["phone", "phone_id"]
# ctm_names = ["uttr_id", "utt", "start", "dur", "phone_id"]
# segments_names = ["uttr_id", "file", "start_utt", "end_utt"]

# phones_file = os.path.join(EXP_DIR, "tri1", "phones.txt")
# ali_file = os.path.join(OUTPUT_DIR, "merged_alignment.txt")
# segments_file = os.path.join(OUTPUT_DIR, "segments.txt")

# phones = pd.read_table(phones_file, sep=" ", names=phones_names)

# ctm = pd.read_table(ali_file, sep=" ", names=ctm_names)
# ctm["file"] = ctm["uttr_id"]

# segments = pd.read_table(segments_file, sep = "\t", header='infer')
# segments['file'] = segments['file'].astype(object)

# print("Segments data...")
# print(segments.head())

# # segments["start_utt"] = segments["start_utt"].astype("float64")
# # segments["end_utt"] = segments["end_utt"].astype("float64")

# ctm2 = ctm.merge(phones, how="inner", on="phone_id")
# # ctm2 = ctm2.sort_values(by=["uttr_id", "start"])
# print(ctm2.head())

# ctm3 = ctm2.merge(segments, how="inner", on=["uttr_id", "file"])
# print(ctm3.head())
# ctm3 = ctm3[["uttr_id","file", "phone_id", "utt", "start", "dur", "phone", "uttr_start", "uttr_end"]]

# # print(ctm3.info())
# ctm3["st"] = np.round(ctm3["start"] + ctm3["uttr_start"], 5)
# ctm3["ed"] = np.round(ctm3["st"] + ctm3["dur"], 5)

# ctm3["st"] = np.round(ctm3["st"] * 1e7, 7)
# ctm3["ed"] = np.round(ctm3["ed"] * 1e7, 7)

# ctm3["st"] = ctm3["st"].astype('int')
# ctm3["ed"] = ctm3["ed"] .astype('int')

# ctm3["ph"] = ctm3["phone"].apply(lambda x: x.split("_")[0])

# ctm3 = ctm3.sort_values(by=["uttr_id", "start"])
# # print(ctm3.head())
# # utterances = ctm3[["st", "ed", "ph"]]
# ctm3.to_csv(os.path.join(OUTPUT_DIR, "final_ali.txt"), sep="\t", header=True, index=False)
# # utterances.to_csv(os.path.join(OUTPUT_DIR, "final_ali.txt"), sep="\t", header=True, index=False)

# ----------
# APPENDIX
# ----------

# *********
# R Code
# *********
# phones <- read.table("/Users/Eleanor/mycorpus/recipefiles/phones.txt", quote="\"")
# segments <- read.table("/Users/Eleanor/mycorpus/recipefiles/segments.txt", quote="\"")
# ctm <- read.table("/Users/Eleanor/mycorpus/recipefiles/merged_alignment.txt", quote="\"")

# names(ctm) <- c("file_utt","utt","start","dur","id")
# ctm$file <- gsub("_[0-9]*$","",ctm$file_utt)
# names(phones) <- c("phone","id")
# names(segments) <- c("file_utt","file","start_utt","end_utt")

# ctm2 <- merge(ctm, phones, by="id")
# ctm3 <- merge(ctm2, segments, by=c("file_utt","file"))
# ctm3$start_real <- ctm3$start + ctm3$start_utt
# ctm3$end_real <- ctm3$start_utt + ctm3$dur

# write.table(ctm3, "Users/Eleanor/mycorpus/recipefiles/final_ali.txt", row.names=F, quote=F, sep="\t")

# ***********
# Python Code
# ***********
# import pandas as pd

# phones = pd.read_table("/Users/Eleanor/mycorpus/recipefiles/phones.txt", quote="\"")
# segments = pd.read_table("/Users/Eleanor/mycorpus/recipefiles/segments.txt", quote="\"")
# ctm = pd.read_table("/Users/Eleanor/mycorpus/recipefiles/merged_alignment.txt", quote="\"")
# ctm.columns = ["file_utt","utt","start","dur","id"]
# ctm["file"] = ctm["file_utt"].str.replace("_[0-9]*$","")
# phones.columns = ["phone","id"]
# segments.columns = ["file_utt","file","start_utt","end_utt"]
# ctm2 = pd.merge(ctm, phones, on="id")
# ctm3 = pd.merge(ctm2, segments, on=["file_utt","file"])
# ctm3["start_real"] = ctm3["start"] + ctm3["start_utt"]
# ctm3["end_real"] = ctm3["start_utt"] + ctm3["dur"]
# ctm3.to_csv("Users/Eleanor/mycorpus/recipefiles/final_ali.txt", sep="\t", index=False, quoting=False)


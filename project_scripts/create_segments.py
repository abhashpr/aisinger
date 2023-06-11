import os
import pandas as pd

wavscp_file = os.path.join('data', 'train', 'wav.scp')
segments_file = os.path.join("output", "segments.txt")

print("Read " + wavscp_file + "..")
try:
    df = pd.read_table(wavscp_file, sep="\t", names=["uttr_id", "wavfile"])
except FileNotFoundError:
    print(wavscp_file + " not found.")

print(df.head())
print("Dropping WAVFILE path..")
df.drop(columns=["wavfile"], inplace=True)

df["file"] = df["uttr_id"]
df["uttr_start"] = 0
df["uttr_end"] = 0

print("Write segments file..")
df.to_csv(segments_file, sep="\t", index=False, header=True)
print("Finished creating the segments file")
print()

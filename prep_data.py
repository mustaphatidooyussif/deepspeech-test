import os 
import pandas as pd 
import csv

train_dir = 'C:/Users/Mustapha/Desktop/Nokwary/audios/wave/train'
dev_dir = 'C:/Users/Mustapha/Desktop/Nokwary/audios/wave/dev'
test_dir = 'C:/Users/Mustapha/Desktop/Nokwary/audios/wave/test'
path = "C:/Users/Mustapha/Desktop/Nokwary/audios/wave/clips/"
trans_file = "C:/Users/Mustapha/Desktop/Nokwary/audios/wave/original.tsv"
ignore = ['.git', 'original.txt', 'transcription.txt']
# print(os.listdir(path))
NUM_AUDIOS = 30
def encode_files(audios_dir, transcript_file):
    f =  open(transcript_file, 'r').readlines()
    audios = os.listdir(audios_dir)
    rows = []
    for i in range(NUM_AUDIOS):
        row = [audios_dir + audios[i], os.path.getsize(audios_dir + audios[i]), f[i][:-1]]
        rows.append(row) 
    return rows

data = encode_files(path, trans_file)

def train_dev_test_split(arr):
    train =  arr[: int(0.7*len(arr))]
    dev =  arr[int(0.7*len(arr)): int(0.9*len(arr))]
    test =  arr[int(0.9*len(arr)):]
    return train, dev , test 

train, dev , test  = train_dev_test_split(data)

with open(train_dir + '/train.csv', 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',')
    filewriter.writerow(['wav_filename','wav_filesize','transcript'])
    for r in train:
        filewriter.writerow(r)
    
with open(dev_dir + '/dev.csv', 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',')
    filewriter.writerow(['wav_filename','wav_filesize','transcript'])
    for r in dev:
        filewriter.writerow(r)
    
with open(test_dir + '/test.csv', 'w',  newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',')
    filewriter.writerow(['wav_filename','wav_filesize','transcript'])
    filewriter.writerows(test)

"""
This file contains preprocessing script for the combined csv (which made from splitted data)

EMSE_DevInt>python ./python/tokenize_csv.py D:\Victoria\EMSE\p2\EMSE_DevInt\python\data\data_processed\data.csv D:\Victoria\EMSE\p2\EMSE_DevInt\python\data\data_processed\processed_data.csv
"""
import pandas as pd
import sys
from lib.tokenization import process

def preprocess_title_and_text(datafilepath, savefilepath):
    data = pd.read_csv(datafilepath)
    titles_and_texts = data['title'] + " " + data['text']
    processed_data = titles_and_texts.map(process)
    data["processed_title_and_text"] = processed_data
    data.to_csv(savefilepath)
    print("Preprocessing ended successfully")


def main(argv):
    datafilepath = argv[1]
    savefilepath = argv[2]
    preprocess_title_and_text(datafilepath, savefilepath)


if __name__ == '__main__':
    main(sys.argv)

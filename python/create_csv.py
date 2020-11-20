"""
This file combines the splitted data to a csv file
Commandline call:
EMSE_DevInt>python ./python/create_csv.py D:\Victoria\EMSE\p2\EMSE_DevInt\python\data\data_splitted D:\Victoria\EMSE\p2\EMSE_DevInt\python\data\data_processed\data.csv
"""

import pandas as pd
import os
import sys


def combine_data(path):
    print(path)
    # Get all directories in the main directory
    dirs = os.listdir(path)

    
    # Define lists to store data
    texts = [] #track texts
    titles = []  # track titles
    errors = []  # track errored directories
    new_dirs = []  # track success directories
    
    # for printing
    i=0
    n=len(dirs)
    
    # loop over directories
    for _dir in dirs:
        if _dir != ".DS_Store": # omit os generated files
            
            try:
                # Obtain text
                with open(path+"/"+_dir+"/text.txt", "r") as f:
                    text = f.read()
                
                # Obtain title
                with open(path+"/"+_dir+"/title.txt", "r") as f:
                    title = f.read()
                
                # Store data in the lists
                texts.append(text)
                titles.append(title)
                new_dirs.append(_dir)
            except:
                # Collect the list of errored directories
                errors.append(_dir)
                
        # pring iteration
        i = i + 1
        print("Finished "+str(i)+"/"+str(n))
        
    # return all the lists
    return new_dirs, errors, titles, texts

def create_csv(new_dirs, titles, texts):
    list_of_tuples = list(zip(new_dirs,titles, texts))
    df = pd.DataFrame(list_of_tuples, columns=['dir','title', 'text'])
    return df

# Permission denied error
def save_csv(df, filepath):
    df.to_csv(filepath)
    
def main(argv):
    new_dirs, errors, titles, texts = combine_data(argv[1])
    df = create_csv(new_dirs, titles, texts)
    save_csv(df, argv[2])
    
if __name__ == '__main__':
    main(sys.argv)

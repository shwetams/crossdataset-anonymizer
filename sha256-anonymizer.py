## A simple script that loads CSV , reads the headers/ index values from configuration and outputs 
## an encrypted csv with the same name in a folder "encrypted" with encrypted columns

import hashlib
from enum import Enum
import sys, getopt
import csv

class FILE_TYPES(Enum):
    CSV = 1
    JSON = 2
    XML = 3

class File_Folder(Enum):
    FILE = 1
    FOLDER = 2

### Set the constant
FILE_TYPE = FILE_TYPES.CSV
Is_Header = True

def anonymize_csv(csv_dataset,cols_list):
    for row in csv_dataset:

        print(row)


def main(argv):
    input_path = ''
    headers = ''
    file_folder = None
    try:
        opts, args = getopt.getopt(argv)
        for opt, arg in opts:
            if opt in ('h','--help'):
                print("Need two arguments, input data folder and configuration file: crossdataset-anonymizer.py --file <input file path> OR --folder <input folder path> , --headers header1, heade2, header3 ")
            elif opt == '--file':
                file_folder = File_Folder.FILE
                input_path = arg
            elif opt == '--folder':
                file_folder = File_Folder.FOLDER
                input_path = arg
            elif opt == '--config':
                config_json_path = headers

    except getopt.GetoptError:
        print("Need two arguments, input data folder and configuration file: crossdataset-anonymizer.py --file <input file> OR --folder <input folder> , --headers header1, heade2, header3 ")
        sys.exit()
    
    ### Implementation for CSV
    if FILE_TYPE == FILE_TYPES.CSV:
        with open(input_path) as csv_file:
            csv_reader = csv.reader(csv_file,delimiter=',')
            anonymize_csv(csv_reader,headers)    
          







str = "9833732177"

result = hashlib.sha256(str.encode())

print(result.hexdigest())

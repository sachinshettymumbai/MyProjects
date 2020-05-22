from zipfile import ZipFile
import argparse

#Pass the full path of the zip file to be extracted(Source)
#Pass the full path where the conents of the zip file will be extracted(Destination)
#Assuming that the unzip.py file is in c:\myfiles folder. 
#The below is the example for the command to be typed in the Dos prompt. I am assuming that you have set your python path in the environment variable
#python C:\myfiles\unzip.py "c:\FilestoUnzip\abcd.zip" "c:\unzip"
#Replace the source and destination as per your requirement

parser = argparse.ArgumentParser(description='')
parser.add_argument('SourceZippath',metavar='N', type=str,help='Enter zip filename with path')
parser.add_argument('Destinationpath', metavar='N', type=str,help='Enter path to unzip')

args = parser.parse_args()


file_name = args.SourceZippath

with ZipFile(file_name, 'r') as zip:
    print('Extracting all the files now...')
    zip.extractall(path=args.Destinationpath)
    zip.printdir()

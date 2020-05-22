from zipfile import ZipFile
import argparse


parser = argparse.ArgumentParser(description='')
parser.add_argument('SourceZippath',metavar='N', type=str,help='Enter zip filename with path')
parser.add_argument('Destinationpath', metavar='N', type=str,help='Enter path to unzip')

args = parser.parse_args()


file_name = args.SourceZippath

with ZipFile(file_name, 'r') as zip:
    print('Extracting all the files now...')
    zip.extractall(path=args.Destinationpath)
    zip.printdir()

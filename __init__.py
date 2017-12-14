# -*- coding: utf-8 -*-
"""
This is a scprit to analyse HTS data from MSSR laboratory
"""


import glob, os, datetime, re

# Two dimentioanl array support
import numpy as np


# This script is specifically designated for TREF conversion of AnalystGT readout to .CSV file
# It can easily adjusted to parse any other AnalystGT file.
# Please note important variables:
#
# 1. Variable table515 contains data for 515 nm output. Lines from the begining of the table, designation of column numbers
# and ends at last line of data. Adjsut the line numbers upon changes.
#  
# 2. Variable table495 contains data for 495 nm output. Lines from the begining of the table, designation of column numbers
# and ends at last line of data. Adjsut the line numbers upon changes.
#  
# 3. Variable tableRatios contains data for 520/495 nm ratios . Lines from the begining of the table, designation of column numbers
# and ends at last line of data. Adjsut the line numbers upon changes.
#
# 4. Variable directory = "C:/Documents/TR-FRET/2016-09-27/". This is an example. Change to the path of your .txt diles that 
# contain data.
#
# 5. Variable  basename = "DL-*". Try using a notation, where you designate .txt files with prefix of the screen name followed by white space.
# A good exaple for the file name is <DL-1 01012016.txt>. You can also use a suffix; however, make sure 
# the file name notation ends with a space and a screen name. Example <01012016 DL-1.txt>. If you follow
# this notation, you have to make the following change:
# at the line: fout.write ( ('{0},{1},{2},{3},{4}{5}'.format((i.split()[1]).rstrip('.txt')
#
# Also, if you name has more than 2 strings separated by a space, adjust the index at "i.split()[1]"
#
# Cheers and good luck
#
# P.S. If I will have time, I will adjust the script to receive the former 5 parameters as arguments. Until then, just use
# the script in a Python shell.
#     

class plate():
    
    def __init__(self):
        
        # Read plate file into a two dimentional data array 
        
        return
    
    def normalize(self):
        return
    
    

    
def main(directory, basename, outfile=('output.csv') ):
    
    files = glob.glob1(directory, basename)
#    outfile=('{}-{}.csv'.format(datetime.date.today().strftime("%Y-%m-%d"), 
#                                basename.rstrip('-*')))
    outfile=('{}-{}.csv'.format(datetime.date.today().strftime("%Y-%m-%d"), 
                                'Validation'))
    print(outfile) 
#     outfile=('{}.csv'.format(datetime.date.today().strftime("%Y-%m-%d"))) 
                                  
    fout = open(outfile, 'w')
    fout.write ('Plate,520,495,520/495,DestinationWell,Date')
    fout.write('\n')
    for i in files:
        print ('parsing {}'.format(i))
        
        
        f=open(directory+i,'r')
        lines = f.readlines()
        loadTime = lines[0]
        table515 = lines[64:80]
        table495 = lines[85:101]
        tableRatios = lines[106:122]
        stringName = ('ABCDEFGHIJKLMNOP')
        
        
        
        
        for l in range(0,len(stringName)):
            for c in range(0,24):
#                print((i.split()[2]).rstrip('.txt'), end=',')
                if ((i.split()[0] ) != ('09262016')) :
                    fout.write ( ('{0},{1},{2},{3},{4}{5},{6}'.format((i.split()[2]).rstrip('.txt'),
                                             float(table515[l].split()[c+1]),
                                             float(table495[l].split()[c+1]),
                                             float(tableRatios[l].split()[c+1]),
                                             stringName[l],
                                             c+1,
                                             loadTime.split()[2])
                       ))
                    fout.write('\n')                  
                else:
                    fout.write ( ('{0},{1},{2},{3},{4}{5},{6}'.format((i.split()[1]).rstrip('.txt'),
                                             float(table515[l].split()[c+1]),
                                             float(table495[l].split()[c+1]),
                                             float(tableRatios[l].split()[c+1]),
                                             stringName[l],
                                             c+1,
                                             loadTime.split()[2])
                       ))
                    fout.write('\n') 
                
       
        
    
    print ('The number of parsed files is {}'.format(len(files)))
if __name__ == "__main__" : 
    directory = "z:/Documents/TR-FRET/2017-03-29-Validation/"
    basename = "49*"
#     basename = "09262016 TAR-1.txt"
    main(directory, basename)

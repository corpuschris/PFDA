import csv

FILENAME= "data.csv"
DATADIR = "C:\Users\Chris\Desktop\PFDA\mywork\week1\"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    for line in reader:
        print (line)

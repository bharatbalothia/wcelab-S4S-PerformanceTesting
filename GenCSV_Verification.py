# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 10:42:37 2020

@author: LayanaAbraham
"""


import csv
import sys

##data = csv.reader(open('Verification_final_ip.csv', 'r'), delimiter=",", quotechar='|')
shipnode, itemid = [], []

k=1
i=0
j=0
z=0

with open('Verification_final_ip.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        shipnode.append(row[0])
        itemid.append(row[1])
        #print(itemid)
    #print(len(shipnode))
    #print('itemlen',len(itemid))
    #for i in shipnode:
    #while(i<len(itemid)):
    while(z<30):
        filename="Verification"+str(k)+".csv"
        k=k+1
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            #writer.writerow(["shipnode", "itemid", "uom"])
            i=0 
            while(i<40):
                j=0
                #print(i)
                while(j<37):
                    #writer.writerow(['test', 'test1', "UNIT"])
                    ship1,ship2=shipnode[i].split('1::')
                    #print(ship1)
                    shipnodeName=ship1+str(z+1)+"::"+ship2
                    #print(shipnodeName)
                    itm1,itm2=itemid[j].split('1::')
                    itemName=ship1+str(z+1)+"::"+itm2
                    writer.writerow([shipnodeName, itemName, "UNIT"])
                    #print(k)
                    j=j+1
                i=i+1
            z=z+1        
                
    







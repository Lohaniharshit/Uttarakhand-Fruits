import csv
<<<<<<< HEAD
import matplotlib.pyplot as plt 
import argparse

with open('Dataset/Fruits(final).csv','r') as fruit:   
    read=csv.DictReader(fruit)
    headers=read.fieldnames


    places=[]
    fruits=[]
    season=[]
    month=[]
    reg={}
    seas={}
    month_percent={}
    c=0
    for line in read:
        fruits.append(line['Fruit'])
        places.append(line['Major Growing Region'])
        season.append(line['Season'])
        month.append(line['Month'])
    for i in range(len(places)):
        name=places[i].split(',')
        sea=season[i].split(',')

        reg[fruits[c]]=name
        seas[fruits[c]]=sea
        c+=1
    
    #    for i in range(7,len())
    #storing season keys and values in seperate lists
    sval=[]
    skey=list(seas.keys())
    for i in seas.values():
        sval.append(i[0])

    #Plotting fruit name vs season
    # print(sval)
    #plt.plot(skey,sval)
    #plt.show()

    
=======
from SoiltypeRatio import Soiltype
from givefruitforregion import get_fruits_by_region
from Monthly_Fruit_Growth import each_fruit


def main():
    file_path = 'Dataset/Fruits(final).csv'
    data=[]
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    query = '  RISHIKESH'


    each_fruit(data, query)


if __name__ == "__main__":
    main()
>>>>>>> main

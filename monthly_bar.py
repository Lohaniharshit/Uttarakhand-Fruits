import csv
import matplotlib.pyplot as plt 
import argparse

with open('Dataset/Fruits(final).csv','r') as fruit:   
    read=csv.DictReader(fruit)
    #Retrive Column names from fruit
    headers=read.fieldnames

    
    places=[]
    fruits=[]
    season=[]
    month=[]
    reg={}
    seas={}
    month_percent={}
    c=0
    #
    for line in read:
        fruits.append(line['Fruit'])
        places.append(line['Major Growing Region'])
        season.append(line['Season'])
        month.append(line['Month'])

    print(fruits)
    #
    for i in range(len(places)):
        name=places[i].split(',')
        sea=season[i].split(',')

        reg[fruits[c]]=name
        seas[fruits[c]]=sea
        c+=1

    #Storing header as keys 
    for i in range(7,len(headers)):
        key=headers[i]
        month_percent[key]=[]
    #print(month_percent.keys())

    #reset file cursor to start
    fruit.seek(0)
    #skip over header row
    next(read)

    for row in read:
        for key in headers[7:]:
            month_percent[key].append(row[key])
    #print(month_percent.values())

    #storing season keys and values in seperate lists
    sval=[]
    skey=list(seas.keys())
    for i in seas.values():
        sval.append(i[0])

    #month_percent plot
    month_val=[]
    month_key=list(month_percent.keys())
    for i in month_percent.values():
        month_val.append(i[0])

    #
    fruit_dict={}
    for i in range(len(fruits)):
        fruit_dict[i]=fruits[i]

    #print(fruit_dict)
    #
    n = str(input("Enter fruit name: "))
    fruit_key=0
    for key,value in fruit_dict.items():
        if value.lower()==n.lower():
            fruit_key=key
            

    #
    k=[]
    p=[]
    for key in month_percent:
        p.append(key)
        k.append(month_percent[key][fruit_key])
    print(k)
    print(p)
    #Plotting Fruit% vs 
    plt.bar(p,k)
    plt.xlabel("Months")
    plt.ylabel("Percentage Growth")
    plt.yticks(['0','5','10','15','20','25','30','35','40','45','50'])
    plt.show()



import csv
import matplotlib.pyplot as plt

# Open the CSV file
with open('Dataset\Fruits(final).csv','r') as csvfile:
    # Create a CSV reader object
    reader = csv.DictReader(csvfile)
    winter=0
    summer=0
    spring=0
    for i in reader:
        if(i['Season']=='Winter'):
            winter+=1
        elif(i['Season']=='Summer'):
            summer+=1
        else:
            spring+=1
    labels=['Winter','Summer','Spring']
    ratios=[winter,summer,spring]
    plt.pie(ratios,labels=labels,autopct='%1.1f%%')
    plt.title('Season wise Distribution of Fruits')
    plt.show()
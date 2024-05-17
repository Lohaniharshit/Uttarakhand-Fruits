import csv
import matplotlib.pyplot as plt

# Open the CSV file
with open('Dataset\Fruits(final).csv','r') as csvfile:
    # Create a CSV reader object
    reader = csv.DictReader(csvfile)
    loamy=0
    sandy=0
    clayey=0
    for i in reader:
        if(i['Soil Type']=='Loamy'):
            loamy+=1
        elif(i['Soil Type']=='Sandy'):
            sandy+=1
        else:
            clayey+=1
    labels=['Loamy','Sandy','Clayey']
    ratios=[loamy,sandy,clayey]
    plt.pie(ratios,labels=labels,autopct='%1.1f%%')
    plt.title('Soil wise Distribution of Fruits')
    plt.show()
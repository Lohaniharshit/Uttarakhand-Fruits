import csv
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

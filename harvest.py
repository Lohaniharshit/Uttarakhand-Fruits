import csv
import matplotlib.pyplot as plt

FILE_PATH = "Dataset/Fruits(final).csv"


def monthly_fruit_growth(n, p, k):
    """
    Plot the monthly growth percentage of a given fruit.
    """
    plt.bar(p, k, color="skyblue")
    plt.xlabel("Months")
    plt.ylabel("Percentage Growth")
    plt.title(f"Growth Percentage of {n}")

    plt.yticks(range(0, 31, 5))  # Ensuring y-ticks are displayed at intervals of 5
    plt.xticks(rotation=45)
    plt.show()


def seasonwisefruits(data):
    """
    Analyzes the distribution of fruits across different seasons and visualizes it as a pie chart.
    """
    winter = 0
    summer = 0
    spring = 0

    for entry in data:
        if entry["Season"] == "Winter":
            winter += 1
        elif entry["Season"] == "Summer":
            summer += 1
        elif entry["Season"] == "Spring":
            spring += 1

    labels = ["Winter", "Summer", "Spring"]
    ratios = [winter, summer, spring]

    plt.pie(ratios, labels=labels, autopct="%1.1f%%")
    plt.title("Season-wise Distribution of Fruits")
    plt.show()


def soiltype(data):
    """
    Analyzes the distribution of different soil types and visualizes it as a pie chart.
    """
    loamy = 0
    sandy = 0
    clayey = 0

    for entry in data:
        if entry["Soil Type"] == "Loamy":
            loamy += 1
        elif entry["Soil Type"] == "Sandy":
            sandy += 1
        elif entry["Soil Type"] == "Clayey":
            clayey += 1

    labels = ["Loamy", "Sandy", "Clayey"]
    ratios = [loamy, sandy, clayey]

    plt.pie(ratios, labels=labels, autopct="%1.1f%%")
    plt.title("Soil-wise Distribution of Fruits")
    plt.show()


def get_fruits_by_region(data, query_region):
    fruits_in_region = []
    query_region = query_region.lower().strip()

    for fruit in data:
        regions = fruit["Major Growing Region"].lower().split(",")
        for region in regions:
            if region.lower().strip() == query_region:
                fruits_in_region.append(fruit["Fruit"])
                break

    plot_fruit_availability(data, fruits_in_region)
    return fruits_in_region

def plot_fruit_availability(reader, fruit_list):
    # Iterate through each row in the CSV
    for row in reader:
        # Check if the current fruit is in the fruit_list
        if row['Fruit'].lower() in [fruit.lower() for fruit in fruit_list]:
            plot_fruit(row)

def plot_fruit(fruit_data):
    months = ['Jan (%)', 'Feb (%)', 'Mar (%)', 'Apr (%)', 'May (%)', 'Jun (%)',
              'Jul (%)', 'Aug (%)', 'Sep (%)', 'Oct (%)', 'Nov (%)', 'Dec (%)']
    availability = [int(fruit_data[month].strip('%')) for month in months]

    plt.figure(figsize=(10, 5))
    plt.bar(months, availability)
    plt.title(f'Seasonal Availability of {fruit_data["Fruit"]}')
    plt.xlabel('Month')
    plt.ylabel('Percentage Availability')
    plt.show()


def main():
    with open(FILE_PATH, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)  # Convert reader to list of dictionaries
        # Retrieve column names from fruit
        headers = reader.fieldnames

        places = []
        fruits = []
        season = []
        month = []
        regions = []
        reg = {}
        seas = {}
        month_percent = {}
        c = 0

        for line in data:
            fruits.append(line["Fruit"])
            places.append(line["Major Growing Region"])
            season.append(line["Season"])
            month.append(line["Month"])

        for i in range(len(places)):
            name = places[i].split(",")
            sea = season[i].split(",")
            reg[fruits[c]] = name
            seas[fruits[c]] = sea
            c += 1

        # Storing header as keys
        for i in range(7, len(headers)):
            key = headers[i]
            month_percent[key] = []

        for row in data:
            for key in headers[7:]:
                month_percent[key].append(row[key])

        # storing season keys and values in separate lists
        sval = []
        skey = list(seas.keys())
        for i in seas.values():
            sval.append(i[0])

        # month_percent plot
        month_val = []
        month_key = list(month_percent.keys())
        for i in month_percent.values():
            month_val.append(i[0])
        #

        #

        fruit_dict = {}
        for i in range(len(fruits)):
            fruit_dict[i] = fruits[i]

        query = input("Choose Region or Fruit: ").strip()
        if query.lower() == "region":
            print(regions)
            query_region = input("Enter region name: ").strip()
            fruits_in_region = get_fruits_by_region(data, query_region)
            print(f"Fruits in {query_region}: {', '.join(fruits_in_region)}")


        elif query.lower() == "fruit":
            for i in fruits:
                print(i)
            n = input("Enter fruit name: ").strip()
            fruit_key = None
            for key, value in fruit_dict.items():
                if value.lower() == n.lower():
                    fruit_key = key
                    break

            if fruit_key is not None:
                k = []
                p = []
                for key in month_percent:
                    p.append(key)
                    k.append(int(month_percent[key][fruit_key]))

            monthly_fruit_growth(n, p, k)
        else:
            print(f"Fruit '{n}' not found in the dataset.")
            seasonwisefruits(data)
            soiltype(data)


if __name__ == "__main__":
    main()

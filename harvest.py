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
 
def seasonwisefruits(data) -> None:
    """
    Analyzes the distribution of fruits across different seasons and visualizes it as a pie chart.
    @parameters: 
    @returns:
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


def soiltype(data) -> None:
    """
    Analyzes the distribution of different soil types and visualizes it as a pie chart.
    @returns:
    @parameters:
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
 
def get_fruits_by_region(data, query_region, month_percent):
    fruits_in_region = []
    query_region = query_region.lower().strip()
 
    for fruit in data:
        regions = fruit["Major Growing Region"].lower().split(",")
        for region in regions:
            if region.lower().strip() == query_region:
                fruits_in_region.append(fruit["Fruit"])
                break
 
    # Call plot_fruit_availability to generate graphs for each fruit
    plot_fruit_availability(data, fruits_in_region, month_percent)
 
    return fruits_in_region
 
 
def plot_fruit_availability(reader, fruit_list, month_percent):
    # Iterate through each row in the CSV
    for row in reader:
        # Check if the current fruit is in the fruit_list
        if row['Fruit'].lower() in [fruit.lower() for fruit in fruit_list]:
            k = []
            p = []
            for key in month_percent:
                p.append(key)
                k.append(int(month_percent[key][row["Fruit"]]))
            monthly_fruit_growth(row['Fruit'], p, k)
 
 
def main():
    with open(FILE_PATH, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)  # Convert reader to list of dictionaries
        headers = reader.fieldnames
 
        places = []
        fruits = []
        season = []
        month = []
 
        for line in data:
            fruits.append(line["Fruit"])
            places.append(line["Major Growing Region"])
            season.append(line["Season"])
            month.append(line["Month"])
 
        
        month_percent = {}

        for header in headers[7:]:
            percentages = {}
            for row in data:
                percentages[row["Fruit"]] = row[header]
            month_percent[header] = percentages
 
        query = input("Choose Region or Fruit: ").strip()
        if query.lower() == "region":
            regions_list = set()
            for regions in places:
                for region in regions.split(','):
                    regions_list.add(region.strip())
            for i in regions_list:
                print(i)
            print("All")
            query_region = input("Enter region name: ").strip().lower()
            if query_region == "all":
                seasonwisefruits(data)
                soiltype(data)
            else:
                fruits_in_region = get_fruits_by_region(data, query_region, month_percent)
                print(f"Fruits in {query_region}: {', '.join(fruits_in_region)}")
                plot_fruit_availability(reader, fruits_in_region, month_percent)
 
        elif query.lower() == "fruit":
            for i in fruits:
                print(i)
            print("All")
            n = input("Enter fruit name: ").strip().lower()
            if n in fruits:
                p = list(month_percent.keys())
                k = [int(month_percent[key][n]) for key in p]
                monthly_fruit_growth(n, p, k)
            elif n == "all":
                seasonwisefruits(data)
                soiltype(data)
            else:
                print(f"Fruit '{n}' not found in the dataset.")
 
        else:
            print(f"Invalid choice: {query}")
            return
 
 
if __name__ == "__main__":
    main()

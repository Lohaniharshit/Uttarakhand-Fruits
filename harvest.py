import csv
import matplotlib.pyplot as plt

FILE_PATH = "Dataset/Fruits(final).csv"


def monthly_fruit_growth(n: str, p, k) -> None:
    """
    Plot the monthly growth percentage of a given fruit.

    @param n: Name of the fruit.
    @param p: List of months.
    @param k: List of growth percentages corresponding to the months.
    @returns: None
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

    @param data: List of dictionaries representing rows of the CSV file.
    @returns: None
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

    @param data: List of dictionaries representing rows of the CSV file.
    @returns: None
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


def get_fruits_by_region(data, query_region: str):
    """
    Retrieves fruits grown in a specific region and plots their availability.

    @param data: List of dictionaries representing rows of the CSV file.
    @param query_region: The region to query.
    @param month_percent: Dictionary with monthly percentage data for each fruit.
    @returns: List of fruits grown in the queried region.
    """
    fruits_in_region = []
    query_region = query_region.lower().strip()

    for fruit in data:
        regions = fruit["Major Growing Region"].lower().split(",")
        for region in regions:
            if region.lower().strip() == query_region:
                fruits_in_region.append(fruit["Fruit"])
                break

    return fruits_in_region


def plot_fruit_availability(reader, fruit_list, month_percent) -> None:
    """
    Plots the availability of fruits based on the monthly percentage data.

    @param reader: List of dictionaries representing rows of the CSV file.
    @param fruit_list: List of fruits to plot.
    @param month_percent: Dictionary with monthly percentage data for
                          each fruit.
    @returns: None
    """
    for row in reader:
        if row['Fruit'].lower() in [fruit.lower() for fruit in fruit_list]:
            k = []
            p = []
            for key in month_percent:
                p.append(key)
                k.append(int(month_percent[key][row["Fruit"]]))
            monthly_fruit_growth(row['Fruit'], p, k)


def main() -> None:
    """
    Main function to run the script. It loads the CSV data, extracts months
    and percentages, and interacts with the user.

    @returns: None
    """
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
            elif query_region not in regions_list:
                print(f"Invalid Region :{query_region}")
            else:
                fruits_in_region = get_fruits_by_region(data, query_region)
                print(f"Fruits in {query_region}: {', '.join(fruits_in_region)}")
                plot_fruit_availability(data, fruits_in_region, month_percent)

        elif query.lower() == "fruit":
            for i in fruits:
                print(i)
            print("All")
            fruit_query = input("Enter fruit name: ").strip().capitalize()
            if fruit_query in fruits:
                p = list(month_percent.keys())
                k = []
                for key in p:
                    k.append(int(month_percent[key][fruit_query]))

                monthly_fruit_growth(fruit_query, p, k)
            elif fruit_query == "All":
                seasonwisefruits(data)
                soiltype(data)
            else:
                print(f"Fruit '{fruit_query}' not found in the dataset.")

        else:
            print(f"Invalid choice: {query}")
            return


if __name__ == "__main__":
    main()

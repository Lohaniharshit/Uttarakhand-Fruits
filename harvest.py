import csv
import argparse
from code.Monthly_plot import monthly_fruit_growth
from code.Soiltype import soiltype
from code.Seasonewisefruits import seasonwisefruits
from code.Plotfruitavailability import plot_fruit_availability
from code.Getfruitsbyregion import get_fruits_by_region

FILE_PATH = "Dataset/Fruits(final).csv"

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
        if headers is not None:
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
            query_region = input("Enter region name: ").strip().capitalize()
            if query_region == "All":
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
                month_names = list(month_percent.keys())
                monthly_data = []
                for key in month_names:
                    monthly_data.append(int(month_percent[key][fruit_query]))

                monthly_fruit_growth(fruit_query, month_names, monthly_data)
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

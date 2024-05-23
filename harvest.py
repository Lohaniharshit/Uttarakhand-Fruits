import csv
import argparse
from code.Monthly_plot import monthly_fruit_growth
from code.Soiltype import soiltype
from code.Seasonewisefruits import seasonwisefruits
from code.Plotfruitavailability import plot_fruit_availability
from code.Getfruitsbyregion import get_fruits_by_region

FILE_PATH = "Dataset/Fruits(final).csv"


def main() -> None:

    data, headers = Readerfunction()
    places, fruits = List_data_generator(data)
    month_percent = month_percent_generator(headers, data)

    parser = argparse.ArgumentParser(description='Provide either a fruit name or a region name')
    # Define the mutually exclusive group
    group = parser.add_mutually_exclusive_group(required=True)
    fruits.append('All')
    places.add('All')

    # Add the arguments to the group
    group.add_argument('--fruit', help='Enter name of the fruit', choices=fruits)
    group.add_argument('--region', help='Enter name of the region', choices=places)

    args = parser.parse_args()

    if args.fruit:
        fruit_query = args.fruit
        fruit_query.capitalize()
        if fruit_query in fruits:
            month_names = list(month_percent.keys())
            monthly_data = []
            for key in month_names:
                monthly_data.append(int(month_percent[key][fruit_query]))

            monthly_fruit_growth(fruit_query, month_names, monthly_data)
        elif fruit_query == "All":
            seasonwisefruits(data)
            soiltype(data)
    elif args.region:
        region_query = args.region
        region_query.capitalize()
        if region_query == "All":
            seasonwisefruits(data)
            soiltype(data)
        else:
            fruits_in_region = get_fruits_by_region(data, region_query)
            print(f"Fruits in {region_query}: {', '.join(fruits_in_region)}")
            plot_fruit_availability(data, fruits_in_region, month_percent)


def Readerfunction():
    with open(FILE_PATH, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)  # Convert reader to list of dictionaries
        headers = reader.fieldnames
        return data, headers


def List_data_generator(data):
    places = []
    fruits = []
    for line in data:
        fruits.append(line["Fruit"])
        places.append(line["Major Growing Region"])
    regions_list = set()
    for regions in places:
        for region in regions.split(','):
            regions_list.add(region.strip())
    return regions_list, fruits


def month_percent_generator(headers, data):
    month_percent = {}
    for header in headers[7:]:
        percentages = {}
        for row in data:
            percentages[row["Fruit"]] = row[header]
        month_percent[header] = percentages
    return month_percent


if __name__ == "__main__":
    main()

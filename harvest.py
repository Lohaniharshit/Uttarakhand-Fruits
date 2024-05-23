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
    Main function to handle fruit or region queries and generate respective
    plots and data.

    @returns: None
    """
    data, headers = reader_function()
    places, fruits = list_data_generator(data)
    month_percent = month_percent_generator(headers, data)

    parser = argparse.ArgumentParser(
        description='Provide either a fruit name or a region name'
        )
    # Define the mutually exclusive group
    group = parser.add_mutually_exclusive_group(required=True)
    fruits.append('All')
    places.add('All')

    # Add the arguments to the group
    group.add_argument(
        '--fruit',
        help='Enter name of the fruit',
        choices=fruits
                        )
    group.add_argument(
        '--region',
        help='Enter name of the region',
        choices=places)

    args = parser.parse_args()

    if args.fruit:
        if args.fruit in fruits:
            month_names = list(month_percent.keys())
            monthly_data = []
            for key in month_names:
                monthly_data.append(int(month_percent[key][args.fruit]))

            monthly_fruit_growth(args.fruit, month_names, monthly_data)
        elif args.fruit == "All":
            seasonwisefruits(data)
            soiltype(data)
    elif args.region:
        if args.region == "All":
            seasonwisefruits(data)
            soiltype(data)
        else:
            fruits_in_region = get_fruits_by_region(data, args.region)
            print(f"Fruits in {args.region}: {', '.join(fruits_in_region)}")
            plot_fruit_availability(data, fruits_in_region, month_percent)


def reader_function() -> tuple:
    """
    Reads the CSV file and returns the data and headers.

    @returns: A tuple containing a list of dictionaries with the data and
              a list of headers.
    """
    with open(FILE_PATH, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
        headers = reader.fieldnames
        return data, headers


def list_data_generator(data: list) -> tuple:
    """
    Generates lists of places and fruits from the data.

    @param data: List of dictionaries containing the CSV data.
    @returns: A tuple containing a set of regions and a list of fruits.
    """
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


def month_percent_generator(headers: list, data: list) -> dict:
    """
    Generates a dictionary with month-wise percentages for each fruit.

    @param headers: List of headers from the CSV file.
    @param data: List of dictionaries containing the CSV data.
    @returns: A dictionary with month names as keys and dictionaries of
              fruit percentages as values.
    """
    month_percent = {}
    for header in headers[7:]:
        percentages = {}
        for row in data:
            percentages[row["Fruit"]] = row[header]
        month_percent[header] = percentages
    return month_percent


if __name__ == "__main__":
    main()

import argparse
from code.List_data_generator import list_data_generator
from code.Month_percent_generator import month_percent_generator
from code.Reader import reader_function
from code.Monthly_plot import monthly_fruit_growth
from code.Soiltype import soiltype
from code.Seasonewisefruits import seasonwisefruits
from code.Plotfruitavailability import plot_fruit_availability
from code.Getfruitsbyregion import get_fruits_by_region

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

            monthly_fruit_growth(fruit_query, month_names, monthly_data)
        elif fruit_query == "All":
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

if __name__ == "__main__":
    main()

import argparse
from code.List_data_generator import list_data_generator
from code.Month_percent_generator import month_percent_generator
from code.Reader import lazy_load_csv
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
    gen = lazy_load_csv(FILE_PATH)
    headers = next(gen)  # Extract headers first
 
    # Using generator directly in list_data_generator
    places, fruits = list_data_generator(gen)
 

    # Rewind the generator again for month_percent_generator
    gen = lazy_load_csv(FILE_PATH)
    next(gen)  # Skip headers again
 
    month_percent = month_percent_generator(headers, gen, lazy_load_csv, FILE_PATH)
 
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
        choices=places
    )
 
    args = parser.parse_args()
 
    if args.fruit:
        if args.fruit == "All":
            gen = lazy_load_csv(FILE_PATH)
            next(gen)  # Skip headers again
            seasonwisefruits(gen)
            gen = lazy_load_csv(FILE_PATH)
            next(gen)  # Skip headers again
            soiltype(gen)
        elif args.fruit in fruits:
            month_names = list(month_percent.keys())
            monthly_data = []
            for key in month_names:
                fruit_percent = month_percent[key].get(args.fruit, 0)
                monthly_data.append(int(fruit_percent))
            monthly_fruit_growth(args.fruit, month_names, monthly_data)
    elif args.region:
        if args.region == "All":
            gen = lazy_load_csv(FILE_PATH)
            next(gen)  # Skip headers again
            seasonwisefruits(gen)
            gen = lazy_load_csv(FILE_PATH)
            next(gen)  # Skip headers again
            soiltype(gen)
        else:
            gen = lazy_load_csv(FILE_PATH)
            next(gen)  # Skip headers again
            fruits_in_region = get_fruits_by_region(gen, args.region)
            print(f"Fruits in {args.region}: {', '.join(fruits_in_region)}")
            gen = lazy_load_csv(FILE_PATH)
            next(gen)  # Skip headers again
            plot_fruit_availability(gen, fruits_in_region, month_percent)
 
main()

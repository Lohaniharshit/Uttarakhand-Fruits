import argparse
from code.fruits_regions import Fruit_region_list
from code.monthly_percentage import month_percentage
from code.csv_reader import lazy_load_csv
from code.plot_fruit import monthly_fruit_growth
from code.soil import soiltype
from code.season import seasonwisefruits
from code.plot_region import plot_fruit_availability
from code.fruits_by_region import get_fruits_by_region
 
def main() -> None:
    """
    Main function to handle fruit or region queries and generate respective
    plots and data.
 
    @returns: None
    """
    headers = lazy_load_csv('headers')
    gen = lazy_load_csv('data')
    # Using generator directly in list_data_generator
    places, fruits = Fruit_region_list(gen)
 

    # Rewind the generator again for month_percent_generator
    gen = lazy_load_csv('data')
 
    month_percent = month_percentage(headers, gen, lazy_load_csv) 
    parser = argparse.ArgumentParser(
        description='Provide either one or more fruit names or region names '
    )
    # Define the mutually exclusive group
    group = parser.add_mutually_exclusive_group(required=True)
    fruits.append('All')
    places.add('All')
 
    # Add the arguments to the group
    group.add_argument(
        '--fruit',
        help='Enter name(s) of the fruit(s)',
        nargs='+',
        choices=fruits
    )
    group.add_argument(
        '--region',
        help='Enter name(s) of the region(s)',
        nargs='+',
        choices=places
    )
 
    args = parser.parse_args()
    if args.fruit:
        if 'All' in args.fruit:
            gen = lazy_load_csv('data')
            seasonwisefruits(gen)
            gen = lazy_load_csv('data')
            soiltype(gen)
        else:
            fruit_queries = args.fruit
            for fruit_query in fruit_queries:
                fruit_query = fruit_query.capitalize()
                if fruit_query in fruits:
                    month_names = list(month_percent.keys())
                    monthly_data = []
                    for key in month_names:
                        monthly_data.append(int(month_percent[key][fruit_query]))

                    monthly_fruit_growth(fruit_query, month_names, monthly_data)

    elif args.region:
        if 'All' in args.region:
            gen = lazy_load_csv('data')
            seasonwisefruits(gen)
            gen = lazy_load_csv('data')
            soiltype(gen)
        else:
            region_queries = args.region
            for region_query in region_queries:
                gen = lazy_load_csv('data')
                fruits_in_region = get_fruits_by_region(gen, region_query)
                print(f"Fruits in {region_query}: {', '.join(fruits_in_region)}")
                gen = lazy_load_csv('data')
                plot_fruit_availability(gen, fruits_in_region, month_percent, region_query)
 
main()

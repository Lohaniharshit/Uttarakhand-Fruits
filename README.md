# Uttarakhand Fruits Analysis

This project analyzes and visualizes data related to the growth, distribution, and seasonal availability of various fruits in Uttarakhand. The data is sourced from a CSV file containing information on different fruits, including their growing regions, soil types, and monthly growth percentages.

## Features

- **Monthly Fruit Growth Visualization**: Plots the monthly growth percentage of a selected fruit.
- **Season-wise Fruit Distribution**: Displays the distribution of fruits across different seasons as a pie chart.
- **Soil Type Distribution**: Shows the distribution of different soil types for fruit cultivation as a pie chart.
- **Region-wise Fruit Availability**: Lists and plots the availability of fruits in a selected region.

## Requirements

- Python 3.12.3
- `matplotlib` library



## Usage

The main script `harvest.py` accepts either one or more fruit names or a region names as input.

```bash
python3 harvest.py --fruit Apple Banana
python3 harvest.py --region Dehradun Rishikesh
```
## Running Tests

```bash
python3 test_harvest.py 
```

### Additional options:

--fruit: Specify the name(s) of the fruit(s) to analyze.

--region: Specify region(s) instead of a fruit(s).


### Command Line Arguments

The script uses the argparse module to handle command line arguments. Here are the available options:

--fruit: Specify the name of the fruit(s) to analyze.

--region: Specify the name of the region(s) to analyze.


## Contributing

Contributions are welcome! If you find any bugs or have suggestions for
improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE.md).

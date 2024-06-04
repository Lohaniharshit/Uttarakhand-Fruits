import matplotlib.pyplot as plt
from collections import defaultdict

def soiltype(data) -> None:
    """
    Analyzes the distribution of different soil types and visualizes it as a
    pie chart.

    @param data: List of dictionaries representing rows of the CSV file.
    @returns: None
    """
    ratio_dict = defaultdict(int)
    for entry in data:
        ratio_dict[entry["Soil Type"]]+=1

    plt.pie(ratio_dict.values(), labels=ratio_dict.keys(), autopct="%1.1f%%")
    plt.title("Soil-wise Distribution of Fruits")
    plt.show()

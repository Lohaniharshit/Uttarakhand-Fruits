import matplotlib.pyplot as plt
from collections import defaultdict

def seasonwisefruits(data) -> None:
    """
    Analyzes the distribution of fruits across different seasons and
    visualizes it as a pie chart.

    @param data: List of dictionaries representing rows of the CSV file.
    @returns: None
    """
    ratio_dict = defaultdict(int)

    for entry in data:
        ratio_dict[entry["Season"]]+=1

    plt.pie(ratio_dict.values(), labels=ratio_dict.keys(), autopct="%1.1f%%")
    plt.title("Season-wise Distribution of Fruits")
    plt.show()



import matplotlib.pyplot as plt
def soiltype(data) -> None:
    """
    Analyzes the distribution of different soil types and visualizes it as a
    pie chart.

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

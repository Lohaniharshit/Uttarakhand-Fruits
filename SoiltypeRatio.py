import matplotlib.pyplot as plt


def Soiltype(data,):
    """
    Analyzes the distribution of different soil types from the given data and
    visualizes the distribution as a pie chart.

    Parameters:
    data (list of dict): A list of dictionaries where each dictionary
    represents a data entry with a 'Soil Type' key.
    query (str, optional): An optional parameter for future extensibility.
    Currently not used in this function.

    Returns:
    None
    """
    loamy = 0
    sandy = 0
    clayey = 0

    for entry in data:
        if entry['Soil Type'] == 'Loamy':
            loamy += 1
        elif entry['Soil Type'] == 'Sandy':
            sandy += 1
        elif entry['Soil Type'] == 'Clayey':
            clayey += 1

    labels = ['Loamy', 'Sandy', 'Clayey']
    ratios = [loamy, sandy, clayey]

    plt.pie(ratios, labels=labels, autopct='%1.1f%%')
    plt.title('Soil-wise Distribution of Fruits')
    plt.show()

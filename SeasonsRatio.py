import matplotlib.pyplot as plt


def SeasonWiseFruits(data):
    """
    Analyzes the distribution of fruits across different seasons from the given
    data and visualizes the distribution as a pie chart.

    Parameters:
    data (list of dict): A list of dictionaries where each dictionary
    represents a data entry with a 'Season' key.

    Returns:
    None
    """
    winter = 0
    summer = 0
    spring = 0

    for entry in data:
        if entry['Season'] == 'Winter':
            winter += 1
        elif entry['Season'] == 'Summer':
            summer += 1
        elif entry['Season'] == 'Spring':
            spring += 1

    labels = ['Winter', 'Summer', 'Spring']
    ratios = [winter, summer, spring]

    plt.pie(ratios, labels=labels, autopct='%1.1f%%')
    plt.title('Season-wise Distribution of Fruits')
    plt.show()

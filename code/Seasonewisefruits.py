import matplotlib.pyplot as plt
def seasonwisefruits(data) -> None:
    """
    Analyzes the distribution of fruits across different seasons and
    visualizes it as a pie chart.

    @param data: List of dictionaries representing rows of the CSV file.
    @returns: None
    """
    winter = 0
    summer = 0
    spring = 0

    for entry in data:
        if entry["Season"] == "Winter":
            winter += 1
        elif entry["Season"] == "Summer":
            summer += 1
        elif entry["Season"] == "Spring":
            spring += 1

    labels = ["Winter", "Summer", "Spring"]
    ratios = [winter, summer, spring]

    plt.pie(ratios, labels=labels, autopct="%1.1f%%")
    plt.title("Season-wise Distribution of Fruits")
    plt.show()



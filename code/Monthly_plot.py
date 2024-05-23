import matplotlib.pyplot as plt
def monthly_fruit_growth(fruit_query: str, month_names, monthly_data) -> None:
    """
    Plot the monthly growth percentage of a given fruit.

    @param n: Name of the fruit.
    @param p: List of months.
    @param k: List of growth percentages corresponding to the months.
    @returns: None
    """
    plt.bar(month_names, monthly_data, color="skyblue")
    plt.xlabel("Months")
    plt.ylabel("Percentage Growth")
    plt.title(f"Growth Percentage of {fruit_query}")

    plt.yticks(range(0, 31, 5))
    plt.xticks(rotation=45)
    plt.show()

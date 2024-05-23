from code.Monthly_plot import monthly_fruit_growth

def plot_fruit_availability(reader, fruit_list, month_percent) -> None:
    """
    Plots the availability of fruits based on the monthly percentage data.

    @param reader: List of dictionaries representing rows of the CSV file.
    @param fruit_list: List of fruits to plot.
    @param month_percent: Dictionary with monthly percentage data for
                          each fruit.
    @returns: None
    """
    for row in reader:
        if row['Fruit'].lower() in [fruit.lower() for fruit in fruit_list]:
            monthly_data = []
            month_names = []
            for key in month_percent:
                month_names.append(key)
                monthly_data.append(int(month_percent[key][row["Fruit"]]))
            monthly_fruit_growth(row['Fruit'], month_names, monthly_data)




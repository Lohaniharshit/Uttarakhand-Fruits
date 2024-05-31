from code.plot_fruit import monthly_fruit_growth
import matplotlib.pyplot as plt

def plot_fruit_availability(reader, fruit_list, month_percent, region_name) -> None:
    """
    Plots the availability of fruits based on the monthly percentage data.

    @param reader: List of dictionaries representing rows of the CSV file.
    @param fruit_list: List of fruits to plot.
    @param month_percent: Dictionary with monthly percentage data for
                          each fruit.
    @param region_name: Name of the region.                      
    @returns: None
    """
    month_names = [] 
    for key in month_percent:
        month_names.append(key)
    width = 0 
    bar0 = []
    # For full screen display
    plt.subplots(figsize=(15, 8)) 
    for row in reader:
        if row['Fruit'].lower() in [fruit.lower() for fruit in fruit_list]:
            monthly_data = []
            for key in month_percent:
                monthly_data.append(int(month_percent[key][row["Fruit"]]))
            bar0=[x for x in range(1,len(month_names)+1)]
            bar=[x+width for x in bar0]
            width+=0.2
            plt.bar(bar, monthly_data, 0.2, label=row['Fruit'])  
    plt.xlabel("Months")                                 
    plt.ylabel("Percentage Growth")                      
    plt.title(f"Month wise Growth Percentage of Fruits in {region_name} Region")     
    plt.yticks(range(0, 31, 5))
    positions=[x+0.1 for x in range(1,13)]
    plt.xticks(positions,month_names,rotation=45) 
    plt.legend()
    plt.show()         

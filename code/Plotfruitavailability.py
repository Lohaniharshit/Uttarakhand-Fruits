from code.Monthly_plot import monthly_fruit_growth
import matplotlib.pyplot as plt

def plot_fruit_availability(reader, fruit_list, month_percent, region_name) -> None:
    """
    Plots the availability of fruits based on the monthly percentage data.

    @param reader: List of dictionaries representing rows of the CSV file.
    @param fruit_list: List of fruits to plot.
    @param month_percent: Dictionary with monthly percentage data for
                          each fruit.
    @returns: None
    """
    month_names = [] 
    for key in month_percent:
        month_names.append(key)
    w=0 
    bar=[]
    # Create a figure with a large size for full screen display
    fig, ax = plt.subplots(figsize=(15, 8)) 
    for row in reader:
        if row['Fruit'].lower() in [fruit.lower() for fruit in fruit_list]:
            monthly_data = []
            for key in month_percent:
                monthly_data.append(int(month_percent[key][row["Fruit"]]))
            bar=[x for x in range(1,len(month_names)+1)]
            bar2=[x+w for x in bar]
            w+=0.2
            plt.bar(bar2, monthly_data, 0.2, label=row['Fruit'])  
    plt.xlabel("Months")                                 
    plt.ylabel("Percentage Growth")                      
    plt.title(f"Month wise Growth Percentage of Fruits in {region_name} Region")     
    plt.yticks(range(0, 31, 5))
    positions=[x+0.1 for x in range(1,13)]
    plt.xticks(positions,month_names,rotation=45) 
    plt.legend()
    plt.show()         

def month_percentage(header_obj: list, data_gen, lazy_load_csv_func) -> dict:
    """
    Returns a dictionary with month-wise percentages for each fruit.
 
    @param headers: List of headers from the CSV file.
    @param data_gen: Generator yielding dictionaries containing the CSV data.
    @param lazy_load_csv_func: Function to lazily load the CSV file.
    @returns: A dictionary with month names as keys and dictionaries of
              fruit percentages as values.
    """
    month_percent = {}
    headers=list(next(header_obj))    
    if headers is not None:
        for header in headers[7:]:  # Assuming the first 7 columns are not months
            percentages = {}
            for row in data_gen:
                fruit = row["Fruit"]
                percentage = row.get(header, 0)  # Default to 0 if not present
                percentages[fruit] = int(percentage) if percentage else 0
            month_percent[header] = percentages
            # Rewind generator to the start for the next header
            data_gen = lazy_load_csv_func('data')   
        return month_percent

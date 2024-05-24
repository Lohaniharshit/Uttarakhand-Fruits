def month_percent_generator(headers: list, data: list) -> dict:
    """
    Generates a dictionary with month-wise percentages for each fruit.

    @param headers: List of headers from the CSV file.
    @param data: List of dictionaries containing the CSV data.
    @returns: A dictionary with month names as keys and dictionaries of
              fruit percentages as values.
    """
    month_percent = {}
    for header in headers[7:]:
        percentages = {}
        for row in data:
            percentages[row["Fruit"]] = row[header]
        month_percent[header] = percentages
    return month_percent

import csv
def reader_function() -> tuple:
    """
    Reads the CSV file and returns the data and headers.

    @returns: A tuple containing a list of dictionaries with the data and
              a list of headers.
    """
    FILE_PATH = "Dataset/Fruits(final).csv"
    with open(FILE_PATH, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
        headers = reader.fieldnames
        return data, headers

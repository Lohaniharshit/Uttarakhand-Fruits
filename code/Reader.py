import csv
def lazy_load_csv(FILE_PATH):
    """
    Reads the CSV file and returns the data and headers.

    @returns: A tuple containing a list of dictionaries with the data and
              a list of headers.
    """
    with open(FILE_PATH, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames
        yield headers  # First, yield the headers
        for row in reader:
            yield row  # Then, yield each row as a dictionary

import csv
 
def lazy_load_csv(file_path):
    """
    Generator to lazily load CSV data.
 
    @param file_path: Path to the CSV file.
    @yields: First, yields the headers as a list, then yields each row as a dictionary.
    """
    with open(file_path, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames
        yield headers  # First, yield the headers
        for row in reader:
            yield row  # Then, yield each row


import csv

FILE_PATH = "Dataset/Fruits(final).csv"

def lazy_load_csv(request):
    """
    Generator to lazily load CSV data.
 
    @param request: Decides whether to yield headers or data 
    @yields: Yields the headers as a list or yields each row as a dictionary.
    """
    with open(FILE_PATH, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        if request == 'headers':
            headers = reader.fieldnames
            yield headers
        elif request == 'data':
            for row in reader:
                yield row

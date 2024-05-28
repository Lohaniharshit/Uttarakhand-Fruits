import csv
import unittest
from harvest import get_fruits_by_region

FILE_PATH = "Dataset/Fruits(final).csv"

with open(FILE_PATH, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)  # Convert reader to list of dictionaries
    headers = reader.fieldnames


class TestBarGraph(unittest.TestCase):
    month_percent = {}
    if headers is not None:
        for header in headers[7:]:
            percentages = {}
            for row in data:
                percentages[row["Fruit"]] = row[header]
        month_percent[header] = percentages

    def test_initialization(self) -> None:
        listoffruits = get_fruits_by_region(data, 'Shimla')
        self.assertEqual(listoffruits, ['Apple'])



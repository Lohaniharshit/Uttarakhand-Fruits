def get_fruits_by_region(data, query_region: str):
    """
    Retrieves fruits grown in a specific region and plots their availability.

    @param data: List of dictionaries representing rows of the CSV file.
    @param query_region: The region to query.
    @param month_percent: Dictionary with monthly percentage data for each
     fruit.
    @returns: List of fruits grown in the queried region.
    """
    fruits_in_region = []
    query_region = query_region.lower().strip()

    for fruit in data:
        regions = fruit["Major Growing Region"].lower().split(",")
        for region in regions:
            if region.lower().strip() == query_region:
                fruits_in_region.append(fruit["Fruit"])
                break

    return fruits_in_region

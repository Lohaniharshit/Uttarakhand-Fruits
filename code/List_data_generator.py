def list_data_generator(data: list) -> tuple[set,list]:
    """
    Generates lists of places and fruits from the data.

    @param data: List of dictionaries containing the CSV data.
    @returns: A tuple containing a set of regions and a list of fruits.
    """
    places = []
    fruits = []
    for line in data:
        fruits.append(line["Fruit"])
        places.append(line["Major Growing Region"])
    regions_list = set()
    for regions in places:
        for region in regions.split(','):
            regions_list.add(region.strip())
    return regions_list, fruits



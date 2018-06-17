items = [{"pastel de belem": ["Portugal", "Lisbon", "Belem"]},
         {"croissant": ["Paris", "France"]},
         {"pizza": ["Rome", "Italy", "Lisbon"]},
         {"bitoque": ["Lisbon", "Portugal"]},
         {"laptop": ["France", "Italy", "Portugal"]}]

result = [{"Portugal": ["pastel de belem", "laptop", "bitoque"]},
          {"Lisbon": ["pastel de belem", "bitoque", "pizza"]},
          {"Belem": ["pastel de belem"]},
          {"Paris": ["croissant"]},
          {"France": ["croissant", "laptop"]},
          {"Rome": ["pizza"]},
          {"Italy": ["pizza", "laptop"]}]


def get_location_names(items_array):
    result_array = []
    aux_dict = {}
    # iterates over the items list
    for index in range(len(items_array)):
        # gets the first key from the dict since we only have one anyway
        key = next(iter(items_array[index]))
        # iterates over the location list in each object
        for index2 in range(len(items_array[index][key])):
            aux_dict.setdefault(items_array[index][key][index2], []).append(key)
    # iterate over the aux_dict to make the final list with the objects inside
    for key, v in aux_dict.iteritems():
        result_array.append({key: v})
    return result_array


print get_location_names(items)

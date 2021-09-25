def transpose(lists: list) -> list:
    return list(map(list, zip(*lists)))

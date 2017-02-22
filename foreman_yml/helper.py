

def filterbyname(list, name):
    """Find an element with it's name

    Args:
        list (list): List of elements
        name (str): Element name to look for

    Returns:
        int: Id of element if found, Raises Exception otherwise
    """
    for el in list['results']:
        if el['name'] == name:
            return el['id']
    else:
        raise Exception

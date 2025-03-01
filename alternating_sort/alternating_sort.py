def alternating_sort(data):
    """
    Sorts a list by alternating between removing smaller and larger elements,
    with the specified behavior.

    Args:
        data: The list to sort.

    Returns:
        A new list containing the sorted elements.
    """

    if not data:
        return []

    result = [data[0]]
    data = data[1:]
    ascending = True  # Start by removing smaller elements

    while data:
        if ascending:
            if data[0] >= result[-1]:
                result.append(data[0])
                data = data[1:]
                ascending = False
            else:
                data = data[1:]
        else:
            if data[0] <= result[-1]:
                result.append(data[0])
                data = data[1:]
                ascending = True
            else:
                data = data[1:]

    return result
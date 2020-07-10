def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    data = {}

    for i, weight in enumerate(weights):
        data[weight] = i

    for i, weight in enumerate(weights):
        if limit - weight in data:
            return (data[limit-weight], i)

    return None

def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    data = {}

    for arr in arrays:
        for elem in arr:
            if elem in data.keys():
                data[elem] += 1
            else:
                data[elem] = 1
    
    result = [x[0] for x in data.items() if x[1] == len(arrays)]
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])


    print(intersection(arrays))

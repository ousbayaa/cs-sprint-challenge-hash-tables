def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    numbs = {}
    result = []

    for number in a:
        numbs[number] = 1
        if number != 0 and -number in numbs:
            result.append(abs(number))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

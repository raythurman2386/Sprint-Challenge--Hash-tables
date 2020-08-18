def intersection(arrays):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []
    # Your code here
    # go through each array inside the array
    for array in arrays:
        # Loop over each item of the inner array
        for index in array:
            # if that item isn't in the cache
            if index not in cache:
                # initialize it to the cache with a value of 1
                cache[index] = 1
            else:
                # otherwise increment the value
                cache[index] += 1

    # Loop over the cahce
    for k, v in cache.items():
        # if the value is equal to the length of the main arrays
        if v >= len(arrays):
            # add that number to the results
            result.append(k)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

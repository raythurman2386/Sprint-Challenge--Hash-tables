def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    my_table = {}

    # loop through each INDEX of the array
    for index in range(len(weights)):
        # If it is not in the dict
        if weights[index] not in my_table:
            # add the limit - the weight of the index to the dict
            # as the key, with the index as the value
            my_table[limit - weights[index]] = index
        else:
            # Arrange the index's to return thhe higher number
            if my_table[weights[index]] > index:
                return (my_table[weights[index]], index)
            else:
                return (index, my_table[weights[index]])

    return None


w = [4, 6, 10, 15, 16]
print(get_indices_of_item_weights(w, 5, 21))

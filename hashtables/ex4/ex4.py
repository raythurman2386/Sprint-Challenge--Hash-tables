def has_negatives(a):
    """
    YOUR CODE HERE
    """
    pos_cache, neg_cache = {}, {}
    result = []
    # Your code here
    for item in a:
        if item >= 0:
            pos_cache[item] = item
        else:
            neg_cache[item] = item

    for k in neg_cache.keys():
        if abs(k) in pos_cache:
            result.append(abs(k))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

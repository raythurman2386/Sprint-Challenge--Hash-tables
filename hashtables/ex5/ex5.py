# Your code here
def finder(files, queries):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []

    for file in files:
        # split the file and get just the filename of every file
        file_arr = file.split('/')
        file_name = file_arr[-1]

        # Add every filename to the cache as a key
        if file_name not in cache:
            # make the value an array, with the full file path of the file
            cache[file_name] = [file]
        else:
            # If the file name exists,
            # add the files full path to the existing array for that filename
            cache[file_name].append(file)

    for query in queries:
        # Check to see if the query is a key in the cache
        if query in cache.keys():
            # if it is, loop over each file in that query entry to the cache
            for file in cache[query]:
                # add those files to the results
                result.append(file)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))

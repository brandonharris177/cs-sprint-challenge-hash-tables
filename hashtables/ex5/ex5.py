# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    file_paths = {}

    for total_file in files:
        file_key = total_file.split("/")
        file_key = file_key[len(file_key)-1]
        if file_key not in file_paths:
            file_paths[file_key] = []
        file_paths[file_key].append(total_file)

    # print(file_paths)

    result = []

    for query in queries:
        if query in file_paths:
            for path in file_paths[query]:
                result.append(path)

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

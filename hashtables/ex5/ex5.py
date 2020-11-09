""" FILE FINDER

1. Understand:
    a. Goal: return all full paths that match inputted full file paths and filename
    b. Input: full file paths, list of filenames to query
    c. Output: all full paths from list that match filename

2. Plan:
    a. iterate to find the filename in each path
    b. add the path if filename is there
    c. if it isnt, add to the dictionary
    d. iterate through query array
    e. add all the paths that has a filename equal to the query


3. Execute:
"""
path_dict = {}

def finder(files, queries):
    global path_dict

    result = []

    for path in files:
        # find the filename in each path
        full_path = path
        path = path.split('/')
        filename = path[-1]

        # if the filename is there already, add the new path
        if filename in path_dict:
            path_dict[filename].append(full_path)

        # if not, add it to path_dict 
        else:
            path_dict[filename] = [full_path]

    # iterate the query array and 
    # add each path that has a filename that is equal to the query
    for query in queries:
        if query in path_dict:
            for file_path in path_dict[query]:
                result.append(file_path)

    path_dict = {}
    return result

"""
4. Review
"""

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


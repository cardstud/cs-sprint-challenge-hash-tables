"""
# Positive and Negative

1. Undestand
    a. Goal: find which positive numbers have corresponding negative numbers
    b. Input:   list of integers
    c. Output:  list of +/- number pairs
    d. Input can be in any order
    e. Output can be in any order
    f. Use a hash table to solve
    g. Constraints: input list can contain about 5,000,000 elements

    Test cases
    ----------
    Input:  [ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]
    Output: [ 1, 3, 4 ]

2. Plan:
    a. 



3. Execute:
"""
number_dict = {}

def has_negatives(a):
    global number_dict

    result = []

    for num in a:
        #if the opposite of the number exists then add to result
        if num - (num*2) in number_dict:
            result.append(abs(num))

        # if not in dictionary, add it
        if num not in number_dict:
            number_dict[num] = num

        # if in dictionary, keep going
        if num in number_dict:
            continue
        
    number_dict = {}

    return result

"""
4. Review
"""
if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
    print(has_negatives([1,2,3,-4]))

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

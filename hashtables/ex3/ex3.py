""" INTERSECTION OF MULTIPLE LISTS

1. Understand:
    Goal: find intersection of multiple lists of integers

    Test case
    ---------
    Input: list of lists
            [1,2,3,4,5]
            [12,7,2,9,1]
            [99,2,7,1]
        
    Output: (1,2)

2. Plan:
    
    NOTE: skipping this one. 

"""



if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

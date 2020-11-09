
""" MERGING TWO PACKAGES

1. Understand:
    Goal: Create a function that finds two items whose sum of weights equals the weight limit	(function is: get_indices_of_item_weights)

    Inputs:
        a. package with weight limit: 	limit
        b. list of item weights:	    weights
        c. length of weights array:     length  

     Output: 
        a. tuple of integers (0, 1) where each element represents the item weights of two packages 
           (put higher valued index first, lower second = (higher value weight, lower value weight)

        b. if the pair does not exist for given inputs, return None

    Note: Solution should run in linear time

    Test cases
    ----------
    Input:	weights = [4,6,10,15,16]
            length  = 5
            limit   = 21

    Output: (3,1)	(since these are indices of weights 15 and 6, whose sum = 21)

    Input: weights = [1,2,3,4]
           length  = 4
           limit   = 5

    Output: (2,1)

    Input: weights = [4,4]
           length  = 2
           limit   = 8

2. Plan:
        a. using (limit-weight) = result, loop through weights to find that value
            - if it is there, return that weight and the result(2nd weight)
            - if not, return None

3. Execute:
"""
def get_indices_of_item_weights(weights, length, limit):
    table = dict()

    for weight in range(length):
        result = limit - weights[weight]
        if result in table:
            return(weight, table[result])
        else:
            table[weights[weight]] = weight
    return None

"""
4. Review
"""
print(get_indices_of_item_weights([4,6,10,15,16], 5, 21))
print(get_indices_of_item_weights([1,2,3,4], 4, 5))
print(get_indices_of_item_weights([4,4], 2, 8))

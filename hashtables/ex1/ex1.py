def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    hash_table = {}

    count = 0

    for weight in weights:
        hash_table[weight] = count
        count += 1

    return(hash_table)

    # return result

weights_3 = [4, 6, 10, 15, 16]
print(get_indices_of_item_weights(weights_3, 5, 21))

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    intersections = {}

    for number in a:
        absolute = abs(number)
        if absolute not in intersections:
            intersections[absolute] = 1
        else: 
            intersections[absolute] += 1

    flipped = {} 
  
    for key, value in intersections.items(): 
        if value not in flipped: 
            flipped[value] = [key] 
        else: 
            flipped[value].append(key) 

    result = []

    if 2 in flipped:
        result = flipped[2]

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
    print(has_negatives([1, 2, 3]))

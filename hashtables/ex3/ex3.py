import operator

def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    intersections = {}

    for single_list in arrays:
        for number in single_list:
            if number not in intersections:
                intersections[number] = 1
            else: 
                intersections[number] += 1

    flipped = {} 
  
    for key, value in intersections.items(): 
        if value not in flipped: 
            flipped[value] = [key] 
        else: 
            flipped[value].append(key) 

    result = flipped[len(arrays)]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])


    # arrays.append([1,2,3]),
    # arrays.append([1,3,5]),
    # arrays.append([1,6,7])


    print(intersection(arrays))

def convert_vector(numbers):
    value = []
    for number, w in enumerate(numbers):
        if w != 0:
            value.append((number, w))
    return dict(value)


print (convert_vector([0,0,2,5,0,4,0,0,0,0,1]))
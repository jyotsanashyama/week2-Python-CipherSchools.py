#generate lists with range functions
#index method
#pass list to a function

numbers = list(range(1,11))
print(numbers)

numbers.pop()
print(numbers)

print(numbers.index(1,3))

def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative

print(negative_list(numbers))
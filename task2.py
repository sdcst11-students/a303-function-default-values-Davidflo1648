#!python3
"""
Create a function called multiplication that takes 2 input paremeters:
number: integer.  
end: integer. It should have a default value of 12.

The function will create a LIST that stores the multiplication tables for the number, and ends at end.

return value:
list.  The multiplication tables starting at a multiple of 1 and ending at whatever the default value is.

example assertion:
assert multiplication(5) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
assert multiplication(2,5) == [2, 4, 6, 8, 10]
"""
def multiplication(num, end = 12):
    #mult_of_nums = []
    #while mult < end:
        #mult = 1
        #multiples = mult * num
        #mult += 1
        #mult_of_nums.append(multiples)

    return [num * i for i in range(1, end + 1)]

print(multiplication(2, 5))

#if __name__ == "__main__":
    #assert multiplication(5) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
    #assert multiplication(2,5) == [2, 4, 6, 8, 10]
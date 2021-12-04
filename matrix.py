equation1 = [7,9,5,6,4]
equation2 = [1,6,7,3,8]
equation3 = [9,6,2,4,5]
equation4 = [5,1,6,7,4]

matrix = [equation1,equation2,equation3,equation4]

print("matrix:",matrix)

def multiplyNumbers(mul):
    total = 1
    for equation in mul:
        for number in equation:
            total *= number
    print("Multiplication of these numbers:",total)

multiplyNumbers(matrix)

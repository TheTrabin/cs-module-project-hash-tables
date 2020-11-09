# Your code here
'''
exps(x, y, z) =
     if x <= 0: y + z
     if x >  0: exps(x-1,y+1,z) + exps(x-2,y+2,z*2) + exps(x-3,y+3,z*3)

     Set up dictionary
     Based on above.
     Range is 10, Test involves iteration, 3 scales.
     i of 2/3/4 = x
     Print information.
'''
dictionary = {}

def expensive_seq(x, y, z):
    # Your code here
# Dictionary
    if (x,y,z) in dictionary:
        return dictionary[(x,y,z)]

    expense = 0
    if x <=0:
        expense = y + z
    if x > 0:
        expense = expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)

    dictionary[(x,y,z)] = expense
    return expense

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))

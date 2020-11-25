def eq(x,y):
    if(x == y):
        return 0
    if(x > y):
        return x-y
    if y % 2 == 0:    
        return 1 + eq(x, y/2)       
    else:
       return 1 + eq(x, y+1)
x = int(input())
y = int(input())
print(eq(x,y))

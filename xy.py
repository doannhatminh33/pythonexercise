def eq(x,y):
    count=0
    times ="{} times"
    while x != y:
        if x >y/2:
           x-=1
           count+=1
        else:
            x*=2
            count+=1
    print(times.format(count))
eq(int(input()),int(input()))1
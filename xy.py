def eq(x,y):
    count=0
    times ="{} times"
    while x != y:
        if y%2==0:    
            if x >y/2:
               x-=1
               count+=1
            else:
                x*=2
                count+=1
        else:
            if x > (y+1)/2:
                x-=1
                count+=1
            elif x <(y+1)/2:
                x*=2
                count+=1
            elif x == (y+1)/2:
                x*=2
                count+=1
                x-=1
                count+=1
    print(times.format(count))
eq(int(input()),int(input()))

f = [1,0,1,-2]
def func(f, x):
    sum=0
    temp=0
    for i in range(len(f)):
        sum+=f[i]*(x**(len(f)-1-temp))
        temp+=1
        
    return sum
def falseposition(f, xl, xu, epsilon):
    old_x = 0

    while True:
        # Calculate the new point using false position method
        new_x = (xu * func(f, xl) - xl * func(f, xu)) / (func(f, xl) - func(f, xu))

        # Check if it meets the condition of f(xl) * f(new_x) < 0
        if func(f, xl) * func(f, new_x) < 0:
            xu = new_x
        else:
            xl = new_x

        # Check the threshold value to stop the iteration
        if abs((new_x - old_x) / new_x) * 100 < epsilon:
            return new_x

        # Update old_x for the next iteration
        old_x = new_x
x=falseposition(f, -2, 2, .005)
xr = falseposition(f, xl, xu, epsilon)
print("Approximate xr:", xr)
func(f,x)

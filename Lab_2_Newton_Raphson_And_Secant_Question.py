f = [1,-2,0,4]

df = [3,-4,0]

def func(f, x):
    sum=0
    temp=0
    for i in range(len(f)):
        sum+=f[i]*(x**(len(f)-1-temp))
        temp+=1

    return sum


def newton_raphson(f, df, x0, tol):
    x_old = x0

    while True:
        # Use the equation x_new = x_old - f(x) / df(x), to get the updated value
        x_new = x_old - func(f, x_old) / func(df, x_old)
        
        # Check the tolerance level with the equation relative_error = abs((x_old - x_new) / x_new) * 100
        relative_error = abs((x_old - x_new) / x_new) * 100
        
        # If the relative error is below tolerance level, return the x value.
        if relative_error < tol:
            return x_new
        
        # Update the x_old value
        x_old = x_new


# Use the equation with the tolerance level of 0.0001
result = newton_raphson(f, df, 5, 0.00001)


# check if we get f(x) = 0
func(f, result)

def secant(f, x_current, x_prev, tol):
    while True:
        # Use the equation x_next = x_current - (f(x_current) * (x_current - x_prev)) / (f(x_current) - f(x_prev)), to get the updated value
        x_next = x_current - (func(f, x_current) * (x_current - x_prev)) / (func(f, x_current) - func(f, x_prev))
        
        # Check the tolerance level with the equation relative_error = abs((x_next - x_current) / x_next) * 100
        relative_error = abs((x_next - x_current) / x_next) * 100
        
        # If the relative error is below tolerance level, return the x_next value.
        if relative_error < tol:
            return x_next
        
        # Update the x_prev and x_current value
        x_prev = x_current
        x_current = x_next


# Use the equation with the tolerance level of 0.0001
result = secant(f, 5, 7,  0.00001)


# check if we get f(x) = 0
print (func(f,result))

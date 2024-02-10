# Execute this cell to test how the function works

def func(x, f):
    result = 0
    start = len(f) - 1
    for i in range(len(f)):
        result += f[start] * (x ** i)
        start -= 1
    return result
# result = f[0]*x^3+f[1]*x^2+f[2]*x+f[3]*1

f = [1, -2, 0, 4]

print(func(5, f))

rae = []
iteration = []
flag = 0

def bisection_method(f, xl, xu, epsilon):
    global rae, iteration, flag
    while True:
        xm = (xl + xu) / 2
        f_xl = func(xl, f)
        f_xm = func(xm, f)
        if f_xl * f_xm < 0:
            xu = xm
        else:
            xl = xm

        relative_error = abs((xu - xl) / xu) * 100

        rae.append(relative_error)
        iteration.append(xm)

        if relative_error <= epsilon:
            flag = 1
            break

    if flag == 1:
        return xm, rae, iteration

xl = 0
xu = 2
epsilon = 0.01

root, rae, iteration = bisection_method(f, xl, xu, epsilon)
print("Root of the equation:", root)
print("Relative Approximate Error:", rae)
print("Iterations:", iteration)

def square_sum(a, b):
    c = a**2 + b**2;
    a = a + 1;
    b = b + 1;
    return (a, b, c);

# 这里使用的是引用
def square_sum1(x):
    x[0] = x[0] + 1;
    return x;

a = 3;
b = 4;
square_sum(a, b)
print(a, b);

x = [3, 4];
square_sum1(x);
print(x);
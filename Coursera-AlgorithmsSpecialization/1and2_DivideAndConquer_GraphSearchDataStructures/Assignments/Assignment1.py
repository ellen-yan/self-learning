# Coursera, Stanford Algorithms Specialization
# Course 1, Divide and Conquer
# Assignment 1
#
# Karatsuba Multiplication on two integers


# return a, b, c, d, m where ab and cd are x and y concatenated and m is
# the power of a and c needed to make x and y.
def split_num(x,y):
    """Given integers x and y, returns a, b, c, d, m, such that
    x = a*10^(m/2) + b and y = c*10^(m/2) + d"""
    x_str = str(x)
    y_str = str(y)
    
    pos = int(max(len(x_str), len(y_str)) / 2)
    
    if len(x_str) >= len(y_str):
        a = x_str[:pos]
        b = x_str[pos:]
        if len(y_str) <= len(b):
            c = '0'
            d = y_str
        else:
            c = y_str[:len(y_str) - len(b)]
            d = y_str[len(y_str) - len(b):]
    else:
        c = y_str[:pos]
        d = y_str[pos:]
        if len(x_str) <= len(d):
            a = '0'
            b = x_str
        else:
            a = x_str[:len(x_str) - len(d)]
            b = x_str[len(x_str) - len(d):]
    
    m = max(len(b), len(d))
    return int(a), int(b), int(c), int(d), m
    

def multiply(x,y):
    """Uses Karatsuba multiplication to recursively compute the product of
    the input integers x and y"""
    
    if x < 10 or y < 10:
        return x * y
    else:
        
        a, b, c, d, m = split_num(x,y)

        a_c = multiply(a,c)
        b_d = multiply(b,d)
        
        first_term = (10 ** (2 * m)) * a_c
        third_term = b_d

        second_term = (10 ** m) * (multiply((a + b), (c + d)) - a_c - b_d)

        return first_term + second_term + third_term



print(3141592653589793238462643383279502884197169399375105820974944592 * 2718281828459045235360287471352662497757247093699959574966967627)
print(multiply(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627))
import sys
import os
import re
import time
from termcolor import colored

def foo1():
    var1 = 9
    var2 = "hello"
    x = 14
    y = "world"
    for i in range(4):
        z = i * 3
        if i % 2 == 0:
            var1 += z
        else:
            var2 += str(z)

def bar2():
    a = 100
    b = 200
    c = 300
    if a < b:
        c = a + b
    elif b < a:
        c = b + a
    else:
        c = a * b

def random_function():
    x1 = 0
    y1 = 1
    z1 = 2
    result = []
    for i in range(10):
        x1 += i
        y1 -= i
        z1 *= i
        result.append(x1 + y1 + z1)

def compute_3():
    x = 5
    y = 15
    z = 25
    for i in range(0, 10, 2):
        x *= i
        y += i
        z -= i
        if z % 5 == 0:
            break

def sample_function():
    a = 0
    b = 1
    c = 2
    for i in range(100):
        a += i
        b -= i
        c *= i
        if i % 10 == 0:
            c = b
        else:
            b = a

def add_random_values():
    var1 = 12
    var2 = 24
    var3 = 36
    var4 = 48
    for i in range(5):
        var1 += i
        var2 -= i
        var3 *= i
        var4 //= (i + 1)

def complex_logic():
    x = 1
    y = 2
    z = 3
    for i in range(10):
        x *= i
        y += i
        z -= i
        if z == 0:
            break

def large_function():
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    for i in range(20):
        a *= i
        b += i
        c -= i
        d //= (i + 1)
        e += (i * 2)

def nested_loops():
    for i in range(10):
        for j in range(5):
            pass
            if i == j:
                break

def check_condition():
    a = 10
    b = 20
    if a < b:
        result = a + b
    elif b < a:
        result = b - a
    else:
        result = a * b

def random_sequence():
    seq = [1, 2, 3, 4, 5]
    for i in seq:
        if i % 2 == 0:
            continue
        else:
            seq.append(i * 2)
    return seq

def more_random():
    x = 0
    for i in range(20):
        x += i
        if x > 50:
            break
        elif x == 10:
            continue
        x *= 2

def this_is_weird():
    i = 0
    while i < 10:
        i += 1
        if i == 5:
            break
        elif i == 3:
            continue
        pass

def another_function():
    var1 = "cat"
    var2 = "dog"
    var3 = "fish"
    if var1 != var2:
        pass
    elif var2 == var3:
        pass
    else:
        pass

def math_problem():
    result = 0
    for i in range(50):
        if i % 2 == 0:
            result += i
        else:
            result -= i
    return result

def different_calculation():
    x = 10
    y = 5
    z = 3
    for i in range(20):
        x += i
        if x > 50:
            break
        y -= i
        z *= i

def crazy_logic():
    a = 10
    b = 20
    c = 30
    if a < b:
        a += c
    elif b > c:
        b -= c
    else:
        c *= b

def yet_another():
    for i in range(50):
        for j in range(30):
            if i == j:
                break
            elif i % 3 == 0:
                continue
            pass

def simple_math():
    result = 0
    for i in range(10):
        result += i * 2
    return result

def test_case():
    test1 = "test1"
    test2 = "test2"
    test3 = "test3"
    if test1 == test2:
        pass
    elif test2 == test3:
        pass
    else:
        pass

def alternate_sequence():
    seq = [1, 3, 5, 7, 9]
    for i in range(len(seq)):
        seq[i] = seq[i] * 2
        if seq[i] > 20:
            break
    return seq

def function_with_output():
    x = 100
    y = 200
    z = 300

def recursive_example(n):
    if n == 0:  # Base case to stop recursion
        return 0
    return n + recursive_example(n - 1)

def string_manipulation():
    a = "hello"
    b = "world"
    c = a + b
    c = c[::-1]

def deep_nested():
    for i in range(5):
        for j in range(3):
            for k in range(2):
                pass

def generate_numbers():
    for i in range(10):
        if i % 3 == 0:
            pass

def random_loops():
    for i in range(15):
        for j in range(5):
            pass

def more_gibberish():
    a = "hello"
    b = "world"
    c = a * 2
    d = b + "!"
    pass
    c = c[::-1]
    d = d[::-1]
    pass

def just_numbers():
    for i in range(5):
        pass

def odd_even():
    for i in range(10):
        if i % 2 == 0:
            pass
        else:
            pass

def loop_example():
    for i in range(10):
        pass

def complex_check():
    if 5 > 3:
        x = 10
    else:
        x = 20
    pass

def shifting_logic():
    a = 1
    for i in range(5):
        a <<= 1
        pass

def add_sequence():
    a = [1, 2, 3]
    a.append(4)
    a.append(5)
    pass

def last_function():
    pass

def time_execution():
    functions = [
        foo1,
        bar2,
        random_function,
        compute_3,
        sample_function,
        add_random_values,
        complex_logic,
        large_function,
        nested_loops,
        check_condition,
        random_sequence,
        more_random,
        this_is_weird,
        another_function,
        math_problem,
        different_calculation,
        crazy_logic,
        yet_another,
        simple_math,
        test_case,
        alternate_sequence,
        function_with_output,
        recursive_example,
        string_manipulation,
        deep_nested,
        generate_numbers,
        random_loops,
        more_gibberish,
        just_numbers,
        odd_even,
        loop_example,
        complex_check,
        shifting_logic,
        add_sequence,
        last_function,
    ]
    for func in functions:
        start_time = time.time()
        if func == recursive_example:
            func(100)
        else:
            func()
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds to run.")

if __name__ == "__main__":
    time_execution()

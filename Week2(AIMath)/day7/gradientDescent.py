import sympy as sym
from sympy.abc import x
import numpy as np

def func(val):
    fun = sym.poly(x**2 + 2*x + 3)
    return fun.subs(x,val), fun

def func_gradient(fun,val):
    _, function = func(val)
    diff = sym.diff(function, x)
    return diff.subs(x , val) , diff

def gradient_descent(fun, init_point, lr_rate = 1e-2, epsilon = 1e-5):
    cnt = 0
    val = init_point    
    diff, _ = func_gradient(fun, init_point)
    while abs(diff) > epsilon:
        val -= lr_rate * diff
        diff, _ = func_gradient(fun, val)
        cnt += 1
    print(f"함수 : {fun(val)[1]}, 연산횟수 : {cnt} , 최소점 : ({val} , {fun(val)[0]})")

gradient_descent(fun = func, init_point = np.random.uniform(-2,2))

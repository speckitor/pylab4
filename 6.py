import time

def squares_loop(lst):
    res = []
    for x in lst:
        if x % 2 == 0:
            res.append(x*x)
    return res

def squares_comp(src):
    return [x * x for x in src if x % 2 == 0]

def timeit(square_fn, lst):
    times = []
    for _ in range(7):
        t0 = time.time()
        r = square_fn(lst)
        t1 = time.time()
        times.append(t1 - t0)
    print(f"{square_fn.__name__}:")
    print(f"{times}")
    print(f"avg: {sum(times) / 7}")

lst = list(range(10_000))
print(f"{len(lst)}:")
timeit(squares_loop, lst)
timeit(squares_comp, lst)

print()

lst = list(range(100_000))
print(f"{len(lst)}:")
timeit(squares_loop, lst)
timeit(squares_comp, lst)

print()

lst = list(range(1_000_000))
print(f"{len(lst)}:")
timeit(squares_loop, lst)
timeit(squares_comp, lst)

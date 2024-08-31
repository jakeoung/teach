import marimo

__generated_with = "0.7.14"
app = marimo.App()


@app.cell
def __():
    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    return fib,


@app.cell
def __(fib):
    import timeit

    print(timeit.timeit('fib(30)', globals={'fib': lambda n: (0 if n == 0 else 1 if n == 1 else fib(n-1) + fib(n-2))}))
    print(timeit.timeit('fib(31)', globals={'fib': lambda n: (0 if n == 0 else 1 if n == 1 else fib(n-1) + fib(n-2))}))
    print(timeit.timeit('fib(32)', globals={'fib': lambda n: (0 if n == 0 else 1 if n == 1 else fib(n-1) + fib(n-2))}))

    return timeit,


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()

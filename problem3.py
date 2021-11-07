
def my_func(c):
    if c % 2:
        print(c)
    if c > 995:
        pass
    my_func(c + 1)
my_func(1)
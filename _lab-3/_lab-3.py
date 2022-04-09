def cycle_for(i, i_max, foo):
    if i==i_max:
        return
    else:
        foo()
        cycle_for(i+1, i_max, foo)

def my_func():
    print("I'm doing something strange")

cycle_for(0, 10, my_func)

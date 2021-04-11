my_list = []

def with_cycles():
    for i in range(1, 101):
        if i % 3 != 0:
            my_list.append(i**2)
    print(my_list)

def list_comprenhension():
    my_list = [i**2 for i in range(1,101) if i % 3]
    print(my_list)

if __name__ == '__main__':
    list_comprenhension()

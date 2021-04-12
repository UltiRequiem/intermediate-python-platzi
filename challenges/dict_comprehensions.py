from math import sqrt

def dict_comprenhension():
    my_dict = {i: sqrt(i) for i in range(1,1001)}
    print(my_dict)

if __name__ == '__main__':
    dict_comprenhension()

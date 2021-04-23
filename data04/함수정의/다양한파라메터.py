def list_p(x):
    for index in range(len(x)):#len쓰면 index
        print(index, x[index])
def set_p(x):
    for data in x:  # len쓰면 index
        print(data)
def dic_p(x):

    for key in x:
        val = x[key]
        print(key, ':', val)


def tuple_p(x):
    for data in x:
        print(data)
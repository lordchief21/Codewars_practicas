s = "Hola"
def make_upper_case(s):
    # Code here
    a = "".join([l.capitalize() for l in s])
    print(a)

make_upper_case(s)
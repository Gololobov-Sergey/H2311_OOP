# print("file open")
# try:
#     a = int(input("a = "))
#     b = int(input("b = "))
#     print("Work with file")
#     c = a / b
#     print(c)
# except Exception as ex:
#     print(ex)
# finally:
#     print("File close")


def checker(var):
    if type(var) != str:
        raise TypeError(f"Type {var} not string")
    else:
        return var

v = "10"
v = checker(v)
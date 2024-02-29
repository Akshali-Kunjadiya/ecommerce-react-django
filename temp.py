def auth(*args):
    def inner(func):
        print(args)
        print("user  ")
        return func
    return inner

@auth("get")
def addpost():
    print("post added")

addpost()
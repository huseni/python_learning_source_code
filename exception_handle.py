
__author__ = 'kathiria'

while True:
    try:
        n = input("Please enter an integer: ")
        if isinstance(n, int):
            break
    except ValueError:
       # print(v.args)
        print("No valid integer! Please try again ...")
print("Great, you successfully enabctered an integer!")
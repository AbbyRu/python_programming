print(1<1)
print(1<=1)
print(1>1)
print(1>=1)
print(1!=1)
print(1==1)

name = input("What is your name? ")
if name == "Ruon":
    print("Hello,nice to see you {}".format(name))
elif name == "Bob":
    print("Hello, you are a nice person.")
elif name == "Clara":
    print("Hello {}, have a good day.".format(name))
else:
    print("Have a nice day.")

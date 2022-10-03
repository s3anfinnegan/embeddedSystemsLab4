guestlist= ["Tom", "Dick", "Harry", "Sean"]
name = input("Please enter guest name: ")


if name in guestlist:
	print("Welcome to the party " + name + "!")
else:
	print("Sorry," + name + ", you're not invited")


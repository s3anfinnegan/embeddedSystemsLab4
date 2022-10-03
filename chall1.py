print("Please choose a watersport...")
print("Swimming")
print("Kayaking")
print("Surfing")
print("Sailing")

while True:
    choice = input("Which watersport are you choosing?: ")
    if choice == "Swimming":
    	print("The water is freezing, you're a hardy yoke!")
    elif choice == "Kayaking":
        print("Onto the rapids ya good thing!")
    elif choice == "Surfing":
        print("Its an offshore wind, grab your suit we're going!")
    elif choice == "Sailing":
        print("Don't forget your life jacket!")
    else:
        break

mainmenu()

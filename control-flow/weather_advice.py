# prompt the user for weather input
weather = input("What's the weather like today? (sunny, rainny, cold): ")

# provide the clothing recommendation

if weather == "sunny":
    print("Wear a T-shirt  and sunglasses.")
elif weather == "rainny":
    print("Don't forget the Umbrella and Raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")

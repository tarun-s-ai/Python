print(" Welcome to the Secret Code Name Generator!")

# Ask for user inputs
name = input("Enter your first name: ").strip().capitalize()
fav_thing = input("What's one thing you really like? ").strip().lower()

# Generate the code name
part1 = name[:2] + fav_thing[-2:]
part2 = fav_thing[:3][::-1] + name[-1].upper()

code_name = part1 + "_" + part2

print("\n🎉 Your Secret Code Name is:", code_name)
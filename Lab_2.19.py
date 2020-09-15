# Andrew Li
# 1824794

# PART 1
lemon_cups = float(input("Enter amount of lemon juice (in cups):\n"))
water_cups = float(input("Enter amount of water (in cups):\n"))
agave_cups = float(input("Enter amount of agave nectar (in cups):\n"))
num_servings = float(input("How many servings does this make?\n"))
print("")
print("Lemonade ingredients - yields {:.2f} servings".format(num_servings))
print("{:.2f} cup(s) lemon juice".format(lemon_cups))
print("{:.2f} cup(s) water".format(water_cups))
print("{:.2f} cup(s) agave nectar\n".format(agave_cups))

# PART 2
desired_servings = float(input("How many servings would you like to make?\n"))
servings_factor = desired_servings/num_servings  # every cup measurement will be multiplied by this factor

lemon_cups = lemon_cups*servings_factor  # scales up servings by factor determined before
water_cups = water_cups*servings_factor
agave_cups = agave_cups*servings_factor
# print(lemon_cups, water_cups, agave_cups)  # debugging purposes

print("Lemonade ingredients - yields {:.2f} servings".format(desired_servings))
print("{:.2f} cup(s) lemon juice".format(lemon_cups))
print("{:.2f} cup(s) water".format(water_cups))
print("{:.2f} cup(s) agave nectar\n".format(agave_cups))




# Andrew Li
# 1824794
import math

# PART 1
# Prompt user to enter height and width
height = int(input("Enter wall height (feet):\n"))
width = int(input("Enter wall width (feet):\n"))
# calculate area
area = int(height*width)
print("Wall area: {} square feet".format(area))

# PART 2
# Calculate gallons needed to paint wall
gallons_paint = area/350  # one gallon of paint covers 350 sq ft
print("Paint needed: {:.2f} gallons".format(gallons_paint))

# PART 3
# Calculate # of 1 gallon paint cans needed
num_paint_cans = math.ceil(gallons_paint)
print("Cans needed: {} can(s)\n".format(num_paint_cans))

# PART 4
# Assign costs to color paints and calculate total
colors = {
    "red": 35,
    "blue": 25,
    "green": 23
}
chosen_color = input("Choose a color to paint the wall:\n")
price = colors[chosen_color]
total = price*num_paint_cans
print("Cost of purchasing {} paint: ${}".format(chosen_color, total))


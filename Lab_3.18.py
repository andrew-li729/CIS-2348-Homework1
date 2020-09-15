# Andrew Li
# 1824794

# PART 1
# Prompt user to enter height and width
height = int(input("Enter wall height (feet):\n"))
width = int(input("Enter wall width (feet):\n"))
# calculate area
area = int(height*width)
print("Wall area: {} square feet\n".format(area))

# PART 2
# Calculate gallons needed to paint wall
gallons_paint = area/350  # one gallon of paint covers 350 sq ft
print("Paint needed: {:.2f} gallons".format(gallons_paint))

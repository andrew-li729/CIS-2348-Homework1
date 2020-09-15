# Andrew Li
# 1824794

# PART 1
# Services menu
services = {
    "Oil change": 35,
    "Tire rotation": 19,
    "Car wash": 7,
    "Car wax": 12,
    "-": 0
}
print("Davy's auto shop services")
print("Oil change -- ${}".format(services["Oil change"]))
print("Tire rotation -- ${}".format(services["Tire rotation"]))
print("Car wash -- ${}".format(services["Car wash"]))
print("Car wax -- ${}\n".format(services["Car wax"]))

# PART 2
# Prompt user for two services
# will store choices in own variables to index dictionary
service1 = input("Select first service:\n")
service2 = input("Select second service:\n")


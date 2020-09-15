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
print("")

# PART 3
# calculate total cost of services
service1_cost = services[service1]  # fetches costs from dict
service2_cost = services[service2]
total = service1_cost + service2_cost

# PART 4
# Extends program to allow user to select no service
print("Davy's auto shop invoice\n")

if service1 == "-":  # do not need to access dict if no service is chosen
    print("Service 1: No service")
else:
    print("Service 1: {}, ${}".format(service1, services[service1]))

if service2 == "-":
    print("Service 2: No service\n")
else:
    print("Service 2: {}, ${}\n".format(service2, services[service2]))

print("Total: ${}".format(total))

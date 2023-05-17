# Create a  Car  object "my_car" with the given data attributes:
my_car = Car(make,model,color)

# Use the method car_info() to print out the data attributes.
my_car.car_info()

# Call the method  sell()  in the loop, then call the method  car_info() again
for i in range(5):
    my_car.sell()

my_car.car_info()

# -*- coding: utf-8 -*-
#cars = 100
#space_in_a_car = 4.0
#drivers = 30
#passengers = 90
#cars_not_driven = cars - drivers
#cars_driven = drivers
#carpool_capacity = cars_driven * space_in_a_car
#average_passengers_per_car = passengers / cars_driven


#print "There are", cars, "cars available."
#print "There are only", drivers, "drivers available."
#print "There will be", cars_not_driven, "empty cars today."
#print "We can transport", carpool_capacity, "people today."
#print "We have", passengers, "to carpool today."
#print "We need to put about", average_passengers_per_car, "in each car."
# 我把每辆车换成只有2个空间，就是第三行4.0改成2，运行还是一样的。
cars = 100
space_in_a_car = 5.0
drivers = 20
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers avaiable.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")

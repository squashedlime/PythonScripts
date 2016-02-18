#this defines the function and how many variables it has
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d Cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print " Get a blanket...\n"
#this parses it's value to the function in the parenthesis
print "we can just give the functions numbers directly:"
cheese_and_crackers(20, 30)
#this sets the variables first then they are put into the funtion..
print "Or, we can use varibales from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
# here...
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#math is done first then the values are passed to the function
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)
#same here!
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, 
amount_of_crackers + 1000)


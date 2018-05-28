Python unit testing exercise.

# Context.

A company rents bikes under following options: 

1. Rental by hour, charging $5 per hour
2. Rental by day, charging $20 a day
3. Rental by week, changing $60 a week
4. Family Rental, is a promotion that can include from 3 to 5 Rentals (of any type) with a discount of 30% of the total price

# Solution.

The domain consists of a class that represents the "rent" entity. It has methods for each action that can be performed in the entity. Using chained methods, abstraction was simplified, making not necessary to create additional entities.

An additional file containing unit testing methods has included.

# Running the example.

Using python 3.6 on the solution directory:

$> python -m unittest discover

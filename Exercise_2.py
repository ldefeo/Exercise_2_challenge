"""Descripción del ejercicio: There is a queue for the self-checkout tills at the supermarket. Your task is to write a function
to calculate the total time required for all the customers to check out!
Input
    customers: an array of positive integers representing the queue. Each integer represents a
        customer, and its value is the amount of time they require to check out.
    n: a positive integer, the number of checkout tills.
Output
    The function should return an integer, the total time required."""

def self_service(customers, n):
    tills = [0] * n # --> I generate a list of tills according to n
    if n == 1:
        return sum(customers) # --> if n=1 then the time required is the sum of all the customers time
    if n >= len(customers):
        return max(customers) # --> if n >= to the number of customers, means that there is a till for each customer, then the time required is going to be the longest time
    else:
        for time in range(len(customers)):
            if time+1 <= len(tills):  # --> if the index of customers is lower than len(tills), i can send a customer to each till 
                tills[time] = customers[time]
            else: # --> if the index is greater, should wait and the next customer must go to the till that is about to finish registering a customer
                till_ending = min(tills)
                tills[tills.index(till_ending)] += customers[time] # --> the time of the customer who was registering at that till and that of the new customer who is about to register is added.
        return max(tills)  # --> I get the max time between all the tills since the time was acumulative and everyone will finish registering when the longest time ends.
            



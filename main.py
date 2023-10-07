

from Exercise_2 import self_service


def main():
    customers_n_tuples = [([10,2,3,3],2),([5,3,4],1),([2,3,10],2)]
    for tuple in range(len(customers_n_tuples)):
        time_request = self_service(customers_n_tuples[tuple][0], customers_n_tuples[tuple][1])
        print("The total time required for the tuple ({},{}) to register is: {}".format(customers_n_tuples[tuple][0],customers_n_tuples[tuple][1],time_request))
        
main()


from Exercise_2 import self_service


def main():
    customers = [10,2,3,3]
    n = 2
    time_request = self_service(customers, n)
    print("The total time required to register is: ",time_request)
main()
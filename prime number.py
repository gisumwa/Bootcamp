import math
def first_n_primes(terms):
    #declaration of an empty list
    prime_list=[2]
    #declaration of a for loop that starts at 3 but may never reach terms squared and skips checking of even numbers from primes and terminates at the square root of num
    # as explained by the primarity test algorithm
    for num in range(3,terms**2,2):
        if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
            #while loop that checks whether the number of elements in the list has reached the one specified
            while len(prime_list)<terms:
                prime_list.append(num)
                break
    return prime_list
print(first_n_primes(5))





def fizz_buzz(n):
    """return fizz when n divisible by 3
       return buzz when n divisible by 5
       rerutn fizzbuzz when n divisible by both 3 and 5
    """
    if n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    elif n % 3 == 0:
        return 'fizz'
    elif n % 5 == 0:
        return 'buzz'

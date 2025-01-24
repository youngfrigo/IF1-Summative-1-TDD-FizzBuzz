def fizzbuzz(n):
    """ Funciton to implement rules of FizzBuzz

    Args:
        n (int): input parameter/number
    """
    res = ''
    if n % 3 == 0:
        res = "Fizz"
    if n % 5 == 0:
        res += "Buzz"
    return(n if not res else res)
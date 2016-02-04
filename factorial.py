def factorial(PositiveInt):
    """
    Computes the factorial of a positive integer
    """
    
    if PositiveInt == int(PositiveInt):
        if PositiveInt > 0:
            Prod = 1
            for n in xrange(int(PositiveInt)):
                Prod *= n+1
            return Prod
        else: 
            raise NotImplementedError("The factorial is only defined for positive integers")
    else: 
            raise NotImplementedError("The factorial is only defined for positive integers")

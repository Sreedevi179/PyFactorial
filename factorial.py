def factorial(positive_int):
    """
    Computes the factorial of a positive integer.
    Integers, integer floats, and integer complex numbers with zero imaginary parts are accepted input.
    """
    
    if type(positive_int) == complex: 
        if positive_int.imag == 0:
            positive_int = positive_int.real
        else:
            raise NotImplementedError("The factorial is only defined for positive integers, not complex values with nonzero imaginary part")
    if type(positive_int) == str:
         raise NotImplementedError("The factorial is only defined for positive integers, not strings")
    #____________________________________
    if positive_int == int(positive_int):
        if positive_int > 0:
            fac_prod = 1
            for n in xrange(int(positive_int)):
                fac_prod *= n+1
            return fac_prod
        else: 
            raise NotImplementedError("The factorial is only defined for positive integers")
    else: 
            raise NotImplementedError("The factorial is only defined for positive integers")

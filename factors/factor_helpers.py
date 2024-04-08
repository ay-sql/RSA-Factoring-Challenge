def basic_factorize(n):
    """ Factorize a given natural number n into two factors using basic trial division. """
    # Handle even numbers first
    if n % 2 == 0:
        return 2, n // 2

    # Check for factors from 3 upwards
    p = 3
    while p * p <= n:
        if n % p == 0:
            return p, n // p
        p += 2

    # If no factors are found, return n and 1
    return n, 1

def advanced_factorize(n):
    """
    Factorize a given natural number n into two factors using more advanced algorithms.
    Placeholder for advanced algorithms like Pollard's Rho, Quadratic Sieve, etc.
    """
    # This is a placeholder for more advanced factorization methods.
    # For demonstration, let's use the basic factorization.
    return basic_factorize(n)

def factorize(n, method='basic'):
    """
    Factorizes the number n using the specified method.
    Available methods: 'basic', 'advanced'
    """
    if method == 'advanced':
        return advanced_factorize(n)
    else:
        return basic_factorize(n)

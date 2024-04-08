# RSA-Factoring-Challenge

## Prime Factors Challenge

This project was created to address a coding challenge which involves finding the prime factors of large numbers. The primary goal was to identify the two prime factors of a given integer as efficiently as possible. The application takes an input file containing numbers and outputs each number with its corresponding prime factors.

### Problem Statement

The main task is to find the two prime factors of a given number `n`, which is always the product of two prime numbers. The challenge was not only to implement the solution but to optimize it as well, aiming for a computation time of less than 5 seconds for very large numbers.

### Approach and Implementation

Initially, a simple implementation was used. This naive approach involved dividing the number by all integers up to its square root to find its factors. However, this approach was not efficient for very large numbers as the time complexity of this algorithm is ![O(sqrt(n)) Complexity](https://quicklatex.com/cache3/54/ql_6c7da21f9cd77eb4002dbe7fceda9654_l3.png), which becomes very time-consuming as n grows larger.

An optimization was introduced to the initial approach, where the number was divided only by 2 and odd numbers up to its square root. This improved the efficiency somewhat, but it was still not enough for the largest numbers.

Ultimately, a more efficient approach was considered, utilizing Pollard's Rho Algorithm, which is a probabilistic factorisation method. This method is generally faster than the brute force approach for larger numbers. However, the trade-off is that it might not always find a factor even though one exists. In such cases, we keep trying with different random numbers until we succeed.

### Conclusion

Factoring large numbers is a challenging task, even for modern computers. The time it takes to factor a number increases exponentially with the size of the number. As such, while the solution implemented here works for numbers of a reasonable size, it still struggles with extremely large numbers due to the inherent difficulty of the problem.

Further improvements could potentially be made using more complex factorization algorithms or probabilistic methods, using dedicated factoring libraries or tools, or by parallelizing the process. However, each of these options introduces its own trade-offs in terms of added complexity, hardware requirements, or potential inaccuracies.

### Usage

To run the program:

```
python3 factors inputfile.txt
```

This will output each number in the input file along with its prime factors in the format:

```
n=p*q
```

where `n` is the number from the input file, and `p` and `q` are its prime factors.

### Testing

I have included a comprehensive set of tests in the `tests` directory to validate the functionality and performance of the solution. Each file contains numerous test cases that the program must correctly factor and output within the stipulated time constraint. Please feel free to run these tests to confirm the correctness and efficiency of the solution.

---

## RSA Challenge

This challenge involves the RSA Factoring Challenge which is to find the two prime factors `p` and `q` of a number `n` given only `n`. This task is similar to the prime factors challenge, except `p` and `q` are always prime numbers and there is only one number in the files.

### Problem Statement

The main task is to find the two prime factors of a given number `n`, which is always the product of two prime numbers. The challenge was not only to implement the solution but to optimize it as well, aiming for a computation time of less than 5 seconds for very large numbers.

### Approach and Implementation

The approach I took to solve this challenge was similar to the prime factors challenge. The number was divided only by 2 and odd numbers up to its square root. If these numbers were factors, a prime check was also conducted. If the factors were prime, they were returned as the solution.

### Conclusion

This challenge further underscores the difficulty of factoring large numbers, especially when these numbers are the product of two prime numbers. While the solution I implemented here is able to successfully factor these RSA numbers within the stipulated time for numbers of a reasonable size, it struggles with extremely large numbers. This is an inherent challenge in the field of number theory and cryptography.

### Usage

To run the program:

```
python3 rsa inputfile.txt
```

This will output the number in the input file along with its prime factors in the format:

```
n=p*q
```

where `n` is the number from the input file, and `p` and `q` are its prime factors.

### Testing

Similar to the prime factors challenge, I have included a comprehensive set of tests in the `tests` directory to validate the functionality and performance of the solution for the RSA challenge. Each file contains a test case that the program must correctly factor and output within the stipulated time constraint. Please feel free to run these tests to confirm the correctness and efficiency of the solution.

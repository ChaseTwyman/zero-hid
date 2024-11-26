def generate_primes():
    primes = []
    num = 2
    while True:
        is_prime = True
        for prime in primes:
            if prime * prime > num:
                break
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            yield num
        num +=1

prime_generator = generate_primes()
for i in prime_generator:
    if i > 1000000: print(i)
    
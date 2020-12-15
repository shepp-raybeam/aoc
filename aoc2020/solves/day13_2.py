from functools import reduce

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(*args):
    """Return lcm of args."""   
    return reduce(lcm, args)

input = '23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,829,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,677,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19'.split(',')
input = '17,x,13,19'.split(',')

terms = [1 if v == 'x' else max(1, (3*int(v)-i)%int(v)) for i, v in enumerate(input)]

prod = reduce(lambda x, y: x*y, terms)
print(prod)

def check(time):
    for i, term in enumerate([1 if v == 'x' else v for v in input]):
        if (time+i)%int(term) != 0:
            return False
    return True


time = prod
while not check(time):
    print(f'checking {time}')
    time += prod


(t + i)%bus[i] == 0

t+i mod n = 0
t+i+1 mod n = 1

t+i mod n = 0 

t mod n = (n - i) mod n 

t = n-i (mod n)

t = kn + (n-i)

t = k17 + 17
t = k13 + 11
t = k19 + 16

t mod 17 = 17 mod 17 = 0
t mod 13 = 11 mod 13 = 11
t mod 19 = 16 mod 19 = 16

t mod 13+19 
25


t*t mod 13*19 = 171?


148809600576 too low

3, 17, 67


t = 17z      (z = 201) 3*67
t = 13x + 11 (x = 262) 2*131
t = 19y + 16 (y = 179) 1*179

13X = t-11
19y = t-16

13x*19y = t^2-27t+176



17z = 13x + 11
17z = 19y + 16

35 = 13x + 11
24 = 13x



13x + 11 = 19y + 16

13x - 19y = 5


print(terms)

t+i mod(prime[i]) = 0

t+i = 0 mod(prime[i])


t = prime[i]-i mod(prime[i])


2*17*67*331 = 754018
67,7,59,61


x mod 17
y mod 13


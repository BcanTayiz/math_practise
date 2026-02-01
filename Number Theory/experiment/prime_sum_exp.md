# Prime Sum -- Dynamic Formula

I have created a formula for prime counting.
It counts the differences and finds the values. The formula is as below

```Python

def prime_sum_fomrula(self):
        x = 0
        for i in range(len(self.prime_nums)):
            arr = self.prime_nums.copy()
            x += arr[i]-arr[i-1]
            x -= x / arr[i]
        return 1- x / self.n
    
```

We could try to optimize the x increase but eventually we can define a system of increase and decrease.

However this is an upper bound and with 5000 value the result is 

<span style="color:coral"> for n 5000 the ratio of primes 0.18 </span>

I have changed the function and add log to two values then the result is 


```Python

primeSum = PrimeSime()
arr = []
error = []
for i in range(10,100000):
    primeSum.define_primes(i)
    y_pred = primeSum.prime_sum_fomrula() *i 
    y_pred = math.log(y_pred) 
    y = primeSum.prime_count()
    y = math.log(y)
    print(y_pred,y)
    arr.append(y_pred)
    error.append(abs(y_pred-y))

primeSum.plot_arr(arr)
primeSum.plot_arr(error)

```

![y_pred arr log value](image.png)
![two log differences error rate converges to 0.3](image-1.png)


## Formula Logic

In the formula 

```Python
def prime_sum_fomrula(self):
        x = 0
        for i in range(len(self.prime_nums)):
            arr = self.prime_nums.copy()
            x += arr[i]-arr[i-1]
            x -= x / arr[i]
        return 1- x / self.n
```

since 2 divides the values and half of them is not prime. When we get 3 prime we learn that 1/3 of the values are not prime and so on. then we calculate the ratio like that which are ***non prime numbers***. Then 1- ratio gives the prime numbers in rough.

```math
x = 0 \\[10px]
\sum_{n=0}^{n=\infty} (x + (p_{n} - p_{n-1})) - \frac{x}{p_{n}} = S \\[10px]

```

These calculation lead us to **non prime numbers**


```math
x = 0 \\[10px]
\sum_{n=0}^{n=\infty} (x + (p_{n} - p_{n-1})) - \frac{x}{p_{n}} = S \\[10px]

1 - S = primes

```

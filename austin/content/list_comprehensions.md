Title: List Comprehensions
Date: 2017-11-06 10:00
Category: Python


###List Comprehensions
![stranger_things_bruteforce_code](https://image.ibb.co/fBroQ6/bob_newby_code.png)

List comprehensions allow a Python programmer to build lists in a natural and clear manner.
Instead of describing the intricacies of list comprehensions, lets look at a few examples.

#####1. Print a list of the powers of two up to the tenth power:
######Here is the output we are hoping to obtain:
```python
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

```

######Standard:
```python
x = []
for power in range(0, 11):
    x.append(2**power)
print(x)
```
######List Comprehension    
```python
x = [2**power for power in range(0, 11)]
print(x)
```

In this case it is easy to see the benefit of list comprehensions.  The list comprehension 

- builds the list more concisely than the for loop  
- is more explicit (once you learn how to read list comprehensions)
- is faster than the for loop (discussion for another time)

Here is how I would read that list comprehension in plain English.

![list_comprehension_0.png](https://image.ibb.co/jD3Dsm/list_comprehension_0.png)

###### 


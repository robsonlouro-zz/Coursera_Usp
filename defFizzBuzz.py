def fizzbuzz(num):

    res3 = num % 3
    res5 = num % 5
    if res3 == 0 and res5 == 0:
        return "FizzBuzz"
    elif res3 == 0 and res5 != 0:
        return "Fizz"
    elif res3 != 0 and res5 == 0:
        return "Buzz"
    else:
        return num

print(fizzbuzz(5))
print(fizzbuzz(3))
print(fizzbuzz(15))
print(fizzbuzz(23))
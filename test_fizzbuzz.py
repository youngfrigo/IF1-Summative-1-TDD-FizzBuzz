import pytest
from fizzbuzz import *

# if divisible by 3 = fizz - DONE
# if divisible by 5 = buzz - DONE
# if divisible by 3 and 5 = fizzbuzz - DONE
# if not divisible by 3 or 5 return number

def test_fizz():
    assert fizzbuzz(3) == "Fizz"
    
def test_buzz():
    assert fizzbuzz(5) == "Buzz"
    
def test_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"

def test_return_number():
    assert fizzbuzz(1) == 1
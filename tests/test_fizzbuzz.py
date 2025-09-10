from fizzbuzz import fizzbuzz

def test_fizzbuzz_1_to_100():
    """Test fizzbuzz for numbers 1-100"""
    expected_results = [
        1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz",
        11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz",
        "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz",
        31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz",
        41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz",
        "Fizz", 52, 53, "Fizz", "Buzz", 56, "Fizz", 58, 59, "FizzBuzz",
        61, 62, "Fizz", 64, "Buzz", "Fizz", 67, 68, "Fizz", "Buzz",
        71, "Fizz", 73, 74, "FizzBuzz", 76, 77, "Fizz", 79, "Buzz",
        "Fizz", 82, 83, "Fizz", "Buzz", 86, "Fizz", 88, 89, "FizzBuzz",
        91, 92, "Fizz", 94, "Buzz", "Fizz", 97, 98, "Fizz", "Buzz"
    ]
    
    for i in range(1, 101):
        assert fizzbuzz(i) == expected_results[i-1], f"Failed for {i}: expected {expected_results[i-1]}, got {fizzbuzz(i)}"

def test_fizzbuzz_specific_cases():
    """Test specific fizzbuzz cases"""
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"
    assert fizzbuzz(45) == "FizzBuzz"
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2
    assert fizzbuzz(4) == 4

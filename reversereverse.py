def reverse_reverse(numbers):
    if not numbers:
        return []
    else:
        return numbers[-1:] + reverse_reverse(numbers[:-1])

#my print statement calls the reverse_reverse function with a set of numbers to use
print(reverse_reverse([1,2,3,4,5,6,7,8,9,10]))
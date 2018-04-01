#my recursion function that looks through an arry of numbers for the maximum and minimum number
def min_max(numbers):
    if isinstance(numbers, list):
        allnumbers = [min_max(eachnumber) for eachnumber in numbers]
        return min([m[0] for m in allnumbers]), max([m[1] for m in allnumbers])
    else:
        return numbers, numbers



numbers = [-80,-50,-56, 31, -120, 25, -92, 18, 2, -91, -58, -97, -56, -44, 55, -48, -15, -34, -127, 44, 10, -20, 12, 22, 46, -42, 68, -42, 81, 97]

print("The min and max are: ", min_max(numbers))
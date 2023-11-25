def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive call
    return fibonacci(n - 1) + fibonacci(n - 2)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def compareTo(s1, s2):
    if len(s1) < len(s2):
        return -1
    elif len(s1) > len(s2):
        return 1
    else:
        for i in range(len(s1)):
            if s1[i] < s2[i]:
                return -1
            elif s1[i] > s2[i]:
                return 1
        return 0

def main():
    """The function that runs when the program is executed."""

    print("The 15th element of the fibonacci sequence is {}.".format(fibonacci(15)))
    print("The greatest common divisor of 32 and 96 is {}.".format(gcd(32, 96)))
    print("The result of the string comparison str1 and str2 is {}.".format(compareTo("Testing str1", "Testing str2")))


if __name__ == '__main__':
    main()
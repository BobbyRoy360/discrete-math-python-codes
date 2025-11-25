def aliquot_sum(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total = total + i
    return total

if __name__ == "__main__":
    number = 12
    result = aliquot_sum(number)
    print(f"The aliquot sum of {number} is {result}")

    number = 10
    result = aliquot_sum(number)
    print(f"The aliquot sum of {number} is {result}")
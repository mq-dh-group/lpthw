def sex_machine(num, incr):
    i = 0
    numbers = []
    for i in range(0, num, incr):
        print(f"At the top i is {i}")
        numbers.append(i)

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i} \n")

    return numbers

gday = sex_machine(50, 6)

print(f"The numbers: {gday}")

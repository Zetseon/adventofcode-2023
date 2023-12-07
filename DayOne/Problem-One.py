def numbersOnly(string):
    l, r = 0, len(string) - 1

    while string[l].isdigit() != True:
        l += 1
    while string[r].isdigit() != True:
        r -= 1
    print(string, string[l], string[r])
    return int(string[l] + string[r])


def main():
    text = open("InputOne.txt", "r")
    output = 0
    for line in text:
        output += numbersOnly(line)

    print(output)


if __name__ == "__main__":
    main()

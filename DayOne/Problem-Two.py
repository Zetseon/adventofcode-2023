def numbersOnly(string):
    l, r = 0, len(string) - 1

    while string[l].isdigit() != True:
        l += 1
    while string[r].isdigit() != True:
        r -= 1
    return int(string[l] + string[r])


def replaceWords(string):
    num_map = {
        "zero": "z0o",
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }

    for n in num_map:
        string = string.replace(n, num_map[n])
    return string


def main():
    text = open("InputOne.txt", "r")

    output = 0

    for line in text:
        line = replaceWords(line)
        output += numbersOnly(line)
    print(output)


if __name__ == "__main__":
    main()

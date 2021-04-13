def read():
    numbers = []
    with open("./../txt/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["Eiji", "Iyo", "Rin", "Sena"]
    with open("./../txt/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def main():
    write()


if __name__ == "__main__":
    main()

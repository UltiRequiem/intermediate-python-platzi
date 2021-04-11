def main():
    my_list = [29, "Giorno", False, 89.6]
    my_dict = {"first_name": "Eliaz", "last_name": "Bobadilla"}

    super_list = [
        {"first_name": "Eliaz", "last_name": "Bobadilla"},
        {"first_name": "Aka", "last_name": "Akasaka"},
        {"first_name": "Sakae", "last_name": "Esuno"},
        {"first_name": "Sebas", "last_name": "Camarena"}
    ]

    super_dict = {
        "natural_numbers": [1, 2, 3, 4, 5],
        "integer_numbers": [-1, -3, 0],
        "floating_numbers": [1.5, 5.6, 5.9, 11.5]
    }

    for key, value in super_dict.items():
        print(key,"-",value)

    for item in super_list:
        print(item["first_name"], item["last_name"])

if __name__ == '__main__':
    main()

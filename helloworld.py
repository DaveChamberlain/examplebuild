DEFAULT_GREETING = "Good morning"


def get_greeting(name):
    return "{} {}".format(DEFAULT_GREETING, name)


def main():
    name = input("Enter your name: ")
    print(get_greeting(name))


if __name__ == "__main__":
    main()
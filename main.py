from functions import data_reader


def main():
    # Open the data file
    file = open("data/data.txt", "r", encoding="utf-8")
    read_validation = data_reader(file)


if __name__ == "__main__":
    main()

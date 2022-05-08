from rich import print


def main():
    new_number = float(input("Enter New Number: "))
    original_number = float(input("Enter Original Number: "))
    print (calculation(new_number, original_number))

def calculation(new_number, original_number):
    increase = new_number - original_number
    percent_increase = increase / original_number * 100
    return percent_increase

if __name__ == "__main__":
    main()
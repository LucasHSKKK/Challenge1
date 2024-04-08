# list with the numbers
list_of_numbers = [
    2,
    7,
    34,
    62,
    1,
    50,
    27,
]

# options of sorting
sort = ["asc", "desc", "none"]


# def that print out the order depeding your input
def test(list, ordem):
    if ordem in sort:
        if ordem == "asc":
            print(f"this is your numbers list:")
            print(sorted(list_of_numbers))
        elif ordem == "desc":
            print(f"this is your numbers list:")
            print(sorted(list_of_numbers, reverse=True))
        else:
            print(f"this is your numbers list:")
            print(list_of_numbers)


# message with the options
print(f"these options are available {sort}")
# requesting the input
ordering = input("Select how would you like to order the list: ")

# runnning the def
test(list_of_numbers, ordering)

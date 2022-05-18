def case_insensitive(to_upper):
    str(to_upper).upper()


def product_in_list(shopping_list, product):  # 3 in menu
    if product in shopping_list:
        print("Product in the list")
    else:
        print("Product NOT in the list")


def illegal_products(shopping_list):  # 8 in menu
    illegal = False
    for i in shopping_list:
        if len(i) < 3:
            illegal = True
        for j in i:
            if not j.isalpha():
                illegal = True
        if illegal:
            print(i)
        illegal = False


def order_list(temp_list):
    for i in range(len(temp_list) - 1):
        for j in range(i + 1, len(temp_list)):
            first = temp_list[i]
            second = temp_list[j]

            if int(first[-1]) < int(second[-1]):
                temp = temp_list[i]
                temp_list[i] = temp_list[j]
                temp_list[j] = temp
    return temp_list


def view_popular(shopping_list):  # 12 in menu
    temp_list = []
    string = ""

    for i in shopping_list:
        string += (str(i) + ": " + str(shopping_list[i]))
        temp_list.append(string)
        string = ""

    order_list(temp_list)

    for i in temp_list:
        print(i)


def view_best_popular(shopping_list):
    temp_list = []
    string = ""

    for i in shopping_list:
        string += (str(i) + ": " + str(shopping_list[i]))
        temp_list.append(string)
        string = ""

    order_list(temp_list)

    for i in range(3):
        print(temp_list[i])


def total_sum(shopping_list):
    count = 0
    for i in shopping_list:
        count += shopping_list[i]
    return count


def add_product(shopping_list, product):
    count = 1
    if product in shopping_list:
        count = int(shopping_list[product]) + 1
    shopping_list[product] = count


def remove_product(shopping_list, product):
    if product not in shopping_list:
        print("Product not find")
    else:
        shopping_list[product] -= 1
    if shopping_list[product] == 0:
        del shopping_list[product]


def total_del(shopping_list, product):
    if product in shopping_list:
        del shopping_list[product]
    else:
        print("product not find")


def search_product(shopping_list, product):
    if product[0] == '*':
        if product[-1] == '*':
            for i in shopping_list:
                if product[1:-1] in i:
                    print(i)
        else:
            length = len(product)
            for i in shopping_list:
                for j in range(1, length):
                    if i[j - 1] == product[j]:
                        print(i)

    elif product[-1] == '*':
        length = len(product)
        for i in shopping_list:
            for j in range(-1, length):
                if i[j + 1] == product[j]:
                    print(i)


def save_file(shopping_list):
    pass


def save_csv(shopping_list):
    pass


def print_menu(menu):  # print the main menu
    count = 1
    print()
    for i in menu:
        print(str(count) + ": " + i)
        count += 1
    print()


def second_menu(shopping_list):
    if shopping_list == {}:
        while True:
            user_input = str(input("Please enter product (-1) to stop:"))
            if user_input == '-1':
                break
            add_product(shopping_list, user_input)

    menu = ["View the product list", "How many products are on the cart?", "Is the product on the list?",
            "How many times does a particular product appear?", "Delete a product from the list",
            "Add a product to the list", "Print all illegal products", "Total delete product",
            "View popular", "3 most popular", "search product", "save", "save-csv", "Logout"]

    while True:
        print_menu(menu)
        while True:  # check user input decimal number
            user_input = input()
            if not user_input.isdecimal():
                print("Please enter just numbers (1-9): ")
            else:
                break
        user_input = int(user_input)
        if user_input == 1:
            print(shopping_list)
        elif user_input == 2:
            print(total_sum(shopping_list))
        elif user_input == 3:
            product_in_list(shopping_list, input("enter the product you want to find: ").lower())
        elif user_input == 4:
            print(shopping_list[input("enter product: ").lower()])
        elif user_input == 5:
            remove_product(shopping_list, input("enter the product you want to remove: ").lower())
        elif user_input == 6:
            add_product(shopping_list, input("enter the product you want to add: ").lower())
        elif user_input == 7:
            illegal_products(shopping_list)
        elif user_input == 8:
            total_del(shopping_list, input("enter the product you want to remove: ").lower())
        elif user_input == 9:
            view_popular(shopping_list)
        elif user_input == 10:
            view_best_popular(shopping_list)
        elif user_input == 11:
            search_product(shopping_list, input("enter the product you want to search: ").lower())
        elif user_input == 12:
            save_file(shopping_list)
        elif user_input == 13:
            save_csv(shopping_list)
        elif user_input == 14:
            print("You have successfully logged out")
            return shopping_list
        else:
            print("wrong input, try again\n")


def first_menu():
    menu = ["Login", "Exit"]
    users = {}
    while True:
        print_menu(menu)
        user_input = int(input("Please enter just numbers (1-2):"))
        if user_input == 1:
            username_input = input("Please enter your username: ")
            if username_input not in users:
                users[username_input] = second_menu({})
            else:
                users[username_input] = second_menu(users[username_input])
        elif user_input == 2:
            break
        else:
            print("wrong input, try again\n")


def main():
    first_menu()


main()

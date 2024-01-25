def run():
    print("\nTask_02\n")

    user_input = input("Enter a number: ")

    user_list = [int(i.strip()) for i in user_input.split(",")]

    odds = [i for i in user_list if i % 2 != 0]
    evens = [i for i in user_list if i % 2 == 0]

    print(f"sums :{sum(user_list)} \n"
          f"len evens :{len(evens)}\n"
          f"average :{sum(user_list) / len(user_list)}\n"
          f"sorted evens :{sorted(evens)}\n"
          f"sorter odds :{sorted(odds)}")

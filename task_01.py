def run():
    print("Task_01\n")

    user_input = input("Enter a number: ")

    user_int_list = [int(i.strip()) for i in user_input.split(",")]
    user_zero_list = [i for i in user_int_list if i == 0]
    user_twos_list = [abs(i) for i in user_int_list if i == -2 or i == 2]
    user_negative_num = [i for i in user_int_list if i < 0]
    user_positive_num = [i for i in user_int_list if i >= 0]

    print(f"len tows : {len(user_twos_list)}\n"
          f"max int : {max(user_int_list)}\n"
          f"min int : {min(user_int_list)}\n"
          f"sorted ASC : {sorted(user_int_list)}\n"
          f"len negative numbers list : {len(user_negative_num)}\n"
          f"len positive numbers list : {len(user_positive_num)}\n"
          f"len zeros list : {len(user_zero_list)}")

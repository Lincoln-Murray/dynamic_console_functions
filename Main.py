
def user_input(_option_list:list, _input_text:str = "What would you like to do? ") -> int:
    valid = False
    print(option_list)
    while not valid:
        user_input = input()
        if user_input in _option_list:
            option = _option_list.index(user_input)
            valid = True
            return option
        else:
            try:
                user_input = int(user_input)
                if user_input < len(option_list) and user_input > len(option_list):
                    valid = True
                    return user_input
                else:
                    raise TypeError
            except:
                valid = False
                print('Invalid selection, please try again.')

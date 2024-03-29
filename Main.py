
def user_input(_option_list:list, _input_text:str = "What would you like to do? ") -> int:
    valid = False
    while not valid:
        user_input = input(_input_text)
        if user_input in _option_list:
            option = _option_list.index(user_input)
            valid = True
            return option
        else:
            try:
                user_input = int(user_input)-1
                if user_input <= len(_option_list)-1 and user_input >= 0:
                    valid = True
                    return user_input
                else:
                    raise TypeError
            except:
                valid = False
                print('Invalid selection, please try again.')
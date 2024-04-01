
#The function for user input, you send through the list of options that can be selected and then the query string and it returns the index in the option list.
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

def print_table(_table):
    print('_'*71)
    for item in _table:
        print('|' + str(_table[0]) + ' ' * (40-len(str(_table[0]))) + '| ' + str(_table[1]) + ' ' * (7-len(str(_table[1]))) + '| ' + str(_table[2])  + ' ' * (7-len(str(_table[2]))) + '| ' + str(_table[3]) + ' ' * (7-len(str(_table[3]))) + '|')
        
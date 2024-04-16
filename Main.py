
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

def number_input(_type:type = int):
    valid = False
    while not valid:
        user_input = input(' ')

def print_table(_table:list, left_buffer:int = 1, right_buffer:int = 0, has_labels:bool = False) -> None:
    for i in range(0,len(_table[0])):
        locals()[i] = 0
    for row in _table:
        item_num = 0
        for item in row:
            if locals()[item_num] < len(str(item)):
                locals()[item_num] = len(str(item))
            item_num += 1
    header_string = ' '
    for i in range(0,len(_table[0])):
        header_string = header_string + '_' * (locals()[i]+left_buffer+right_buffer+1)
    header_string = header_string[:-1]
    print(header_string)
    label_string = '|'
    for colum_num in range(0, len(_table[0])):
            label_string = label_string + '‾' * (locals()[colum_num]+left_buffer+right_buffer) + '|'
    first_row = True
    for row in _table:
        row_string = '|' + ' ' *left_buffer
        item_num = 0
        for item in row:
            row_string = row_string + str(item) + ' ' * (locals()[item_num]-len(str(item))) + ' ' * right_buffer + '|'  + ' ' * left_buffer
            item_num += 1
        print(row_string)
        if has_labels and first_row:
            print(label_string)
        first_row = False
    footer_string = header_string.replace('_', '‾')
    print(footer_string)
        
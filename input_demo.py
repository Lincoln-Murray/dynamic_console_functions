import Main

print('Choosing from a table: ')
ol = ['a', 'b', 'c']
print(ol[Main.user_input(ol)])

print('\n choosing a number in a range: ')
print(Main.number_input(float, '??', 0.5, 10))
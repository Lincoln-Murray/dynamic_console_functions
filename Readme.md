# Dynamic Console Functions

## Table of Contents

+ [About](#about)
+ [Getting Started](#getting_started)
+ [Usage](#usage)

## <a name = "about">About </a>

 a project I decided to start in order to compile all the frequently used functions I use when working on small terminal based projects

 Happy Coding!

## <a name = "getting_started">Getting Started </a>

To get this library running download the Main.py file and put it into your projects folder, then you need to just import it like you would any other Python3 library(by whatever the filename is). That's it, then you can call the functions  

## <a name = "usage">Usage </a>

### Initiating the library:

To initiate the library:

```
Import Main  
```

Then use the functions(in this case validating user input):

```
choices = ['a', 'b', 'c']
text = 'Test text: '
validated_input = Main.user_input(choices, text)
```  

Printing tables:  
```
table = [['Numbers', 'Also numbers'],[01,02],[03,04]]
has_headers = True
left_side_buffer = 1
right_side_buffer = 1
print_table(table, left_side_buffer, right_side_buffer, has_headers)
```  

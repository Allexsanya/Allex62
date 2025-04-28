from itertools import chain

from main import some_string

some_string = "0m\n5    my name is alex TTTTTTTTT 1122    name "

upper = some_string.upper()  # ' MY NAME IS ALEX 11'
lower = some_string.lower()  # 'my name is alex ttttttttt 11'
title = some_string.title()  # 'my name is alex ttttttttt 11'
capitalized = some_string.capitalize()  # 'my name is alex ttttttttt 11'
chain = some_string.lower().upper().capitalize()  #

clear_string_spaces = some_string.strip()  #
clear_string_symbols = some_string.strip(" 54naMe")
clear_string_symbols_left = some_string.lstrip(" 54naMe")
clear_string_symbols_reft = some_string.rstrip(" 54naMe")
change_inner_text = (
    some_string.replace("name", "surname", 1).replace("alex", "Alex").replace("1", "2")
)

table = str.maketrans("12", "21", "\n")
result_smart = some_string.translate(table)

slices1 = some_string[:]
slices2 = some_string[0:10]
slices3 = some_string[12:15]
slices4 = some_string[::2]  # каджій второай символ
slices5 = some_string[::-1]  # рохворот строчки
slices6 = some_string[::-2]
slices7 = some_string[-3:-11:-2]

pass
pass

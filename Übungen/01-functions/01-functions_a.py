def concatenate_strings(str_list):
    result = ''
    for l_str in str_list:
        result += l_str
    return result

str_list = ['Hallo', 'Welt']

concatenated_string = concatenate_strings(str_list)
print(concatenated_string)
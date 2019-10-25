def concatenate_strings(str_list, concatenator=' '):
    result = ''
    for l_str in str_list:
        if result == '':
            result += l_str
        else:
            result += concatenator + l_str
    return result

str_list = ['Hallo', 'Welt']

concatenated_string = concatenate_strings(str_list, 'xxx')
print(concatenated_string)
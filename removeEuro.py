euro = '17€'

def euroTransformer(str):
    returnValue = str.replace('€', '')
    return int(returnValue)

output = euroTransformer(euro)
print(output)
print(type(output))
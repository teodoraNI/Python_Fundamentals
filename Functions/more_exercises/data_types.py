def data_type_operations(type:str, item:str):
    if type == 'int':
        return int(item) * 2
    elif type == 'real':
        return f"{float(item) * 1.5:.2f}"
    elif type == 'string':
        new_string = '$' + item + '$'
        return(new_string)

data_type = input()
item = input()
result = data_type_operations(data_type, item)
print(result)

def format_name(first_name, last_name):
    if first_name == "":
        str1 = print(last_name)
        return str1
    elif last_name == "":
        str2 = print(first_name)
        return str2
    elif first_name == "" and last_name == "":
        str3 = print("")
        return str3
    else:
        str4 = print(last_name,first_name)
        return str4
print(format_name("",""))
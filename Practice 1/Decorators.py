def div(a, b):
    print(a / b)


# nested function
def smart_div(func):
    def modifier(a, b):
        if a < b:
            a, b = b, a
        return func(a, b) #executed

    return modifier #waiing to be executed


div1 = smart_div(div)
div1(2, 6)

#swap string case 
def swap_case(s):
    str =""
    for i in s:
        if i.islower():
            str+=i.upper()
        else:
            str+=i.lower()
    return str

if __name__ == '__main__':
    result = swap_case("Python")
    print(result)
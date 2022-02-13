def fizzbuzz(num):
    str = ""
    if num % 3 == 0:
        str += "fizz"
    if num % 5 == 0:
        str += "buzz"
    if str == "":
        str = num
    return str


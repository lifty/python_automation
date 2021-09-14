import pytest
import mainclass


def testGetLocalNumber():
    number = mainclass.MainClass.getLocalNumber()
    if number == 14:
        (print("The number is", number))
    assert number == 14, "The number is not 14"

def testGetClassNumber():
    number_two = mainclass.MainClass.getClassNumber()
    if number_two > 45:
        (print("The number is > 45, it's", number_two))
    assert number_two > 45, "The number is <= 45"

def testGetClassString():
    string_one = mainclass.MainClass.getClassString()
    subs_one = "Hello"
    subs_two = "hello"
    check = True
    first_check = string_one.find(subs_one)
    second_check = string_one.find(subs_two)
    if first_check != -1 or second_check != -1:
        (print("The string includes hello"))
    elif first_check == -1 and second_check == -1:
        check = False
    assert check == True, "The string doesn't include 'Hello' at all or in appropriate register"

if __name__ == '__main__':
    pytest.main()
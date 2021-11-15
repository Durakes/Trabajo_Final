import os

def Route():
    my_path = os.getcwd()
    if "\main" in my_path:
        my_path = my_path[:-5]
    else:
        my_path = my_path
    return my_path

def GetRegistersFile():
    my_path = Route()
    
    file = open(my_path + r"\main\fakedb\registers.txt", "r", encoding="UTF-8")
    registers_ = file.readlines()
    file.close()
    
    for i in range (len(registers_)):
        registers_[i]=registers_[i].split(",")
    
    return registers_

def GetPaymentsFile():
    my_path = Route()
    
    file = open(my_path + r"\main\fakedb\payments.txt", "r", encoding="UTF-8")
    payments_ = file.readlines()
    file.close()
    
    for i in range (len(payments_)):
        payments_[i] = payments_[i].split(",")

    return payments_

def GetLimitFile():
    my_path = Route()

    file = open(my_path + r"\main\fakedb\limits.txt", "r", encoding="UTF-8")
    limits_ = file.readlines()

    file.close()

    return limits_
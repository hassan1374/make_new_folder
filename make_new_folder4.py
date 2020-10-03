import os


def address_maker(location):
    mylist = []
    for char in location:
        if char == "\\":
            mylist.append("/")
        else:
            mylist.append(char)
    loction_new = "".join(mylist)
    return loction_new


def name_maker(name):
    mylist = []
    for item in name:
        if item == "/" or item == ":" or item == '\\' or item == "*" or item == "?" or item == '"' or item == "<" or item == ">" or item == "|":
            mylist.append(" ")
        else:
            mylist.append(item)
    new_name = "".join(mylist)
    return new_name


print("for example C:\\Users\seyedi\Desktop\\1")
folder_loction = address_maker(input("where do you want to make folders :"))
how_make_folder = input("how do you want to make folder : (from file (f) or type name (t) :")
if how_make_folder == "t" or how_make_folder == "T":
    count = 1
    while True:
        str_2 = name_maker(input("enter name of folder: "))
        count2 = str(count)
        str_2 = count2 + " " + str_2
        os.mkdir(f"{folder_loction}/{str_2}")
        print(f"\t the {str_2} was made in {folder_loction} successfully")
        print("----------------")
        count = count + 1
else:
    print("for example C:\\Users\seyedi\Desktop\\myfile.txt")
    file_location = address_maker(input("where is your file: "))
    file = open(file_location)
    count = 1
    for i in file.readlines():
        str_2 = i.strip()
        str_2 = name_maker(str_2)
        count2 = str(count)
        str_2 = count2 + " " + str_2
        os.mkdir(f"{folder_loction}/{str_2}")
        print(f"\t the {str_2} was made in {folder_loction} successfully")
        count += 1

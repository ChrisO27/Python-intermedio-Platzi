def run():
    my_list = [1,"Hello",True,4.5]
    my_dict = {"firstname": "Chris", "lastname": "Panana"}

    super_list = [
        {"firstname": "Chris", "lastname": "Panana"},
        {"firstname": "Jose", "lastname": "Dionicio"},
        {"firstname": "Miguel", "lastname": "Peralta"},
        {"firstname": "Fio", "lastname": "Roldan"},
        {"firstname": "Artur", "lastname": "Ascona"}
    ]

    super_dict = {
        "natural_nums" : [1,2,3,4,5],
        "integer_nums" : [-2,-1,0,1,2],
        "floating_nums" : [1.1,2.2,3.3,4.4,5.5]
    }

    #To print the dictionaries considering the keys and values
    for key, value in super_dict.items():
        print(key,":",value)
    #To print the list
    for value in super_list:
        print(value)
    #To print the list and the value of each dictionary separated
    for values in super_list:
        for key, value in values.items():
            print(f'{key} - {value}')
    #Another way
    for i in super_list:
	    print(i.items())
    #
    for i in super_list:
        print(i["firstname"] , "-" , i["lastname"])
    #aaa
    for i in super_list:
        print(i["firstname"], "-", i["lastname"])
        print(i.keys())
        
if __name__ == "__main__":
    run()
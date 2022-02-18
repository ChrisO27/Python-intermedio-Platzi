def run():
    # # creating one dictionary in each iteration
    # for i in range (101):
    #     print({i:i**3})
    # # creating one dictionary to complete with each iterarion
    # my_dict = {}

    # for i in range(101):
    #     my_dict[i] = i**3

    # print(my_dict)
    # # only 3 multiples
    # my_dict2 = {}

    # for i in range(101):
    #     if i % 3 != 0:
    #         my_dict2[i] = i**3

    # print(my_dict2)
    # # dict comprehension
    # dict3 = {i:i**3 for i in range(101) if i % 3 != 0}
    # print(dict3)

    #challenge
    my_dict = {i:round(i**0.5,2) for i in range(1000)}
    print(my_dict)

if __name__ == "__main__":
    run()
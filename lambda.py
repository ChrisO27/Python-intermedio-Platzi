def run():
    # palindrome = lambda string: string == string[::-1]
    # print(palindrome('ana'))
    my_list = [1,2,3,4,5]
    list = [i**2 for  i in my_list]

    print(list)

if __name__ == "__main__":
    run()
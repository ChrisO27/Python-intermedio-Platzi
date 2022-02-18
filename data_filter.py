DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    # filter  we are going to have each dictonary complete
    list_language = list(filter(lambda x:x["language"]=="python",DATA))
    # we do this function to get only the names
    list_language = list(map(lambda worker:worker["name"],list_language))
    for worker in list_language: print(worker)
    print("\n")
    # list comprenhensions
    all_py_devs = [worker["name"] for worker in DATA if worker["language"]=="python"]
    for worker in all_py_devs: print(worker)

    # we are gonna create a new key, that is gonna say True if you are over 70
    # worker | {"old" : worker["age"]>70}  ==> here we are combining to dictonaries the first with the data
    # of the worker, and the second with the new key as a result of the condition
    old_people = list(map(lambda worker: worker | {"old" : worker["age"]>70},DATA))
    for worker in old_people: print(worker)
    print("\n")
    ## with list comprehension
    old_people2 = [worker | {"old" : worker["age"]>70} for worker in DATA]
    for worker in old_people2: print(worker)

if __name__ == "__main__":
    run()
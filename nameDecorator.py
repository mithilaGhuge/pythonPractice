#name format hackerrank decorator question mark

import operator
from operator import itemgetter
def person_lister(f):
    def inner(people):
        # complete the function
        f(people.sort(key=lambda x: x[2]))
    return inner

@person_lister
def name_format(person):
    for i in person:
        print(i)
        for j in i:
            print(("Mr. " if j[3] == "M" else "Ms. ") + j[0] + " " + j[1])

if __name__ == '__main__':
    people = [input().split() for i in range(int(input("print the name")))]
    print(people)
    name_format(people)
    #print(*name_format(people), sep='\n')
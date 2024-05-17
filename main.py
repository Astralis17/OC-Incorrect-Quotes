import random
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
P1, P2, P3, P4, P5, P6 = "", "", "", "", "", ""
pGroup = ["P1", "P2", "P3", "P4", "P5", "P6"]
people= []

count = int(input("How many people: "))

x = 0
while x != (count):
    string = "Character "+ num[x]+ ": "
    person = input(string)
    people.append(person)
    x+=1

print("")
i = count
if i !=0:
    P1 = people[random.randint(0, len(people)-1)]
    people.remove(P1)
    i -= 1

    if i !=0:
        P2 = people[random.randint(0, len(people)-1)]
        people.remove(P2)
        i -= 1

        if i !=0:
            P3 = people[random.randint(0, len(people)-1)]
            people.remove(P3)
            i -= 1

            if i !=0:
                P4 = people[random.randint(0, len(people)-1)]
                people.remove(P4)
                i -= 1

                if i !=0:    
                    P5 = people[random.randint(0, len(people)-1)]
                    people.remove(P5)
                    i -= 1

                    if i !=0:    
                        P6 = people[random.randint(0, len(people)-1)]
                        people.remove(P6)
                        i -= 1
Quotes= [   
            [],
            [[P1,": Why is it so hard for you to believe me?!", "&", P2, ": ...", "&", P1, ": Oh, right. The lying."], [P1,": I couldn't help you even if I wanted to.", "&", P2, ": But you don't want to.", "&", P1, ": No, no I don't."]],
            [],
            [],
            []
        ]

List = Quotes[count-1]
q = List[random.randint(0, len(List)-1)]

x = 0
string = ""

while x < len(q):
    if q[x] == "&":
        print(string)
        string = ""
    else:
        string += q[x]
    x += 1
print(string)
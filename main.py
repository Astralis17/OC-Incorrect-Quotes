import random
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
P1, P2, P3, P4, P5, P6 = "", "", "", "", "", ""
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
        #One Character Quotes
            [],
        #Two Character Quotes
            [[P1, ": Why is it so hard for you to believe me?!", "&", P2, ": ...", "&", P1, ": Oh, right. The lying."],
             [P1, ": I couldn't help you even if I wanted to.", "&", P2, ": But you don't want to.", "&", P1, ": No, no I don't."],
             [P1, ": Bro do you lift?", "&", P2, ": Yeah dude how did you know?", "&", P1, ": Because you lift my heart whenever you're around", "&", P2, ": Bro", "&", P1, ": Bro"],
             [P1, " walks into a dark room:", "&", P1, ": Hmm. Like a good neighbour-", "&", P1, ": ...", "&", P2, ": Statefarm is here"],
             [P1, ": It's too dangerous to go alone, take this!", "&", P2, ": ", P1, " you're just holding out your hand.", "&", P1, ": Yes."]],
        #Three Character Quotes
            [[P1, ": I swear, by the summer's end, thy will have taken thee to at least one party,", P2, "! 'tis my mission for this summer!", "&", P2, ": ...still bitter that they chose ", P3, " for the school play, are we?", "&", P1, ": Shut up- you and I both know that the only reason that, that thing got the lead role of Juliette is because she was blowing the drama teacher"],
             [P1, ": Make no mistake. Not only am I party rocking, but I am also in the house tonight.", "&", P1, ": But are you shuffling?", "&", P2, ": Everyday.", P3, ": What language are you two speaking??"]],
        #Four Character Quotes
            [],
        #Five Character Quotes
            [],
        #Six Character Quotes
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
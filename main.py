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
x = count
if x !=0:
    P1 = people[random.randint(0, len(people)-1)]
    people.remove(P1)
    x -= 1

    if x !=0:
        P2 = people[random.randint(0, len(people)-1)]
        people.remove(P2)
        x -= 1

        if x !=0:
            P3 = people[random.randint(0, len(people)-1)]
            people.remove(P3)
            x -= 1

            if x !=0:
                P4 = people[random.randint(0, len(people)-1)]
                people.remove(P4)
                x -= 1

                if x !=0:    
                    P5 = people[random.randint(0, len(people)-1)]
                    people.remove(P5)
                    x -= 1

                    if x !=0:    
                        P6 = people[random.randint(0, len(people)-1)]
                        people.remove(P6)
                        x -= 1
def autoCapital(P):
    alph = "abcdefghijklmnopqrstuvwxyz"
    ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    out = ""
    x = 0
    for letter in P:
        while x < 26:
            if letter == alph[x]:
                letter = ALPH[x]
                x = 26
            x += 1
        out += letter
    return out

def CAP(P):
    alph = "abcdefghijklmnopqrstuvwxyz"
    ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    PCAP = ""
    for letter in P:
        x = 0
        while x < 26:
            if letter == alph[x]:
                letter = ALPH[x]
                x = 26
            elif letter == ALPH[x]:
                x = 26
            x += 1
        PCAP += letter
    return PCAP

P1 = autoCapital(P1)
P2 = autoCapital(P2)
P3 = autoCapital(P3)
P4 = autoCapital(P4)
P5 = autoCapital(P5)
P6 = autoCapital(P6)

P1CAP = CAP(P1)
P2CAP = CAP(P2)
P3CAP = CAP(P3)
P4CAP = CAP(P4)
P5CAP = CAP(P5)
P6CAP = CAP(P6)

Quotes= [   
            [#One Character Quotes
                
            ],

            [#Two Character Quotes
             [P1, ": Why is it so hard for you to believe me?!", "&", P2, ": ...", "&", P1, ": Oh, right. The lying."],
             [P1, ": I couldn't help you even if I wanted to.", "&", P2, ": But you don't want to.", "&", P1, ": No, no I don't."],
             [P1, " to ", P2, ": You're gonna get yourself killed one day, but I'll be darned if I don't get a chance to watch it happen"],
             [P1, ": Why do you even bother saving my stupid neck?", "&", P2, ": I can't let you get yourself killed. Who'd pay back all the favours you owe me?"],
             [P1, ": Do you think I could leave some money for the people to buy a replacement?", "&", P2, ": You'll be giving somebody money for something, that's for sure."],
             [P1, ": Wetter than a selkie strip club out there!", "&", P2, ": I- I don't know how to respond to that."],
             [P1, ": Gods, you're impatient.", "&", P2, ": Not impatient. Hungry.", "&", P1, ": Hunger just means your body's impatient for food.", "&", P2, ": Bullshit, hunger means... well... uhh.... Hunger means I'm going to drag you out by the ear if you don't come on!", "&", P1, ": You're truly a master of philosophy."],
             [P1, ": I'm not a very 'jump right in' kind of person.", "&", P2, ": Well then show them that trick where you make things burst into flames. Kids'll love that.", "&", P1, ": ...I'll do that. Thank you, ", P2, "."],
             ],
        
            [#Three Character Quotes
             [P1, ": I swear, by the summer's end, thy will have taken thee to at least one party, ", P2, "! 'tis my mission for this summer!", "&", P2, ": ...still bitter that they chose ", P3, " for the school play, are we?", "&", P1, ": Shut up- you and I both know that the only reason that, that thing got the lead role of Juliette is because she was blowing the drama teacher"],
             [P1, ": What's going on?", "&", P2, " chuckling nervously: I don't know what you're talking about. Everything is completely normal and ", P3, " is exactly where they're supposed to be", "&", P1, ": What do you mean? WHERE IS ", P3CAP],
             [P1, ": I get your point. But gods beyond, ", P3, ", has anyone ever told you that you're just really mean?", "&", P2,": At least a few times a day. You learn to translate it out after a while. After that, they make decent sense."],
             [P1, ": Sometimes I hope God is real, but then I see ", P2, " and my hopes are immediately shattered.", "&", P3, ": Hey! You can't just-", "&", P2, ", eating burnt toast: No, no, they're right."],
            ],
        
            [#Four Character Quotes
            
            ],
        
            [#Five Character Quotes
            
            ],
        
            [#Six Character Quotes
                
            ]
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
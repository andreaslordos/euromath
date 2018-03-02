from random import randint

#goal: find which characteristics approximately half of all people have


def test(size):
    return True

def setup():
    char_table={"Alex":["BLACK HAIR","BIG MOUTH","FACIAL HAIR","MOUSTACHE"],
               "Alfred":["HAIR PARTITION","LONG HAIR","GINGER HAIR","BLUE EYES","SAD LOOKING","FACIAL HAIR","MOUSTACHE"],
               "Anita":["HAIR PARTITION","HAIR STUFF","LONG HAIR","BLOND HAIR","RED CHEEKS","BLUE EYES","FEMALE"],
               "Anne":["CURLY HAIR","BLACK HAIR","EAR RINGS","FEMALE"],
               "Bernard":["HAT","HAIR STUFF","BROWN HAIR","BIG NOSE","SAD LOOKING"],
               "Bill":["BALD","GINGER HAIR","RED CHEEKS","FACIAL HAIR","BEARD"],
               "Charles":["HAIR PARTITION","BLOND HAIR","BIG MOUTH","FACIAL HAIR","MOUSTACHE"],
               "Claire":["HAT","HAIR STUFF","GINGER HAIR","GLASSES","FEMALE"],
               "David":["BLOND HAIR","BIG MOUTH","FACIAL HAIR","BEARD"],
               "Eric":["HAT","BLOND HAIR","BIG MOUTH"],
               "Frans":["CURLY HAIR","GINGER HAIR"],
               "George":["HAT","HAIR STUFF","WHITE HAIR","BIG MOUTH","SAD LOOKING"],
               "Herman":["CURLY HAIR","BALD","GINGER HAIR","BIG NOSE"],
               "Joe":["CURLY HAIR","BLOND HAIR","GLASSES"],
               "Maria":["HAT","HAIR STUFF","LONG HAIR","BROWN HAIR","EAR RINGS","FEMALE"],
               "Max":["CURLY HAIR","BROWN HAIR","BIG MOUTH","BIG NOSE","FACIAL HAIR","MOUSTACHE"],
               "Paul":["WHITE HAIR","GLASSES"],
               "Peter":["HAIR PARTITION","WHITE HAIR","BIG MOUTH","BIG NOSE","BLUE EYES"],
               "Philip":["CURLY HAIR","BLACK HAIR","BIG MOUTH","RED CHEEKS","FACIAL HAIR","BEARD"],
               "Richard":["BALD","BROWN HAIR","FACIAL HAIR","MOUSTACHE","BEARD"],
               "Robert":["HAIR PARTITION","BROWN HAIR","BIG MOUTH","BIG NOSE","RED CHEEKS","BLUE EYES","SAD LOOKING"],
               "Sam":["BALD","WHITE HAIR","GLASSES"],
               "Susan":["HAIR PARTITION","LONG HAIR","WHITE HAIR","BIG MOUTH","RED CHEEKS","FEMALE"],
               "Tom":["BALD","BLACK HAIR","BLUE EYES","GLASSES"]}
                        

    names=list(char_table.keys())
    characteristics=[]
    bigList=[]
    for name in names:
        for characteristic in char_table[name]:
            if characteristic not in characteristics:
                characteristics.append(characteristic)
                
    char_ppl={}                
    for characteristic in characteristics:
        char_ppl[characteristic]=[]
        for name in names:
            if characteristic in char_table[name]:
                char_ppl[characteristic].append(name)

    return char_table,names,characteristics,char_ppl

while True:
    print()
    print("Strategy 1: Eliminate 5 people each time, and when it reaches below 6 people eliminate half each time.")
    print("Strategy 2: Eliminate 1 person each time.")
    print("Strategy 3: Eliminate 3 people each time.")
    zx=input("Strategy 1, 2 or 3? ")
    strat1=strat2=strat3=False
    if zx=="1":
        strat1=True
        break
    elif zx=="2":
        strat2=True
        break
    elif zx=="3":
        strat3=True
        break
games_played=0
trials=int(input("Trials: "))
moves=[]
while games_played<trials:
    char_table,names,characteristics,char_ppl=setup()
    games_played+=1
    secret=randint(0,len(names)-1)
    secret=names[secret]
    current_moves=0
    while len(char_table)>1:
        current_moves+=1
        smallest_difference=999
        best_combo=()
        people_list=[]
        breakFlag=False
        if strat1==True:
            objective=5
            if len(char_table)-objective<1:
                objective=int(len(char_table)/2)
        elif strat2==True:
            objective=1
        else:
            objective=int(len(char_table)/2)
        if test(len(char_table))==False:
            break
        if objective!=1:
            for x in range(len(characteristics)):
                if breakFlag==True:
                    break
                for y in range(len(characteristics)-1):
                    people_list=list(set(char_ppl[characteristics[x]]+char_ppl[characteristics[y+1]]))
                    if abs(objective-len(people_list))<smallest_difference:
                        smallest_difference=abs(objective-len(people_list))
                        best_combo=(characteristics[x],characteristics[y+1])
                        if smallest_difference==0:
                            breakFlag=True
                            break
            people_list=list(set(char_ppl[best_combo[0]]+char_ppl[best_combo[1]]))
        else:
            people_list=[names[randint(0,len(names)-1)]]            
        if secret not in people_list:
            for characteristic in characteristics:
                remove_list=[]
                for name in people_list:
                    if name in char_ppl[characteristic]:
                        remove_list.append(name)
                for remove_name in remove_list:
                    char_ppl[characteristic].remove(remove_name)
            for people in people_list:
                del char_table[people]
                names.remove(people)
        else:
            namesToRemove=[]
            for name in names:
                if name not in people_list:
                    del char_table[name]
                    namesToRemove.append(name)
            for element in namesToRemove:
                names.remove(element)
            remove_list=[]
            for thingy in characteristics:
                remove_list=[]
                for name in char_ppl[thingy]:
                    if name not in people_list:
                        remove_list.append(name)
                for remove_name in remove_list:
                    char_ppl[thingy].remove(remove_name)
    moves.append(current_moves)


for x in range(23):
    if moves.count(x+1)!=0:
        print("Winning in",str(x+1),"moves:",str(round(moves.count(x+1)/len(moves)*100,2))+"%")

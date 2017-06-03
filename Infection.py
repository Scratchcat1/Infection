class Person:
    def __init__(self,Name,Infected,Friends,Immune,Vaccinating,Time_Sick,Time_Vac):
        self._Name=Name
        self._Infected=Infected
        self._Friends=Friends
        self._Immune=Immune
        self._Vaccinating= Vaccinating
        self._Time_Sick=Time_Sick
        self._Time_Vac=Time_Vac

import random
Name_list= ["Bob","Jeff","John","Ninja","Ryan","Watson","Hodges","Wendy","Gray","Hemmings","Nash","Hill","Dan","Liam","Theresa","Mimikyu","Peake","Lee","Molly","Chole","Tim"]
Population=[]
Population_Size = int(input("Population size :"))
infection_chance = float(input("Infection Chance :"))
Number = 1
Possible_friends = []


for asdf in range(Population_Size):  #Create Population
    Temp_Friends = []
    if len(Possible_friends)<4 and len(Possible_friends)>1:
        Num_Friends = random.randint(1,len(Possible_friends))
    else:
        Num_Friends = random.randint(1,5)

    if len(Possible_friends)>0:
        for sdfewf in range(Num_Friends):
            friend = random.choice(Possible_friends)
            if friend in Temp_Friends:
                friend = random.choice(Possible_friends)
            Temp_Friends.append(friend)
        
    Name = random.choice(Name_list)+" #"+str(Number)
    Possible_friends.append(Name)
    Population.append(Person(Name,False,Temp_Friends,False,False,0,0))
    Number+=1

for person in Population:
    for persontwo in Population:
        if persontwo._Name in person._Friends and person._Name not in persontwo._Friends:
            randomthing = random.randint(0,100)
            if randomthing > 60:
                persontwo._Friends.append(person._Name)
            else:
                person._Friends.pop(person._Friends.index(persontwo._Name))

total_friends=0
for person in Population:
    total_friends += len(person._Friends)
    #print(person._Name,"  ",person._Infected,"  ",person._Immune,"  ",person._Vaccinating)
    #print(person._Friends)
    #print("")
print(total_friends/(Population_Size))



Infected = random.randint(0,len(Population)-1)
Population[Infected]._Infected = True
day =1
leave = "In"
while leave != "yes":
    
    wait_time= int(input("Auto Days"))
    for x in range(wait_time):
        print("Day ",day)
        day+=1
    
        for person in Population:
            if person._Infected ==True:
                person._Time_Sick +=1
            if person._Vaccinating == True:
                person._Time_Vac +=1

        for person in Population:
            if person._Vaccinating == True and person._Time_Vac > 2 and person._Infected == False:
                person._Immune = True
                person._Vaccinating == False
                person._Time_Vac = 0
                #print(person._Name," is now immune")
            randomthing = random.randint(0,100)
            if randomthing > 96 and person._Immune == True:
                person._Immune = False
                #print(person._Name," has lost immunity")

        
        for person in Population:  # Sick become immune
            if person._Time_Sick >= 6 and person._Infected == True:
                randomthing = random.randint(0,100)
                if randomthing > 80:
                    person._Time_Sick = 0
                    person._Immune = True
                    person._Infected = False
                    #print(person._Name," is now immune")

        for person in Population:
            for persontwo in Population:
                if persontwo._Name in person._Friends and person._Infected==True and persontwo._Infected == False and persontwo._Immune == False:
                    randomthing = random.randint(0,100)
                    if randomthing > (infection_chance*100):
                        persontwo._Infected = True
                        #print(persontwo._Name, " Is now infected by ", person._Name)

        
    
    
    Want_Vac = input("Want to Vaccinate?").lower()
    if Want_Vac == "yes":
        for person in Population:
            if person._Vaccinating == False and person._Immune == False and person._Infected == False:
                print(person._Name)
                Vacc = input("Yes or no").lower()
                if Vacc == "yes":
                    person._Vaccinating = True





    
    leave = input("Exit?").lower()
    
            

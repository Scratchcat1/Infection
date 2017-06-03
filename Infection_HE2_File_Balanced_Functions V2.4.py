
class Person:
    def __init__(self,Name,Infected,Friends,Immune,Vaccinating,Time_Sick,Time_Vac,Number,x,y):
        self._Name=Name
        self._Infected=Infected
        self._Friends=Friends
        self._Immune=Immune
        self._Vaccinating= Vaccinating
        self._Time_Sick=Time_Sick
        self._Time_Vac=Time_Vac
        self._Number = Number
        self._x = x
        self._y = y

    def getName(self):
        return self._Name
    def getInfected(self):
        return self._Infected
    def getFriends(self):
        return self._Friends
    def getImmune(self):
        return self._Immune
    def getVaccinating(self):
        return self._Vaccinating
    def getTimeSick(self):
        return self._Time_Sick
    def getTimeVac(self):
        return self._Time_Vac
    def getNumber(self):
        return self._Number
    def getx(self):
        return self._x
    def gety(self):
        return self._y
    ##############

    def setInfected(self,setting):
        self._Infected = setting
    def setImmune(self,setting):
        self._Immune= setting
    def setVaccinating(self,setting):
        self._Vaccinating = setting
    def setTimeVac(self,time=None):
        if time != None:
            self._Time_Sick=time
        else:
            self._Time_Sick +=1
    def setTimeVac(self,time=None):
        if time != None:
            self._Time_Vac=time
        else:
            self._Time_Vac +=1
    def setx(self,x):
        self._x = x
    def sety(self,y):
        self._y=y
    
    def Return_Data(self):
        Friend_Sep = ""
        for item in self._Friends:
            Friend_Sep += (str(item)+",")
            
        Friend_Sep = Friend_Sep[0:len(Friend_Sep)-1]
        Tempoary = [self._Name,
        self._Infected,
        Friend_Sep,
        self._Immune,
        self._Vaccinating,
        self._Time_Sick,
        self._Time_Vac,
        self._Number ]
        Data =""
        for item in Tempoary:
            Data+= str(item)+";"
        Data = Data[0:len(Data)-1] +"###"
        #print(Data)
        return Data

import random,math,time
class Machine():
    def __init__(self,MachineID):
        print("Machine ",str(MachineID)," is starting up...")
        self.Infection_Chance = 0.3
        self.Waiting = 0

    def Change_Chance(self,chance):
        self.Infection_Chance = float(chance)

    def Change_Waiting(self,wait):
        self.Wating = float(wait)
        
    def Startup(self,input_val,Use_File,Pygame_Enable):
        self.Pygame_Enable = Pygame_Enable
        self.Pygame_Enable = input("Would you like to activate Pygame?").lower()
        #Pygame Resolution
        self.xpixel = 900
        self.ypixel =900
        if self.Pygame_Enable == "yes":
            self.Pygame_Enable = True
        else:
            self.Pygame_Enable = False
                

        if self.Pygame_Enable:
            try:
                import pygame
                pygame.init()
        ##        pygame.font.init()
                gameDisplay = pygame.display.set_mode((xpixel,ypixel))
                pygame.display.set_caption("Infection overview")
                self.clock = pygame.time.Clock()
            except:
                print("Pygame was not imported. Disabling")
                self.Pygame_Enable = False

        self.Population=[]
    ##    infection_chance = float(input("Infection Chance :"))
    ##    Waiting = int(input("Time between refreshes"))
    ##    Use_File = input("Open file? [Yes or No]").lower()
        if Use_File == True:
            File_Content =[]
            Open_File(input_val)
            self.Sort_Friends()
            """
            Possible_friends = []
            for jkl in range(len(Population)):
                Possible_friends.append(jkl)
                
                item._x,item._y= XCurrent+radius,YCurrent+radius
                XCurrent += SquareSize
                if XCurrent > (xpixel-XLength):
                    XCurrent = 0
                    YCurrent += SquareSize
            Possible_friends = []
            for person in Population:
                Possible_friends.append(person._Number)
                if "" in person._Friends:
                    person._Friends.pop(person._Friends.index(""))
            Possible_friends.pop(0)
            Possible_friends.insert(0,Population[0]._Number)"""
            #Population[0]._Friends = []  
            
        else:
            self.Population_Size = int(input_val)
            self.Possible_friends=[]
            self.Add_Population(self.Population_Size)
            ##    asdf = Population.index(person)
            ##    if asdf % 1000 == 0:
            ##        print(asdf)
                   

        self.total_friends=0
        for person in self.Population:
            self.total_friends += len(person._Friends)
            #print(person._Name,"  ",person._Infected,"  ",person._Immune,"  ",person._Vaccinating)
            #print(person._Friends)
            #print("")
        print(self.total_friends/(self.Population_Size))
        self.start = time.time()
        
        Infected = random.randint(0,len(self.Population)-1)
        self.Population[Infected].setInfected(True)
        self.day =1
          


    def Infect(self):
        for person in self.Population:
            for friend in person._Friends:
                persontwo = Population[friend]
                if person.getInfected()==True and persontwo.getInfected() == False and persontwo.getImmune == False:
                    randomthing = random.randint(0,100)
                    if randomthing < (self.infection_chance*100):
                        persontwo.setInfected(True)
                        #print("[Infected]   ",persontwo._Name, " by ", person._Name)
                        if self.Pygame_Enable: 
                            pygame.draw.line(gameDisplay,red,[person.getx(),person.gety()],[persontwo.getx(),persontwo.gety()])
        

    def Update_Status(self):
        for person in self.Population:
            if person.getInfected ==True:
                person.setTimeSick()
            if person.getVaccinating() == True:
                person.setTimeVac()
            if person.getVaccinating() == True and person.getTimeVac() > 2 and person.getInfected() == False:
                person.setImmune(True)
                person.setVaccinating(False)
                person.setTimeVac(0)
                #print("[Immune]   ",person._Name)
            
            randomthing = random.randint(0,100)
            if randomthing > 96 and person.getImmune() == True:
                person.setImmune(False)
                #print("[Immunity Lost]  ",person._Name)
                
             # Sick become immune
            elif person.getTimeSick()>= 6 and person.getInfected() == True:
                randomthing = random.randint(0,100)
                if randomthing > 80:
                    person.setTimeSick(0)
                    person.setImmune(True) 
                    person.setInfected(False)
                    #print("[Immune]   ",person._Name)
        

    def Save(self,filename,A_or_W):
        Write_Data =[]
        for item in self.Population:
            Write_Data.append(item.Return_Data())
        if ".txt" not in filename:
            filename += ".txt"
        with open(filename,A_or_W) as file:
            file.writelines(Write_Data)
    def Save_Go(self,filename):
        A_or_W = "w"
        self.Save(self,filename,A_or_W)

    def Colours():
        black = (0,0,0)
        white = (255,255,255)
        red = (255,0,0)
        green = (0,255,0)
        blue = (0,0,255)
        return black,white,red,green,blue

    def Set_Grid(self):
        ## Calculate display set up
        area = self.xpixel *self.ypixel
        areapp = area/self.Population_Size
        self.SquareSize = int((math.sqrt(areapp))//1)
        if self.SquareSize == 0:
            self.SquareSize = 1
        self.XLength = (self.xpixel/self.SquareSize)//1
        self.YLength = (self.ypixel/self.SquareSize)//1
        self.radius = int((self.SquareSize/2)//1)
        self.radius -=3
        if self.radius <1:
            self.radius = 1
        self.XCurrent = 0
        self.YCurrent = 0
        if self.Population != []:
            for person in self.Population:
                person.setx(self.XCurrent+self.radius)
                person.sety(self.YCurrent+self.radius)
                self.XCurrent += self.SquareSize
                if self.XCurrent > self.xpixel:#-XLength):
                    self.XCurrent = 0
                    self.YCurrent += SquareSize


    def Vaccinate(self,Vac_Val,Vac_Type):
        if Vac_Type == True:
            names = Vac_Val.split(",")
##            name = ""
##            print("Enter names to vaccinate, enter exit to leave")
##            
##            while True:
##                name = input("Enter name >:")
##                if name != "exit":
##                    names.append(name)
##                else:
##                    break
                             
            for person in self.Population:
                if person._Name in names and person.getInfected() == False:
                    person.setVaccinating( True)
            
        else:
            for asdf in range(int(Vac_Val)):
                num = random.randint(0,self.Population_Size)
                self.Population[num].setVaccinating(True)

    def Shuffle_Friends(self,Shuffle_Factor):
        for person in self.Population:
            for q in range(len(person._Friends)):
                randomthing = random.randint(0,1)
                if randomthing < Shuffle_Factor:
                    person._Friends.pop(q)
                    temp = random.choice(self.Possible_friends)
                    while temp in person._Friends:
                        temp = random.choice(self.Possible_friends)
                    person._Friends.insert(q,temp)

                        
    def Add_Population(self,amount):
        Name_list= ["Bob","Jeff","John","Ninja","Ryan","Watson","Hodges","Wendy","Gray","Hemmings","Nash","Hill","Dan","Liam","Theresa","Mimikyu","Peake","Lee","Molly","Chole","Tim"]
        if len(self.Population) == 0:
            Number = 0
            self.Possible_friends = []
        else:
            Number = len(self.Population)
        
        for ghj in range(len(self.Population),amount):
            self.Possible_friends.append(ghj)

                 
##        Difference = self.Population_Size - len(self.Population)
        for asdf in range(amount):  #Create Population
            Temp_Friends = []
            if len(self.Possible_friends)<5 and len(self.Possible_friends)>=1:
                Num_Friends = random.randint(1,len(self.Possible_friends))
            else:
                Num_Friends = random.randint(2,5)

            if len(self.Possible_friends)>0:
                for sdfewf in range(Num_Friends):
                    friend = random.choice(self.Possible_friends)
                    while friend in Temp_Friends:
                        friend = random.choice(self.Possible_friends)
                    Temp_Friends.append(friend)
            
            Name = random.choice(Name_list)+" #"+str(Number)
            self.Population.append(Person(Name,False,Temp_Friends,False,False,0,0,Number,0,0))
            Number+=1
        if self.Pygame_Enable:
            self.Set_Grid()
        else:
            self.radius = None
        self.Sort_Friends(factor = 40)



    def Sort_Friends(self,factor = 40):
        for person in self.Population:
            for friend in person._Friends:
                persontwo = self.Population[friend]
                if (persontwo._Number in person._Friends) and (person._Number not in persontwo._Friends):
                    randomthing = random.randint(0,100)
                    if randomthing < factor:
                        persontwo._Friends.append(person._Number)
                    else:
                        person._Friends.pop(person._Friends.index(persontwo._Number))

    def Open_File(self,filename):
        Original_Size = len(self.Population)
    ##    while len(Population)==Original_Size:
    ##        filename = input("Filename :")
        if ".txt" not in filename:
            filename += ".txt"
        try:
            with open(filename,"r") as file:
                File_Content = file.read()
            File_Content = File_Content.split("###")

            File_Content.pop(len(File_Content)-1)
            for item in File_Content:
                temp = []
                temp= item.split(";")
                self.Population.append(Person(temp[0],bool(temp[1] =="True"),temp[2].split(","),bool(temp[3] =="True"),bool(temp[4] =="True"),int(temp[5]),int(temp[6]),int(temp[7]),0,0))
            end = len(self.Population)
            for q in range(self.Population_Size,end):
                for x in range(len(self.Population[q]._Friends)):
                    self.Population[q]._Friends[x] = int(self.Population[q]._Friends[x])
                while "" in self.Population[q]._Friends:
                    self.Population[q]._Friends.pop(self.Population[q]._Friends.index(""))
                self.Possible_friends.append(q)
            self.Population_Size = len(self.Population)
            if Pygame_Enable:        
                Set_Grid()
            else:
                self.radius = None
        except:
            print("Error opening file")
            print("Please check filename and file formatting")

    def Infect_Analysis(self,level = 1):
        self.Result = []
        for person in self.Population:
            temp = 0
            for person2 in person._Friends:
                temp+=1
                if level >=2:
                    for person3 in self.Population[person2]._Friends:
                        temp+=1
                        if level >=3:
                            for person4 in self.Population[person3]._Friends:
                                temp+=1
                                if level >=4:
                                    for person5 in self.Population[person4]._Friends:
                                        temp+=1
                                        if level >=5:
                                            for person6 in self.Population[person5]._Friends:
                                                temp+=1
            self.Result.append(temp)

    def Days(self,Autodays,Pygame_Enable):
        self.Pygame_Enable = Pygame_enable
        for tempoaryautodays in range(wait_time):
            print("Day ",self.day)
            self.day+=1
        
            Update_Status()
            if self.Pygame_Enable:
                gameDisplay.fill(white)

                
            ## Has to be seperate to avoid people coming in contact multiplte times        
            Infect()
                      
                            
            
            if self.Pygame_Enable:
                black,white,red,green,blue = Colours()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        crashed = True
                for person in self.Population:
                    CircleColour = black
                    if person._Infected == True:
                        CircleColour = red
                    elif person._Immune == True:
                        CircleColour = blue
                    else:
                        CircleColour = green
                    pygame.draw.circle(gameDisplay,CircleColour,[person._x,person._y],radius)
        ##            pygame.font.Font.render(str(person._Number),False,black,gameDisplay)
                
                pygame.display.update()            
            time.sleep(self.Waiting)

    """                
    leave = "In"
    crashed = False
    while leave != "yes" and not crashed:

                
                
        Analysis_Switch = input("Want to analyse Population").lower()
        if Analysis_Switch == "yes":
            level = int(input("What level of analysis [1-5]"))
            Result = Infect_Analysis(Population,level)
            No_items = int(input("First __ items"))
            for iop in range(No_items):
                location = Result.index(max(Result))
                print("{0:15} : {1:10}".format(Population[location]._Name,str(Result[location])))
                Result[location] = 0
        
        Want_Vac = input("Want to Vaccinate?").lower()
        if Want_Vac == "yes":
            print("~~~~~Vaccination Menu~~~~~")
            print("1. Choice")
            print("2. Random vaccination")
            Vac_Type = int(input(">: "))
            Population = Vaccinate(Population,Vac_Type,Population_Size)

        Friend_Switch = input("Want to shuffle friends").lower()
        if Friend_Switch == "yes":
            Shuffle_Factor = float(input("Enter shuffle factor [0-None,1-All]"))
            Population = Shuffle_Friends(Population,Possible_friends,Shuffle_Factor)

        Add_Switch = input("Would you like to add people?[No, Yes, File]").lower()
        if Add_Switch == "yes":
            People_to_add = int(input("Enter number of people to add"))
            People_to_add += Population_Size
            Population,Population_Size,Possible_friends,radius = Add_Population(Population,Possible_friends,People_to_add,xpixel,ypixel)
        elif Add_Switch == "file":
            Population,Population_Size,Possible_friends,radius = Open_File(Population,Population_Size,Possible_friends,xpixel,ypixel)

        
                
            



        
        leave = input("Exit?").lower()

    end = time.time()
    print(str(end-start),"Seconds")
    """









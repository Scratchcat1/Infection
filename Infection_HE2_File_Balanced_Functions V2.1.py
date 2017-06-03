
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
        

Pygame_Enable = input("Would you like to activate Pygame?").lower()
#Pygame Resolution
xpixel = 900
ypixel =900
if Pygame_Enable == "yes":
    Pygame_Enable = True
else:
    Pygame_Enable = False
        
import random,math,time
if Pygame_Enable:
    try:
        import pygame
        pygame.init()
##        pygame.font.init()
        gameDisplay = pygame.display.set_mode((xpixel,ypixel))
        pygame.display.set_caption("Infection overview")
        clock = pygame.time.Clock()
    except:
        print("Pygame was not imported. Disabling")
        Pygame_Enable = False


def Infect(Population,infection_chance):
    for person in Population:
        for friend in person._Friends:
            persontwo = Population[friend]
            if person._Infected==True and persontwo._Infected == False and persontwo._Immune == False:
                randomthing = random.randint(0,100)
                if randomthing < (infection_chance*100):
                    persontwo._Infected = True
                    #print("[Infected]   ",persontwo._Name, " by ", person._Name)
                    if Pygame_Enable: 
                        pygame.draw.line(gameDisplay,red,[person._x,person._y],[persontwo._x,persontwo._y])
    return Population

def Update_Status(Population):
    for person in Population:
        if person._Infected ==True:
            person._Time_Sick +=1
        if person._Vaccinating == True:
            person._Time_Vac +=1
        if person._Vaccinating == True and person._Time_Vac > 2 and person._Infected == False:
            person._Immune = True
            person._Vaccinating == False
            person._Time_Vac = 0
            #print("[Immune]   ",person._Name)
        
        randomthing = random.randint(0,100)
        if randomthing > 96 and person._Immune == True:
            person._Immune = False
            #print("[Immunity Lost]  ",person._Name)
            
         # Sick become immune
        elif person._Time_Sick >= 6 and person._Infected == True:
            randomthing = random.randint(0,100)
            if randomthing > 80:
                person._Time_Sick = 0
                person._Immune = True
                person._Infected = False
                #print("[Immune]   ",person._Name)
    return Population

def Save(Population,filename,A_or_W):
    Write_Data =[]
    for item in Population:
        Write_Data.append(item.Return_Data())
    if ".txt" not in filename:
        filename += ".txt"
    with open(filename,A_or_W) as file:
        file.writelines(Write_Data)

def Colours():
    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    return black,white,red,green,blue

def Set_Grid(xpixel,ypixel,Population_Size,Population = None):
    ## Calculate display set up
    area = xpixel *ypixel
    areapp = area/Population_Size
    SquareSize = int((math.sqrt(areapp))//1)
    if SquareSize == 0:
        SquareSize = 1
    XLength = (xpixel/SquareSize)//1
    YLength = (ypixel/SquareSize)//1
    radius = int((SquareSize/2)//1)
    radius -=3
    if radius <1:
        radius = 1
    XCurrent = 0
    YCurrent = 0
    if Population != None:
        for person in Population:
            person._x,person._y= XCurrent+radius,YCurrent+radius
            XCurrent += SquareSize
            if XCurrent > xpixel:#-XLength):
                XCurrent = 0
                YCurrent += SquareSize
        return SquareSize,XLength,YLength,radius,XCurrent,YCurrent,Population
    else:
        return SquareSize,XLength,YLength,radius,XCurrent,YCurrent

def Vaccinate(Population,Vac_Type,Population_Size):
    if Vac_Type == 1:
        names = []
        name = ""
        print("Enter names to vaccinate, enter exit to leave")
        
        while True:
            name = input("Enter name >:")
            if name != "exit":
                names.append(name)
            else:
                break
                         
        for person in Population:
            if person._Name in names and person._Infected == False:
                person._Vaccinating = True
        
    elif Vac_Type == 2:
        number = int(input("Number of vaccinations"))
        for asdf in range(number):
            num = random.randint(0,Population_Size)
            Population[num]._Vaccinating = True
    return Population

def Shuffle_Friends(Population,Possible_friends,Shuffle_Factor):
    for person in Population:
        for q in range(len(person._Friends)):
            randomthing = random.randint(0,1)
            if randomthing < Shuffle_Factor:
                person._Friends.pop(q)
                temp = random.choice(Possible_friends)
                while temp in person._Friends:
                    temp = random.choice(Possible_friends)
                person._Friends.insert(q,temp)
    return Population
                    
def Add_Population(Population,Possible_friends,Population_Size,xpixel,ypixel):
    Name_list= ["Bob","Jeff","John","Ninja","Ryan","Watson","Hodges","Wendy","Gray","Hemmings","Nash","Hill","Dan","Liam","Theresa","Mimikyu","Peake","Lee","Molly","Chole","Tim"]
    if len(Population) == 0:
        Number = 0
        Possible_friends = []
    else:
        Number = len(Population)-1
    
    for ghj in range(len(Population),Population_Size):
        Possible_friends.append(ghj)

             
    Difference = Population_Size - len(Population)
    for asdf in range(Difference):  #Create Population
        Temp_Friends = []
        if len(Possible_friends)<5 and len(Possible_friends)>=1:
            Num_Friends = random.randint(1,len(Possible_friends))
        else:
            Num_Friends = random.randint(2,5)

        if len(Possible_friends)>0:
            for sdfewf in range(Num_Friends):
                friend = random.choice(Possible_friends)
                while friend in Temp_Friends:
                    friend = random.choice(Possible_friends)
                Temp_Friends.append(friend)
        
        Name = random.choice(Name_list)+" #"+str(Number)
        Population.append(Person(Name,False,Temp_Friends,False,False,0,0,Number,0,0))
        Number+=1
    if Pygame_Enable:
        SquareSize,XLength,YLength,radius,XCurrent,YCurrent,Population= Set_Grid(xpixel,ypixel,Population_Size,Population)
    else:
        radius = None
    Sort_Friends(Population,factor = 40)
    return Population,Population_Size,Possible_friends,radius


def Sort_Friends(Population,factor = 60):
    for person in Population:
        for friend in person._Friends:
            persontwo = Population[friend]
            if (persontwo._Number in person._Friends) and (person._Number not in persontwo._Friends):
                randomthing = random.randint(0,100)
                if randomthing < factor:
                    persontwo._Friends.append(person._Number)
                else:
                    person._Friends.pop(person._Friends.index(persontwo._Number))
    return Population

def Open_File(Population,Population_Size,Possible_friends,xpixel,ypixel):
    Original_Size = len(Population)
    while len(Population)==Original_Size:
        filename = input("Filename :")
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
                Population.append(Person(temp[0],bool(temp[1] =="True"),temp[2].split(","),bool(temp[3] =="True"),bool(temp[4] =="True"),int(temp[5]),int(temp[6]),int(temp[7]),0,0))
            end = len(Population)
            for q in range(Population_Size,end):
                for x in range(len(Population[q]._Friends)):
                    Population[q]._Friends[x] = int(Population[q]._Friends[x])
                while "" in Population[q]._Friends:
                    Population[q]._Friends.pop(person._Friends.index(""))
                Possible_friends.append(q)
            Population_Size = len(Population)
            if Pygame_Enable:        
                SquareSize,XLength,YLength,radius,XCurrent,YCurrent = Set_Grid(xpixel,ypixel,Population_Size,Population)
            else:
                radius = None
        except:
            print("Error opening file")
            print("Please check filename and file formatting")
    return Population,Population_Size,Possible_friends,radius # Please update possible friends after calling this function

def Infect_Analysis(Population,level = 1):
    Result = []
    for person in Population:
        temp = 0
        for person2 in person._Friends:
            temp+=1
            if level >=2:
                for person3 in Population[person2]._Friends:
                    temp+=1
                    if level >=3:
                        for person4 in Population[person3]._Friends:
                            temp+=1
                            if level >=4:
                                for person5 in Population[person4]._Friends:
                                    temp+=1
                                    if level >=5:
                                        for person6 in Population[person5]._Friends:
                                            temp+=1
        Result.append(temp)
    return Result
                
Population=[]
infection_chance = float(input("Infection Chance :"))
Waiting = int(input("Time between refreshes"))
Use_File = input("Open file? [Yes or No]").lower()
File_Content =[]
if Use_File == "yes":
    Population,Population_Size,Possible_friends,radius = Open_File(Population,Population_Size,Possible_friends,xpixel,ypixel)
    Population = Sort_Friends(Population)
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
    Population_Size = int(input("Enter the Population size :"))
    Possible_friends=[]
    Population, Population_Size,Possible_friends,radius = Add_Population(Population,Possible_friends,Population_Size,xpixel,ypixel)
    ##    asdf = Population.index(person)
    ##    if asdf % 1000 == 0:
    ##        print(asdf)

           

total_friends=0
for person in Population:
    total_friends += len(person._Friends)
    #print(person._Name,"  ",person._Infected,"  ",person._Immune,"  ",person._Vaccinating)
    #print(person._Friends)
    #print("")
print(total_friends/(Population_Size))






Possible_friends=[]
start = time.time()
black,white,red,green,blue = Colours()
Infected = random.randint(0,len(Population)-1)
Population[Infected]._Infected = True
day =1
leave = "In"
crashed = False
while leave != "yes" and not crashed:
    Want_Save = input("Do you want to save? [Yes or No]").lower()
    if Want_Save == "yes":
        filename = input("Filename: ")
        A_or_W = input("Append or Overwrite [A or W]").lower()
        Save(Population,filename,A_or_W)
        
            
    wait_time= int(input("Auto Days"))
    for tempoaryautodays in range(wait_time):
        print("Day ",day)
        day+=1
    
        Population = Update_Status(Population)
        if Pygame_Enable:
            gameDisplay.fill(white)

            
        ## Has to be seperate to avoid people coming in contact multiplte times        
        Population = Infect(Population,infection_chance)
                  
                        
        
        if Pygame_Enable:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
            for person in Population:
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
        time.sleep(Waiting)
            
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
            

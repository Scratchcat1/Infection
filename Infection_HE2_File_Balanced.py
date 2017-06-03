
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
            Friend_Sep += (item+",")
            
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
        

 
        
import random,pygame,math,time
pygame.init()
pygame.font.init()
xpixel = 1200
ypixel =800
gameDisplay = pygame.display.set_mode((xpixel,ypixel))
pygame.display.set_caption("Infection overview")
clock = pygame.time.Clock()

def Colours():
    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    return black,white,red,green,blue

def Set_Grid(xpixel,ypixel,Population_Size):
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
    return SquareSize,XLength,YLength,radius,XCurrent,YCurrent


Population=[]
infection_chance = float(input("Infection Chance :"))
Waiting = int(input("Time between refreshes"))
Use_File = input("Open file? [Yes or No]").lower()
File_Content =[]
if Use_File == "yes":
    while len(Population)==0:
        filename = input("Filename :")
        if ".txt" not in filename:
            filename += ".txt"
##        try:
            with open(filename,"r") as file:
                File_Content = file.read()
            File_Content = File_Content.split("###")

            File_Content.pop(len(File_Content)-1)
            for item in File_Content:
                temp = []
                temp= item.split(";")
                Population.append(Person(temp[0],bool(temp[1] =="True"),temp[2].split(","),bool(temp[3] =="True"),bool(temp[4] =="True"),int(temp[5]),int(temp[6]),int(temp[7]),0,0))
                
##        except:
##            print("Error opening or processing file")
    Population_Size = len(Population)
    SquareSize,XLength,YLength,radius,XCurrent,YCurrent= Set_Grid(xpixel,ypixel,Population_Size)
    for item in Population:
        for friend in item._Friends:
            friend = int(friend)
        item._x,item._y= XCurrent+radius,YCurrent+radius
        XCurrent += SquareSize
        if XCurrent > (xpixel-XLength):
            XCurrent = 0
            YCurrent += SquareSize
    Possible_friends = []
    for person in Population:
        Possible_friends.append(person._Name)
        if "" in person._Friends:
            person._Friends.pop(person._Friends.index(""))
    Possible_friends.pop(0)
    Possible_friends.insert(0,Population[0]._Name)
    Population[0]._Friends = []
        
    
            
    
else:
    Name_list= ["Bob","Jeff","John","Ninja","Ryan","Watson","Hodges","Wendy","Gray","Hemmings","Nash","Hill","Dan","Liam","Theresa","Mimikyu","Peake","Lee","Molly","Chole","Tim"]
    Population_Size = int(input("Enter the Population size :"))
    Number = 0
    Possible_friends = []
    for ghj in range(Population_Size):
        Possible_friends.append(ghj)
    SquareSize,XLength,YLength,radius,XCurrent,YCurrent= Set_Grid(xpixel,ypixel,Population_Size)
             

    for asdf in range(Population_Size):  #Create Population
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
        Population.append(Person(Name,False,Temp_Friends,False,False,0,0,Number,XCurrent+radius,YCurrent+radius))
        Number+=1
        XCurrent += SquareSize
        if XCurrent > xpixel:
            XCurrent = 0
            YCurrent += SquareSize


    for person in Population:
        for friend in person._Friends:
            persontwo = Population[friend]
            if (persontwo._Number in person._Friends) and (person._Number not in persontwo._Friends):
                randomthing = random.randint(0,100)
                if randomthing > 40:
                    persontwo._Friends.append(person._Number)
                else:
                    person._Friends.pop(person._Friends.index(persontwo._Number))
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
        Write_Data =[]
        for item in Population:
            Write_Data.append(item.Return_Data())
        filename = input("Filename: ")
        if ".txt" not in filename:
            filename += ".txt"
        A_or_W = input("Append or Overwrite [A or W]").lower()
        with open(filename,A_or_W) as file:
            file.writelines(Write_Data)
        
            
    wait_time= int(input("Auto Days"))
    for tempoaryautodays in range(wait_time):
        print("Day ",day)
        day+=1
    
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
        gameDisplay.fill(white)
            ## Has to be seperate to avoid people coming in contact multiplte times        
        for person in Population:
            for friend in person._Friends:
                persontwo = Population[friend]
                if person._Infected==True and persontwo._Infected == False and persontwo._Immune == False:
                    randomthing = random.randint(0,100)
                    if randomthing < (infection_chance*100):
                        persontwo._Infected = True
                        #print("[Infected]   ",persontwo._Name, " by ", person._Name)
                        pygame.draw.line(gameDisplay,red,[person._x,person._y],[persontwo._x,persontwo._y])
                  
                        
        
        
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
            """
            for persontwo in Population:
                if persontwo._Name in person._Friends and person._Number < persontwo._Number:
                    pygame.draw.line(gameDisplay,black,[person._x,person._y],[persontwo._x,persontwo._y])
                    """
        pygame.display.update()            
        time.sleep(Waiting)
            
    
    
    Want_Vac = input("Want to Vaccinate?").lower()
    if Want_Vac == "yes":
        for person in Population:
            if person._Vaccinating == False and person._Immune == False and person._Infected == False:
                print(person._Name)
                Vacc = input("Yes or no").lower()
                if Vacc == "yes":
                    person._Vaccinating = True





    
    leave = input("Exit?").lower()

end = time.time()
print(str(end-start),"Seconds")
            

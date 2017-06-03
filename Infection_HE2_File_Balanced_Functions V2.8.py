#from tkinter import Tk,BOTH,Frame,Button
from tkinter import *
from multiprocessing import Process,cpu_count,Queue#,Array
import multiprocessing

#Make a window class

class window(Frame):
    def __init__(self, parent,Colour,Title):
        Frame.__init__(self, parent, background=Colour)    
        self.parent = parent
        self.Main_Menu()
        self.centerWindow()
        
    def Multiply(self,x,y):
        print(str(int(x)*float(y)))

        
    def Main_Menu(self):
        self.parent.title("Sim Control - Win12")
        main = self.parent
        # Left side setup 
        Label(main, text="Setup").grid(row=0)
        Label(main, text="Population").grid(row=1)


        e1 = Entry(main)
        e1.grid(row=1, column=1,padx =5,pady=5)
        Use_File = Checkbutton(main,text = "Open file - input above",command = lambda:Machine1.Use_File_Switch())
        Use_File.grid(row = 2,column = 1)
        Use_Pygame = Checkbutton(main,text = "Use Pygame?",command = lambda:Machine1.Pygame_Switch())
        Use_Pygame.grid(row = 2,column = 0)
                
        #e1.insert(0,"CAT")
        Button(main,text ="Make",command=lambda : Machine1.Startup(e1.get())).grid(row=3,column = 1,padx=5,pady=5)
        for q in range(1,9):
            Label(main, text="   |   ").grid(row=q,column=2)

        Label(main, text="Auto Days").grid(row=1,column=3)
        
        autoday = Entry(main)
        autoday.grid(row=1, column=4,padx =5,pady=5)
        Button(main,text ="Run Simulation",command=lambda : Machine1.Days(int(autoday.get()))).grid(row=1,column = 5,padx=5,pady=5)

        Label(main, text="Add People").grid(row=2,column=3)
        addpeople = Entry(main)
        addpeople.grid(row=2, column=4,padx =5,pady=5)
        Button(main,text ="Add People",command=lambda : Machine1.Add_Population(int(addpeople.get()))).grid(row=2,column = 5,padx=5,pady=5)

        Label(main, text="Append File").grid(row=3,column=3)
        addfile = Entry(main)
        addfile.grid(row=3, column=4,padx =5,pady=5)
        Button(main,text ="Add file",command=lambda : Machine1.Open_File(addfile.get())).grid(row=3,column = 5,padx=5,pady=5)

        Label(main, text="Save File").grid(row=4,column=3)
        savefile = Entry(main)
        savefile.grid(row=4, column=4,padx =5,pady=5)
        Button(main,text ="Save file",command=lambda : Machine1.Save_Go(savefile.get())).grid(row=4,column = 5,padx=5,pady=5)

        Label(main, text="Infect Chance").grid(row=5,column=3)
        chance = Entry(main)
        chance.grid(row=5, column=4,padx =5,pady=5)
        Button(main,text ="Set Value",command=lambda : Machine1.Change_Chance(chance.get())).grid(row=5,column = 5,padx=5,pady=5)

        Label(main, text="Wait time").grid(row=6,column=3)
        waitentry = Entry(main)
        waitentry.grid(row=6, column=4,padx =5,pady=5)
        Button(main,text ="Set Value",command=lambda : Machine1.Change_Waiting(waitentry.get())).grid(row=6,column = 5,padx=5,pady=5)

        Label(main, text="Vaccination").grid(row=7,column=3)
        VacEntry = Entry(main)
        VacEntry.grid(row=7, column=4,padx =5,pady=5)
        Button(main,text ="Vaccinate",command=lambda : Machine1.Vaccinate(VacEntry.get())).grid(row=7,column = 5,padx=5,pady=5)
        Use_Names = Checkbutton(main,text = "Process as Name",command = lambda:Machine1.Set_Vac_Type())
        Use_Names.grid(row = 8,column = 4)
        
        Label(main, text="").grid(row=5,column=1)
        shuffleFactor = Entry(main)
        shuffleFactor.grid(row=6, column=1,padx =5,pady=5)
        Button(main,text ="Shuffle Friends",command=lambda : Machine1.Shuffle_Friends(int(shuffleFactor.get()))).grid(row=6,column = 0,padx=5,pady=5)

        AnalysisLevel = Entry(main)
        AnalysisLevel.grid(row=7, column=1,padx =5,pady=5)
        Button(main,text ="Infect Analysis",command=lambda : Machine1.Infect_Analysis(int(AnalysisLevel.get()))).grid(row=7,column = 0,padx=5,pady=5)
        

        
    def centerWindow(self):
        w = 700# Width and height of window
        h = 500

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw-w)/2
        y = (sh-h)/2
        #self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))
        

def main_window():
    root = Tk()
    root.geometry("800x400+300+300")
    wind = window(root,"white","TITLE")
    root.attributes('-alpha', 1)
    root.mainloop()


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
    def setTimeSick(self,time=None):
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
try:
    import pygame
except:
    print("No pygame")
class Machine():
    def __init__(self,MachineID):
        print("Machine ",str(MachineID)," is starting up...")
        self.Infection_Chance = 0.3
        self.Waiting = 0
        self.Possible_friends = []
        self.Population_Size = 0
        self.Use_File = False
        self.Pygame_Enable = False
        self.Vac_Type = False
        self.day = 1
        self.Colours()
        #self.Population = Array("i",range(10))
        self.Population=[]
        self.Update_Split_List()
        self.Transfer_Queue = Queue()
        

    def Change_Chance(self,chance):
        try:    
            self.Infection_Chance = float(chance)
        except:
            print("Error changing Infection Chance")

    def Change_Waiting(self,wait):
        try:
            self.Waiting = float(wait)
        except:
            print("Error Changing wait time")

    def Pygame_Switch(self):
        if self.Pygame_Enable == False:
            self.Pygame_Enable = True
            print("Pgame")
        else:
            self.Pygame_Enable = False
    def Use_File_Switch(self):
        if self.Use_File == False:
            self.Use_File = True
        else:
            self.Use_File = False

    def Set_Vac_Type(self):
        if self.Vac_Type == False:
            self.Vac_Type = True
        else:
            self.Vac_Type = False
        
    def Update_Split_List(self):
        try:
            self.cores = cpu_count()
        except:
            self.cores = 4
        split = math.ceil(self.Population_Size/self.cores)
        print(self.Population_Size)
        
        self.split_list=[]
        for splitting in range(self.cores):
            self.split_list.append(splitting*split)
        self.split_list.append(self.Population_Size)

    def Infect_Starter(self):
        procs = []
        Transfer_Queue = Queue()
        for fdsa in range(self.cores):
            p = multiprocessing.Process(target = self.Infect(self.Population,self.split_list[fdsa],self.split_list[fdsa+1],Transfer_Queue))
            print(self.split_list)
            procs.append(p)
            p.start()
        self.Population =[]
        aas = []
        for p in procs:
            aas +=Transfer_Queue.get()
            p.join()

 

    
    def Startup(self,input_val):
        
        
##        self.Pygame_Enable = input("Would you like to activate Pygame?").lower()
        #Pygame Resolution
        self.xpixel = 1500
        self.ypixel =800
##        if self.Pygame_Enable == "yes":
##            self.Pygame_Enable = True
##        else:
##            self.Pygame_Enable = False
                

        if self.Pygame_Enable:
            try:
                pygame.init()
        ##        pygame.font.init()
                self.gameDisplay = pygame.display.set_mode((self.xpixel,self.ypixel))
                pygame.display.set_caption("Infection overview")
                self.clock = pygame.time.Clock()
            except:
                print("Pygame was not imported. Disabling")
                self.Pygame_Enable = False
        try:
            self.Population=[]
        ##    infection_chance = float(input("Infection Chance :"))
        ##    Waiting = int(input("Time between refreshes"))
        ##    Use_File = input("Open file? [Yes or No]").lower()
            if self.Use_File == True:
                File_Content =[]
                self.Open_File(input_val)
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
        except:
            print("Error creating inital population")
            print("Filename may not exist or input is not an integer")

    def Infect(self,Population,start,end,Transfer_Queue):
        #print(start,":",end)
        for person in Population[start:end]:
            for friend in person._Friends:
                persontwo = Population[friend]           
                if person.getInfected()==True and persontwo.getInfected() == False and persontwo.getImmune() == False:
                    randomthing = random.randint(0,100)
                    if randomthing < (self.Infection_Chance*100):
                        persontwo.setInfected(True)
                        #print("[Infected]   ",persontwo._Name, " by ", person._Name)
                        if self.Pygame_Enable: 
                            pygame.draw.line(self.gameDisplay,self.red,[person.getx(),person.gety()],[persontwo.getx(),persontwo.gety()])
        Transfer_Queue.put(Population[start:end])                            
                            

    def Update_Status(self):
        for person in self.Population:
            if person.getInfected() ==True:
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
        self.Save(filename,A_or_W)

    def Colours(self):
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.red = (255,0,0)
        self.green = (0,255,0)
        self.blue = (0,0,255)

    def Set_Grid(self):
        ## Calculate display set up
        print("Processing grid")
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

        for person in self.Population:
            person.setx(self.XCurrent+self.radius)
            person.sety(self.YCurrent+self.radius)
            self.XCurrent += self.SquareSize
            if self.XCurrent > self.xpixel:#-XLength):
                self.XCurrent = 0
                self.YCurrent += self.SquareSize
        print("Grid set up")


    def Vaccinate(self,Vac_Val):
        if self.Vac_Type == False:
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
        self.Update_Split_List()
        for person in self.Population:
            for q in range(len(person._Friends)):
                randomthing = random.randint(0,1)
                if randomthing < Shuffle_Factor:
                    person._Friends.pop(q)
                    temp = random.choice(self.Possible_friends)
                    while temp in person._Friends:
                        temp = random.choice(self.Possible_friends)
                    person._Friends.insert(q,temp)
        print("Friends shuffled")

                        
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
            self.Population_Size = len(self.Population)
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
                while "" in self.Population[q]._Friends:
                    self.Population[q]._Friends.pop(self.Population[q]._Friends.index(""))
                for x in range(len(self.Population[q]._Friends)):
                    temp = int(self.Population[q]._Friends[x])
                    self.Population[q]._Friends[x] = temp
                
                self.Possible_friends.append(q)
            self.Population_Size = len(self.Population)
            if self.Pygame_Enable:        
                Set_Grid()
            else:
                self.radius = None
        except:
            print("Error opening file")
            print("Please check filename and file formatting")

    def Infect_Analysis(self,level = 1):
        Result = []
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
            Result.append(temp)
        if len(self.Population)>= 30:
            No_items = 30
        else:
            No_items = len(self.Population)
        for iop in range(No_items):
            location = Result.index(max(Result))
            print("{0:15} : {1:10}".format(self.Population[location]._Name,str(Result[location])))
            Result[location] = 0

    def Days(self,wait_time):
        
        for tempoaryautodays in range(wait_time):
            print("Day ",self.day)
            self.day+=1
        
            self.Update_Status()
            if self.Pygame_Enable:
                self.gameDisplay.fill((0,0,0))

                
            ## Has to be seperate to avoid people coming in contact multiplte times        
            self.Infect_Starter()
                      
                            
            
            if self.Pygame_Enable:
                self.Colours()
##                for event in pygame.event.get():
##                    if event.type == pygame.QUIT:
##                        crashed = True
                for person in self.Population:
                    CircleColour = self.black
                    if person._Infected == True:
                        CircleColour = self.red
                    elif person._Immune == True:
                        CircleColour = self.blue
                    else:
                        CircleColour = self.green
                    pygame.draw.circle(self.gameDisplay,CircleColour,[person.getx(),person.gety()],self.radius)
        ##            pygame.font.Font.render(str(person._Number),False,black,self.gameDisplay)
                
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




if __name__ == "__main__":
    Machine1 = Machine(1)
    main_window()





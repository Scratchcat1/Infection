#from tkinter import Tk,BOTH,Frame,Button
from tkinter import *
#http://dba.stackexchange.com/questions/48568/how-to-relate-two-rows-in-the-same-table
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



import random,math,time
import sqlite3 as sql
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

    def Reset(self):
        self.cur.execute("DROP TABLE IF EXISTS population")
        self.cur.execute("DROP TABLE IF EXISTS friends") 
        self.cur.execute("CREATE TABLE population(Number INTEGER PRIMARY KEY NOT NULL, Infected INTEGER, Vaccing INTEGER, Immune INTEGER, TimeVac INTEGER, TimeSick INTEGER, x INTEGER, y INTEGER)")
        self.cur.execute("CREATE TABLE friends(Number INTEGER, Friend INTEGER)")
        self.con.commit()
            
    def Startup(self,input_val):
        self.con = sql.connect(":memory:")#Population.db
        self.cur = self.con.cursor()
        self.Reset()
        input_val = int(input_val)
        
        
        
        try:    
            self.xpixel = 1500
            self.ypixel =800


            if self.Pygame_Enable:
                try:
                    
                    pygame.init()
            ##        pygame.font.init()
                    self.gameDisplay = pygame.display.set_mode((self.xpixel,self.ypixel))
                    pygame.display.set_caption("Infection overview")
                    self.clock = pygame.time.Clock()
                    self.Colours()
                except:
                    print("Pygame was not imported. Disabling")
                    self.Pygame_Enable = False
           
            self.day =1
            
        except:
            print("Error creating inital population")
            print("Filename may not exist or input is not an integer")
        self.Add_Population(input_val)
        position = random.randint(1,self.Population_Size)
        self.cur.execute("UPDATE population SET Infected = 1 WHERE Number = ?",(position,))
            


    def Infect(self):
##        self.cur.execute("WITH Infect AS (SELECT Number FROM population WHERE Infected = 1) UPDATE population,friends,Infect SET population.Infected = 1 WHERE population.Number = friends.Number AND friends.Friend IN Infect")
##        self.cur.execute("SELECT Number FROM population WHERE Infected = 1")
##        self.cur.execute("SELECT DISTINCT Number FROM friends WHERE friend IN ?")
##        self.cur.execute("SELECT * FROM population")
##        for item in self.cur.fetchall():
##            print(item)
        start = time.time()
        self.cur.execute("UPDATE population SET Infected = 1 WHERE Infected = 0 AND Number = (SELECT DISTINCT Number FROM friends WHERE Friend = (SELECT Number FROM population WHERE Infected = 1))")
        end = time.time()
        self.cur.execute("SELECT COUNT(1) FROM population")
        #print(self.cur.fetchall()[0][0]/(end-start)," Updates per second")
        

    def Update_Status(self):
                         
        self.cur.execute("UPDATE population SET TimeVac = TimeVac+1 WHERE Vaccing = 1")
        self.cur.execute("UPDATE population SET TimeSick = TimeSick +1 WHERE Infected = 1")
        self.cur.execute("UPDATE population SET Immune = 1, TimeVac = 0,TimeSick = 0,Vaccing = 0,Infected = 0 WHERE TimeVac >= 2 OR TimeSick >=6")
        
        self.cur.execute("SELECT Number FROM population WHERE Immune = 1")
        Immunes = self.cur.fetchall()
        chosen = random.sample(Immunes,int(len(Immunes)*0.04))
        self.cur.executemany("UPDATE population SET Immune = 0 WHERE Number = ?",chosen)
        self.con.commit()
        

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
        data = []
        for person in range(1,self.Population_Size+1):
            data.append(((self.XCurrent+self.radius),(self.YCurrent+self.radius),person))
            self.XCurrent += self.SquareSize
            if self.XCurrent > self.xpixel:#-XLength):
                self.XCurrent = 0
                self.YCurrent += self.SquareSize
        self.cur.executemany("UPDATE population SET x = ?,y = ? WHERE Number = ?",data)
        self.con.commit()
        print("Grid set up")



    def Vaccinate(self,Vac_Val):
        if self.Vac_Type == True:
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
                num = random.randint(0,self.Population_Size-1)
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
        print("Friends shuffled")

                        
    def Add_Population(self,input_val):        
        self.cur.executemany("INSERT INTO population(Infected,Immune,Vaccing,TimeVac,TimeSick,x,y) VALUES(?,?,?,?,?,?,?)",[(0,0,0,0,0,0,0)]*input_val)
        self.con.commit()
        
        self.cur.execute("SELECT Number FROM population")
        possible_friends = self.cur.fetchall()

######        #V1
        Friend_List=[]
        
        for x in range(1,input_val+1):
            temp=(random.sample(possible_friends,random.randint(1,6)))
            for item in temp:
                Friend_List.append((x,item[0]))

                
        self.cur.executemany("INSERT INTO friends VALUES(?,?)",Friend_List)
        
        self.cur.execute("SELECT COUNT(Number) FROM population")
        self.Population_Size = self.cur.fetchone()[0]
        if self.Pygame_Enable:
            self.Set_Grid()

        else:
            self.radius = None
        self.Sort_Friends(factor = 40)



    def Sort_Friends(self,factor = 40):
        #self.cur.execute("WITH Flip(Number,Friend) AS (SELECT Number,Friend FROM friends) INSERT INTO friends(Number,Friend) SELECT Flip.Friend,Flip.Number WHERE NOT EXISTS(SELECT 1 FROM friends,Flip WHERE friends.Number = Flip.Friend AND friends.Friend = Flip.Number)")
        self.cur.execute("WITH Flip(Number,Friend) AS (SELECT Number,Friend FROM friends) INSERT INTO friends(Number,Friend) SELECT Flip.Friend,Flip.Number FROM Flip,friends WHERE NOT EXISTS(SELECT 1 FROM friends,Flip WHERE friends.Number = Flip.Friend AND friends.Friend = Flip.Number)")
        self.cur.execute("DELETE FROM friends WHERE Number = Friend")
        print("Friends sorted")
##        self.cur.execute("SELECT * FROM friends")
##        for x in self.cur.fetchall():
##            print(x)
        pass
    
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

            
            ## Has to be seperate to avoid people coming in contact multiplte times        
            self.Infect()
                      
                            
            
            if self.Pygame_Enable:
                
##                for event in pygame.event.get():
##                    if event.type == pygame.QUIT:
##                        crashed = True
                self.gameDisplay.fill((0,0,0))
                self.cur.execute("SELECT Infected,Immune,x,y FROM population ORDER BY Number ASC")
                Population = self.cur.fetchall()
                for person in Population:
##                    CircleColour = self.black
                    if person[0] == 1:
                        CircleColour = self.red
                    elif person[1] == 1:
                        CircleColour = self.blue
                    else:
                        CircleColour = self.green
                    pygame.draw.circle(self.gameDisplay,CircleColour,[person[2],person[3]],self.radius)
        ##            pygame.font.Font.render(str(person._Number),False,black,self.gameDisplay)
                Population = 0
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

Machine1 = Machine(1)

if __name__ == "__main__":
    main_window()





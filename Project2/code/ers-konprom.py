# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 12:30:16 2018

@author: kronprom
"""
import sqlite3 #Import the SQLite3 module


class Room:
    def __init__(self,room_id, name, building, floor,open_time,close_time, is_open):
        self._room_id = room_id
        self._name = name
        self._buliding = building
        self._floor = floor
        self._is_open = is_open
        self._open_time = open_time
        self._close_time = close_time
    
    def get_room_id(self):
        return self._room_id
    
    def get_name(self):
        return self._name
    
    def get_building(self):
        return self._buliding
    
    def get_floor(self):
        return self._floor
    
    def get_open_time(self):
        return self._open_time
    
    def get_close_time(self):
        return self._close_time
        
    def get_is_open(self):
        return self._is_open
    

        
        
        
    def __str__(self):
        return "{0} {1} {2} {3} {4} {5} {6} ".format(self._room_id,self._name,self._buliding,self._floor,self._open_time,self._close_time,self._is_open) 
    


class ClassRoom(Room):
    def __init__(self,room_id, name, building, floor,capacity,open_time,close_time,is_open,with_visualizer):
        super().__init__(room_id,name, building, floor, open_time, close_time,is_open)
        self._capacity = capacity
        self._with_visualizer = with_visualizer
        
    def get_capacity(self):
        return self._capacity
    
    def get_with_visualizer(self):
        return self._with_visualizer
    
    def __str__(self):
        return "{0} {1} {2} {3} {4} {5} {6} ClassRoom".format(self._room_id,self._name,self._buliding,self._floor,self._open_time,self._close_time,self._is_open) 

class LabRoom(Room):
    def __init__(self,room_id, name, building, floor,capacity,open_time,close_time, is_open,computer_type):
        super().__init__(room_id,name, building, floor, open_time, close_time,is_open  )
        self._capacity = capacity
        self._computer_type = computer_type    # PC or MAC
        
    def get_capacity(self):
        return self._capacity
    
    def get_computer_type(self):
        return self._computer_type
    def __str__(self):
        return "{0} {1} {2} {3} {4} {5} {6}  Lab".format(self._room_id,self._name,self._buliding,self._floor,self._open_time,self._close_time,self._is_open) 
    
class MeetingRoom(Room):
    def __init__(self,room_id, name, building, floor,capacity,open_time,close_time, is_open,seat_type):
        super().__init__(room_id,name, building, floor,  open_time, close_time,is_open  )
        self._capacity = capacity
        self._seat_type = seat_type   # Y N
  
    def get_capacity(self):
        return self._capacity
    
    def get_seat_type(self):
        return self._seat_type
    
    def __str__(self):
        return "{0} {1} {2} {3} {4} {5} {6} Meeting Room".format(self._room_id,self._name,self._buliding,self._floor,self._open_time,self._close_time,self._is_open) 

    
class Room_list():
    def __init__(self, room_list=[]):
        self._roomlist = []
        
        
        #here
    def load_room_from_db(self):
        db = connect_db()
#    print (db)
        cursor = db.cursor()
#    print (cursor)
        cursor.execute('''SELECT class,room_id,
       name,
       building,
       floor,
       capacity,
       open_time,
       close_time,
       is_open,
       with_visualizer,
       computer_type,
       seat_type
FROM room;
       ''')
        #print('{0:>10} : {1:>30}'.format("ID","Building Name"))

        for row in cursor:
#            print (row)
#            print('{0:>10} : {1:>30}'.format(row[9],row[1]))
            if row[0] == 'C':
                c1 = ClassRoom(room_id=row[1], name =row[2], building=row[3], floor=row[4],capacity=row[5],open_time=row[6],close_time=row[7],is_open=row[8],with_visualizer=row[9])
                self._roomlist.append(c1)
                
            elif row[0] == 'L':
               
                c1 = LabRoom(room_id=row[1], name =row[2], building=row[3], floor=row[4],capacity=row[5],open_time=row[6],close_time=row[7],is_open=row[8],computer_type=row[10])
                self._roomlist.append(c1)
            
            elif row[0] == 'M':
              
                c1 = MeetingRoom(room_id=row[1], name =row[2], building=row[3], floor=row[4],capacity=row[5],open_time=row[6],close_time=row[7],is_open=row[8],seat_type=row[11])
                self._roomlist.append(c1)
            
           

        db.close()
            

    
    def show_rooms(self,roomtype='',sort='id'):
        #self._roomlist.sort(key=lambda r:r.get_name(), reverse=False)
        print(roomtype)
        if roomtype == "ClassRoom":
            a = ClassRoom
        elif roomtype == "LabRoom":
            a = LabRoom  
        elif roomtype == "MeetingRoom":
            a = MeetingRoom    
        else:
            a = ''

        for i in  self._roomlist:
            if a: 
                if isinstance(i, a):
                    print (i)
            else:
                print (i)
                
                
    def show_rooms_table(self,roomtype='all',sort='id'):
      
        room_id_list = []
        
        if roomtype == "C" or roomtype=='all':
            a = ClassRoom
            print ("******** Class Room ********")
            print (" {0:>10}_{1:>10}_{2:>10}_{3:>10}_{4:>10}_{5:>10}_{6:>10}_{7:>10}_{8:>10}".format("_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10))
            print ("|{0:^10}|{1:^10}|{2:^10}|{3:^10}|{4:^10}|{5:^10}|{6:^10}|{7:^10}|{8:^10}|".format("ID","Room","Builing","Floor","Capcity","Open","Close","Visualizer","Open"))
            print ("|{0:>10}|{1:>10}|{2:>10}|{3:>10}|{4:>10}|{5:>10}|{6:>10}|{7:>10}|_{8:>10}".format("_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10))
       
            for i in  self._roomlist:
                if isinstance(i, a):
                    print ("|{0:^10}|{1:^10}|{2:^10}|{3:^10}|{4:^10}|{5:^10.2f}|{6:^10.2f}|{7:^10}|{8:^10}|".format(i.get_room_id(),i.get_name(),i.get_building(),i.get_floor(),i.get_capacity(),i.get_open_time(),i.get_close_time(),i.get_with_visualizer(),i.get_is_open() ) )
                    room_id_list.append(i.get_room_id())
            print ("|{0:>10}|{1:>10}|{2:>10}|{3:>10}|{4:>10}|{5:>10}|{6:>10}|{7:>10}|{8:>10}|\n".format("_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10))
            
        
        
            
        if roomtype == "L" or roomtype=='all':
            b = LabRoom  
            
            print ("******** Lab Room ********")
            print (" {0:>10}_{1:>10}_{2:>10}_{3:>10}_{4:>10}_{5:>10}_{6:>10}_{7:>10}_{8:>10}".format("_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10))
            print ("|{0:^10}|{1:^10}|{2:^10}|{3:^10}|{4:^10}|{5:^10}|{6:^10}|{7:^10}|{8:^10}|".format("ID","Room","Builing","Floor","Capcity","Open","Close","Computer","Open"))
            print ("|{0:>10}|{1:>10}|{2:>10}|{3:>10}|{4:>10}|{5:>10}|{6:>10}|{7:>10}|_{8:>10}".format("_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10))
       
            for i in  self._roomlist:
                if isinstance(i, b):

                    print ("|{0:^10}|{1:^10}|{2:^10}|{3:^10}|{4:^10}|{5:^10.2f}|{6:^10.2f}|{7:^10}|{8:^10}|".format(i.get_room_id(),i.get_name(),i.get_building(),i.get_floor(),i.get_capacity(),i.get_open_time(),i.get_close_time(),i.get_computer_type(),i.get_is_open() ) )
                    room_id_list.append(i.get_room_id())
            print ("|{0:>10}|{1:>10}|{2:>10}|{3:>10}|{4:>10}|{5:>10}|{6:>10}|{7:>10}|{8:>10}|\n".format("_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10))

                    
        if roomtype == "M" or roomtype=='all':
            c = MeetingRoom  

            print ("******** Meeting Room ********")
            print (" {0:>10}_{1:>10}_{2:>10}_{3:>10}_{4:>10}_{5:>10}_{6:>10}_{7:>10}_{8:>10}".format("_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10))
            print ("|{0:^10}|{1:^10}|{2:^10}|{3:^10}|{4:^10}|{5:^10}|{6:^10}|{7:^10}|{8:^10}|".format("ID","Room","Builing","Floor","Capcity","Open","Close","Fixed Seat","Open"))
            print ("|{0:>10}|{1:>10}|{2:>10}|{3:>10}|{4:>10}|{5:>10}|{6:>10}|{7:>10}|_{8:>10}".format("_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10))
  
            for i in  self._roomlist:
                if isinstance(i, c):

                    print ("|{0:^10}|{1:^10}|{2:^10}|{3:^10}|{4:^10}|{5:^10.2f}|{6:^10.2f}|{7:^10}|{8:^10}|".format(i.get_room_id(),i.get_name(),i.get_building(),i.get_floor(),i.get_capacity(),i.get_open_time(),i.get_close_time(),i.get_seat_type(),i.get_is_open() ) )
                    room_id_list.append(i.get_room_id())
            print ("|{0:>10}|{1:>10}|{2:>10}|{3:>10}|{4:>10}|{5:>10}|{6:>10}|{7:>10}|{8:>10}|\n".format("_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10))
            
        return room_id_list
    
    
    
    def show_open_rooms_table(self,open_time,close_time,roomtype='all'):
      
        room_id_list = []
        
        if roomtype == "C" or roomtype=='all':
            a = ClassRoom
            print ("******** Class Room ********")
            print (" {0:>10}_{1:>10}_{2:>10}_{3:>10}_{4:>10}_{5:>10}_{6:>10}_{7:>10}_{8:>10}".format("_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10))
            print ("|{0:^10}|{1:^10}|{2:^10}|{3:^10}|{4:^10}|{5:^10}|{6:^10}|{7:^10}|{8:^10}|".format("ID","Room","Builing","Floor","Capcity","Open","Close","Visualizer","Open"))
            print ("|{0:>10}|{1:>10}|{2:>10}|{3:>10}|{4:>10}|{5:>10}|{6:>10}|{7:>10}|_{8:>10}".format("_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10))
       
            for i in  self._roomlist:
                
                if  (float(i.get_open_time()) > float(open_time))  or ( float(close_time) > float(i.get_close_time()) ):
                    pass
                else:
                    if isinstance(i, a):
                        print ("|{0:^10}|{1:^10}|{2:^10}|{3:^10}|{4:^10}|{5:^10.2f}|{6:^10.2f}|{7:^10}|{8:^10}|".format(i.get_room_id(),i.get_name(),i.get_building(),i.get_floor(),i.get_capacity(),i.get_open_time(),i.get_close_time(),i.get_with_visualizer(),i.get_is_open() ) )
                        room_id_list.append(i.get_room_id())
            print ("|{0:>10}|{1:>10}|{2:>10}|{3:>10}|{4:>10}|{5:>10}|{6:>10}|{7:>10}|{8:>10}|\n".format("_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10))
            
        
        
            
        if roomtype == "L" or roomtype=='all':
            b = LabRoom  
            
            print ("******** Lab Room ********")
            print (" {0:>10}_{1:>10}_{2:>10}_{3:>10}_{4:>10}_{5:>10}_{6:>10}_{7:>10}_{8:>10}".format("_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10))
            print ("|{0:^10}|{1:^10}|{2:^10}|{3:^10}|{4:^10}|{5:^10}|{6:^10}|{7:^10}|{8:^10}|".format("ID","Room","Builing","Floor","Capcity","Open","Close","Computer","Open"))
            print ("|{0:>10}|{1:>10}|{2:>10}|{3:>10}|{4:>10}|{5:>10}|{6:>10}|{7:>10}|_{8:>10}".format("_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10))
       
            for i in  self._roomlist:
                
                if  (float(i.get_open_time()) > float(open_time))  or ( float(close_time) > float(i.get_close_time()) ):
                    pass
                else:
                    if isinstance(i, b):
    
                        print ("|{0:^10}|{1:^10}|{2:^10}|{3:^10}|{4:^10}|{5:^10.2f}|{6:^10.2f}|{7:^10}|{8:^10}|".format(i.get_room_id(),i.get_name(),i.get_building(),i.get_floor(),i.get_capacity(),i.get_open_time(),i.get_close_time(),i.get_computer_type(),i.get_is_open() ) )
                        room_id_list.append(i.get_room_id())
            print ("|{0:>10}|{1:>10}|{2:>10}|{3:>10}|{4:>10}|{5:>10}|{6:>10}|{7:>10}|{8:>10}|\n".format("_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10))

                    
        if roomtype == "M" or roomtype=='all':
            c = MeetingRoom  

            print ("******** Meeting Room ********")
            print (" {0:>10}_{1:>10}_{2:>10}_{3:>10}_{4:>10}_{5:>10}_{6:>10}_{7:>10}_{8:>10}".format("_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10))
            print ("|{0:^10}|{1:^10}|{2:^10}|{3:^10}|{4:^10}|{5:^10}|{6:^10}|{7:^10}|{8:^10}|".format("ID","Room","Builing","Floor","Capcity","Open","Close","Fixed Seat","Open"))
            print ("|{0:>10}|{1:>10}|{2:>10}|{3:>10}|{4:>10}|{5:>10}|{6:>10}|{7:>10}|_{8:>10}".format("_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10))
  
            for i in  self._roomlist:
                if  (float(i.get_open_time()) > float(open_time))  or ( float(close_time) > float(i.get_close_time()) ):
                    pass
                else:
                    if isinstance(i, c):
    
                        print ("|{0:^10}|{1:^10}|{2:^10}|{3:^10}|{4:^10}|{5:^10.2f}|{6:^10.2f}|{7:^10}|{8:^10}|".format(i.get_room_id(),i.get_name(),i.get_building(),i.get_floor(),i.get_capacity(),i.get_open_time(),i.get_close_time(),i.get_seat_type(),i.get_is_open() ) )
                        room_id_list.append(i.get_room_id())
            print ("|{0:>10}|{1:>10}|{2:>10}|{3:>10}|{4:>10}|{5:>10}|{6:>10}|{7:>10}|{8:>10}|\n".format("_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10))
            
        return room_id_list
    
    
    
                
    def show_all_room(self,sort='id'):
        #self._roomlist.sort(key=lambda r:r.get_name(), reverse=False)

        for i in  self._roomlist:
           print(type(i))
           print (i)
            
            
    
    def add_room(self,room):
        self._roomlist.append(room)
        
    def is_open(self,room_id,from_time,to_time):
        result = True
        print(room_id,from_time,to_time)
        print ('*'*5)
        for i in self._roomlist:
            print (i.get_room_id(),i.get_open_time(),i.get_close_time())
           
            if i.get_room_id() == room_id:
                print ("yes room")
                if  (float(i.get_open_time()) > float(from_time))  or ( float(to_time) > float(i.get_close_time()) ):
                    print ("Error")
                    print (i.get_room_id(),i.get_open_time(),i.get_close_time())
                    result = False
                    
        return result
        

class Reservation():
    def __init__(self,reservation_id,user_name,room_id,date,from_time,to_time,detail,status):
        self._reservation_id = reservation_id
        self._user_name = user_name
        self._room_id = room_id
        self._date = date
        self._from_time = from_time
        self._to_time = to_time
        self._detail = detail
        self._status = status 
        
    def get_reservation_id(self):
        return self._reservation_id
    
    def get_username(self):
        return self._user_name
    
    def get_room_id(self):
        return self._room_id
    
    def get_date (self):
        return self._date
    
    def get_from_time(self):
        return self._from_time
    
    def get_to_time(self):
        return self._to_time
    
    def get_detail(self):
        return self._detail
    
    def get_status(self):
        return self._status
    
    def __str__(self):
        return "{0} {1} {2} {3} {4} {5} {6} {7}".format(self._reservation_id,self._user_name,self._room_id,self._date,self._from_time,self._to_time,self._detail,self._status) 
        
class Reservation_list():
    def __init__(self,r_list=[]):
        self._r_list = []
        
    def add_reservation(self,reservation):
        self._r_list.append(reservation)
        
    def load_reservation_from_db(self):
        db = connect_db()
#    print (db)
        cursor = db.cursor()
#    print (cursor)
        cursor.execute('''SELECT reservation_id,
       user_name,
       room_id,
       date,
       from_time,
       to_time,
       detail,
       status
       FROM reservation order by status,date,from_time;

       ''')
        #print('{0:>10} : {1:>30}'.format("ID","Building Name"))
        
        for row in cursor:
            r1 = Reservation(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
            self._r_list.append(r1)
        
        
    def show_reservation(self,sort='id'):
        #self._r_list.sort(key=lambda r:r.get_from_time(), reverse=False)
        reservation_id_list = []
        print (" ***** All Reservation *******")
        print (" {0:>10}_{1:>10}_{2:>10}_{3:>10}_{4:>10}_{5:>10}_{6:>10}_{7:>10}".format("_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10))
        print ("|{0:^10}|{1:^10}|{2:^10}|{3:^10}|{4:^10}|{5:^10}|{6:^10}|{7:^10}|".format("ID","user","Room","date","From","To","Detail","Status"))
        print ("|{0:>10}|{1:>10}|{2:>10}|{3:>10}|{4:>10}|{5:>10}|{6:>10}|{7:>10}|".format("_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10))
        for i in  self._r_list:
            print ("|{0:>10}|{1:>10}|{2:>10}|{3:>10}|{4:>10.2f}|{5:>10.2f}|{6:>10}|{7:>10}|".format(i.get_reservation_id(),i.get_username(),i.get_room_id(),i.get_date(),i.get_from_time(),i.get_to_time(),i.get_detail(),i.get_status()))
            reservation_id_list.append(i.get_reservation_id())
        print ("|{0:>10}|{1:>10}|{2:>10}|{3:>10}|{4:>10}|{5:>10}|{6:>10}|{7:>10}|".format("_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10))
        return reservation_id_list

    def show_waiting_reservation(self):
        waiting_list = []
        print (" ***** Reservation Waiting For Approve*******")
        print (" {0:>10}_{1:>10}_{2:>10}_{3:>10}_{4:>10}_{5:>10}_{6:>10}_{7:>10}".format("_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10))
        print ("|{0:^10}|{1:^10}|{2:^10}|{3:^10}|{4:^10}|{5:^10}|{6:^10}|{7:^10}|".format("ID","user","Room","date","From","To","Detail","Status"))
        print ("|{0:>10}|{1:>10}|{2:>10}|{3:>10}|{4:>10}|{5:>10}|{6:>10}|{7:>10}|".format("_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10))
        for i in  self._r_list:
            if i.get_status() == "Waiting":
                print ("|{0:>10}|{1:>10}|{2:>10}|{3:>10}|{4:>10.2f}|{5:>10.2f}|{6:>10}|{7:>10}|".format(i.get_reservation_id(),i.get_username(),i.get_room_id(),i.get_date(),i.get_from_time(),i.get_to_time(),i.get_detail(),i.get_status()))
                waiting_list.append(i.get_reservation_id())
        print ("|{0:>10}|{1:>10}|{2:>10}|{3:>10}|{4:>10}|{5:>10}|{6:>10}|{7:>10}|".format("_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10,"_"*10))
        
        return waiting_list
    
    def return_list(self):
        return self._r_list
    
    
    
    
    
    def is_available(self,room_id,date,from_time,to_time):
        result = True
        print(room_id,date,from_time,to_time)
        for i in self._r_list:
           
            if i.get_room_id() == str(room_id) and str(date) == str(i.get_date()):
                print ("yes date")
                if  (float(i.get_from_time()) < float(from_time) < float(i.get_to_time())) or (float(i.get_from_time()) < float(to_time) < float(i.get_to_time())) :
                    print ("Error")
                    print (i.get_room_id() ,i.get_date() ,i.get_from_time(),i.get_to_time())
                    result = False
                    
        return result
            
                
        
        
        
        
            
            
            

def connect_db():
    try:
        # Creates or opens a file called mydb with a SQLite3 DB
        db = sqlite3.connect('ers.db')

    # Catch the exception
    except Exception as e:
        # Roll back any change if something goes wrong
        db.rollback()
        raise e
        
    #finally:
        # Close the db connection
        #db.close()
    return db
        


def show_building():
    db = connect_db()
#    print (db)
    cursor = db.cursor()
#    print (cursor)
    cursor.execute('''SELECT id, name FROM building''')
    print('{0:>10} : {1:>30}'.format("ID","Building Name"))
    for row in cursor:
        print('{0:>10} : {1:>30}'.format(row[0], row[1]))
    db.close()

def add_new_building():
    while True:
        print ("Add New Building")
        input_building_name = input("Enter Building Name:")
        try:
            db = connect_db()
            cursor = db.cursor()
            cursor.execute('''INSERT INTO building(name) VALUES(?)''', [input_building_name])
            print (input_building_name," is added")
            db.commit()
            break
        except sqlite3.IntegrityError:
            print('Record already exists')
            continue
        except Exception as e:
            print (e)
            raise e
            
            
        finally:
            db.close()
    show_menu_admin()
            
def delete_building():
    while True:
        print ("Delete a  Building  chose from List:")
        show_building()
        
        input_building_name = input("Enter build name to Delete:")
        try:
            db = connect_db()
            cursor = db.cursor()
#            cursor.execute('''INSERT INTO building(name)VALUES(?)''', (input_building_name))
            cursor.execute('''DELETE FROM building WHERE name = ? ''', [input_building_name])
            deleted_row_count = cursor.rowcount

            print (deleted_row_count)
            if deleted_row_count == 1 :
                print (input_building_name," is Deleted")
                db.commit()
            else:
                print (input_building_name, "is Not Found!!  Please Try Again")
            break
       
        except Exception as e:
            print (e)
            raise e
            
        finally:
            db.close()
 

def add_room():
    while True:
        print ("Add New Room")
        print ("C for Class room")
        print ("M for Meeting room")
        print ("L for Laboratary room")
        input_room_type = input("Enter Room type   ( C,M,L) :")
        if input_room_type.upper() in ('C','M','L') : 
            input_room_name = input("Enter Room name:")
            input_building_name = input("Enter Building Name:")
            input_floor = input("Enter Floor:")

            input_capacity = int(input("Enter Capacity:"))
            input_open_time = input("Enter Open Time (24hrs format ex. 9.00):")
            input_close_time = input("Enter Close Time (24hrs format ex. 17.30):")
            
            if input_room_type.upper() == "C":
                input_with_visualizer = input("is this room has a visualizer? (Y or N):")
#                classroom1 = ClassRoom(room_id=1, name=input_room_name, building=input_building_name, floor=input_floor,capcity=input_room_capacity,open_time=input_open_time,close_time=input_close_time,with_visualizer=input_with_visualizer)
                classroom1 = ClassRoom(room_id='1',name=input_room_name,building=input_building_name,floor=input_floor,capacity=input_capacity,open_time=input_open_time,close_time=input_close_time,is_open='Y',with_visualizer=input_with_visualizer)
                sql = '''INSERT INTO room (name,building,floor,capacity,open_time,close_time,with_visualizer,is_open,class) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')'''.format(input_room_name,input_building_name,input_floor,input_capacity,input_open_time,input_close_time,input_with_visualizer,'Y',input_room_type.upper())
                print (sql)

                print (input_room_name, "is Added")    
                print (classroom1)
                
                
            if input_room_type.upper() == "L":
                input_computer_type = input("What Computer in this Lab ? (PC or MAC):")
#                classroom1 = ClassRoom(room_id=1, name=input_room_name, building=input_building_name, floor=input_floor,capcity=input_room_capacity,open_time=input_open_time,close_time=input_close_time,with_visualizer=input_with_visualizer)
                classroom1 = LabRoom(room_id='1',name=input_room_name,building=input_building_name,floor=input_floor,capacity=input_capacity,open_time=input_open_time,close_time=input_close_time,is_open='Y',computer_type=input_computer_type)
               
                sql = '''INSERT INTO room (name,building,floor,capacity,open_time,close_time,computer_type,is_open,class) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')'''.format(input_room_name,input_building_name,input_floor,input_capacity,input_open_time,input_close_time,input_computer_type,'Y',input_room_type.upper())
                print (sql)

                
                print (input_room_name, "is Added")    
                print (classroom1)
                
                
                
            if input_room_type.upper() == "M":
                input_seat_type = input("Is fixed seat?  Y or N):")
#                classroom1 = ClassRoom(room_id=1, name=input_room_name, building=input_building_name, floor=input_floor,capcity=input_room_capacity,open_time=input_open_time,close_time=input_close_time,with_visualizer=input_with_visualizer)
                classroom1 = MeetingRoom(room_id='1',name=input_room_name,building=input_building_name,floor=input_floor,capacity=input_capacity,open_time=input_open_time,close_time=input_close_time,is_open='Y',seat_type=input_seat_type)
               
                sql = '''INSERT INTO room (name,building,floor,capacity,open_time,close_time,seat_type,is_open,class) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')'''.format(input_room_name,input_building_name,input_floor,input_capacity,input_open_time,input_close_time,input_seat_type,'Y',input_room_type.upper())
                print (sql)

                
                print (input_room_name, "is Added")    
                print (classroom1)
        else:
            continue
            
        
        try:
            db = connect_db()
            cursor = db.cursor()



            cursor.execute(sql)
            print (input_room_name," is added")
            db.commit()
            db.close()

             
            print ("ADDEDDD")
            break
        
        except sqlite3.IntegrityError:
            print('Record already exists')
            continue
        except Exception as e:
            print (e)
            raise e
            
            
        finally:
            db.close()
            
    show_menu_admin()
    

def show_room(roomtype):
    
    room1 = Room_list()
    room1.load_room_from_db()
    room1.show_rooms_table(roomtype)

def delete_room():
    while True:
        print ("Delete a  Room chose from List:")
        
        
        input_room_id = input("Enter room ID to Delete:")
        try:
            db = connect_db()
            cursor = db.cursor()
#            cursor.execute('''INSERT INTO building(name)VALUES(?)''', (input_building_name))
            cursor.execute('''DELETE FROM room WHERE room_id = ? ''', [input_room_id])
            deleted_row_count = cursor.rowcount

            print (deleted_row_count)
            if deleted_row_count == 1 :
                print (input_room_id," is Deleted")
                db.commit()
            else:
                print (input_room_id, "is Not Found!!  Please Try Again")
            break
       
        except Exception as e:
            print (e)
            raise e
            
        finally:
            db.close()


def show_reservation():
    r1 = Reservation_list()
    r1.load_reservation_from_db()
    r1.show_reservation()
    
def make_reservation():           
    while True:
        print ("Make Reservation:")
        print ("C for Class room")
        print ("M for Meeting room")
        print ("L for Laboratary room")
        input_room_type = input("Enter Room type   ( C,M,L) :")
        input_room_type = input_room_type.upper()
        if input_room_type.upper() in ('C','M','L','') :
            if input_room_type == '':
                break
            
            
            while True:
                try:
                    input_from_time = float(input("Enter from Time (24hrs format ex. 9.00):"))
                    input_to_time = float(input("Enter to Time (24hrs format ex. 17.00):"))
                    if input_from_time >= input_to_time :
                        print ("From time must less than to time")
                        continue
                    else:
                        break
                except:
                    print ("Plase check you Time Format again")
                    continue
            
#            open_check = Room_list()
#            open_check.load_room_from_db()
#            is_open_result = open_check.is_open(input_room_id,input_from_time,input_to_time)
#            if is_open_result is False:
#                print ("*"*50)
#                print ("Time you choose is not open!!")
#                print ("Please Choose new time")
#                print ("*"*50)
#                continue
#            
            
            
            
            
            while True:
                try:
                    aa = Room_list()
                    aa.load_room_from_db()
                    #room_id_list = aa.show_rooms_table(input_room_type.upper())
                    room_id_list = aa.show_open_rooms_table(input_from_time,input_to_time,roomtype=input_room_type)
                    if len(room_id_list) > 0:
                        print (room_id_list)
                    else:
                        print ("*"*50)
                        print ("No open Room Found!  Please try again")
                        print ("*"*50)
                        make_reservation()
                    input_room_id = int(input("Enter Room ID for Reserve :"))
                    if input_room_id in room_id_list:
                        break
                    else:
                        print ("Please choose room ID ")
                        continue
                except:
                    print ("Please Enter Room ID")
                    continue
            
            
            
            
            
            
            input_date = input("Enter Date: dd/mm/yyyy:")
            
            a_check = Reservation_list()
            a_check.load_reservation_from_db()
            is_avaible_result = a_check.is_available(input_room_id,input_date,input_from_time,input_to_time)
            if is_avaible_result is False:
                print ("*"*50)
                print ("Time you choose is not availble!!")
                print ("Please Choose new time")
                print ("*"*50)
                continue
            
            input_username = input("Enter Your name:")
            input_detail = input("Enter Detail:")
            
            sql = '''INSERT INTO reservation (user_name,room_id,date,from_time,to_time,detail,status)  VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}')'''.format(input_username,input_room_id,input_date,input_from_time,input_to_time,input_detail,'Waiting')
            print (sql)
            print (input_username, "is Added")    

        else:
            continue
            
        
        try:
            db = connect_db()
            cursor = db.cursor()



            cursor.execute(sql)
            print (input_username," is added")
            db.commit()
            db.close()

             
            print ("ADDEDDD")
            break
        
        except sqlite3.IntegrityError:
            print('Record already exists')
            continue
        except Exception as e:
            print (e)
            raise e
            
            
        finally:
            db.close()
 

def approve_reservation():
    rw1 = Reservation_list()
    rw1.load_reservation_from_db()
    waiting_list_id = rw1.show_waiting_reservation()
    print (waiting_list_id)

    while True:
        print ("Approve Reservation :")
        
        input_reservation_id = int(input("Enter Reservaion ID to Approve :"))
        if input_reservation_id == '':
            break
        
        if input_reservation_id in waiting_list_id : 
            print ("Found")
            sql = '''UPDATE reservation Set status = '{0}' WHERE reservation_id ={1} '''.format('Approved',input_reservation_id)
            print (sql)
            print (input_reservation_id, "is Approved")    

        else:
            print ("ID not Found!!")
            continue
            
        
        try:
            db = connect_db()
            cursor = db.cursor()

            print (sql)

            cursor.execute(sql)
            print (input_reservation_id," is approve")
            db.commit()
            db.close()
            break
        
        except sqlite3.IntegrityError:
            print('Record already exists')
            continue
        except Exception as e:
            print (e)
            raise e
            
            
        finally:
            db.close()    


def cancel_reservation():

    rc1 = Reservation_list()
    rc1.load_reservation_from_db()
    cancel_list_id = rc1.show_reservation()
    print (cancel_list_id)

    while True:
        print ("Cancel Reservation :")
        
        input_cancel_id = int(input("Enter Reservaion ID to Cancel :"))
        if input_cancel_id == '':
            break
        
        if input_cancel_id in cancel_list_id : 
            print ("Found")
            sql = '''UPDATE reservation Set status = '{0}' WHERE reservation_id ={1} '''.format('Cancel',input_cancel_id)
            print (sql)
            print (input_cancel_id, "is Cancel")    

        else:
            print ("ID not Found!!")
            continue
            
        
        try:
            db = connect_db()
            cursor = db.cursor()

            print (sql)

            cursor.execute(sql)
            print (input_cancel_id," is Cancel")
            db.commit()
            db.close()
            break
        
        except sqlite3.IntegrityError:
            print('Record already exists')
            continue
        except Exception as e:
            print (e)
            raise e
            
            
        finally:
            db.close()    

     
def show_menu():
    while True:
        try:
            who = input("You are Admin or User? :")
            if who.upper() == 'ADMIN':
                show_menu_admin()
                break
            elif who.upper() == "USER":
                show_menu_user()
                break
            elif who.upper() == "EXIT":
                print (" Bye Bye  See you Again!!")
                quit()

                break
            else:
                print ("Please Select !!  ")
                continue
                
        except:
            continue    
def show_menu_admin():
    print ("Menu admin")
    print ("0: Show Menu")
    print ("************ Building **********")
    print("1: Show Building")
    print("2: Add New Building")
    print("3: Delete Building")
    print ("************ Room**********")
    print("4: List All Room")
    print("5: Add New Room")
    print("6: Delete Room")
    print ("************ Reservation **********")
    print ("7: Show All Reservation")
    print ("8: Approve Reservation")
    print("Exit: To Exit")
    
    while True:
        try:
            admin_choice = input("select choice from menu ( 0 for menu):")
            if admin_choice == '2':
                print (admin_choice)
                add_new_building()
                break
            elif admin_choice.upper() == "0":
                show_menu_admin()
            elif admin_choice.upper() == "1":
                show_building()    
            elif admin_choice.upper() == "2":
                add_new_building()   
            elif admin_choice.upper() == "3":
                delete_building()
            elif admin_choice.upper() == "4":
                show_room('all')
            elif admin_choice.upper() == "5":
                add_room()
            elif admin_choice.upper() == "6":
                delete_room()
            elif admin_choice.upper() == "7":
                show_reservation()
            elif admin_choice.upper() == "8":
                approve_reservation()
            elif admin_choice.upper() == "EXIT":
                show_menu()
                break

            else:
                print (" Invalid opition!!")
                continue
                
        except:
            continue

def show_menu_user():
    print ("Menu : User")
    print ("0: Show Menu")
    print ("************ Room**********")
    print("1: List Class Room")
    print ("2: List Meeting Room")
    print ("3: List Lab ")
    print ("************ **********")
    print("4: List Reservation")
    print("5: Make Reservaion")
    print("6: Cancel Reservation")
    print("Exit: To Exit")
    
    while True:
        try:
            user_choice = input("select choice from menu ( 0 for menu):")
            if user_choice == '0':
                show_menu_user()
            elif user_choice == '1':
                show_room('C')
            elif user_choice == '2':
                show_room('M')
            elif user_choice == '3':
                show_room('L')
            elif user_choice.upper() == "4":
                show_reservation()
            elif user_choice.upper() == "5":
                make_reservation()
            elif user_choice.upper() == "6":
                cancel_reservation()

            elif user_choice.upper() == "EXIT":
                show_menu()
                break

            else:
                print (" Invalid opition!!")
                continue
                
        except:
            continue


def show_banner():
    print ('*'*50)
    print ("*         Electronic Reservation System           *")
    print ('*'*50)

def main():

    show_banner()
    show_menu()
#    r111 = Room_list()
#    r111.load_room_from_db()
#    a = r111.show_open_rooms_table('8.00','12.00')
#    print (a)
   



main()        
    
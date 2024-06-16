from datetime import date

class Student:
    def __init__(self,idd,name,dob,classification):
        self.__id=idd
        self.__name=name
        self.__dob=dob
        self.__classification=classification 
        self.__age=0
        self.__register=''

    

def get_age(self):
    return self.__age

def get_registration(self):
    return self.__register


def calc_age(self):
    today=date.today()
    dob=self.__dob.split('/')
    dob_year=int(dob[2])
    age=today.year - dob_year
    self.__age=age

def register(self):
    if self.__classification=='senior':
        self.__register = '11/1 thru 11/3'
    #keep doing elifs


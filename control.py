from os import system
from model import *
from view import *


def weight(inputWeight):
    """
    This function check rightness of weight that you write
    :param inputWeight:weight that you write
    :return:weight
    """
    if(inputWeight>160 or inputWeight==0):
       system('clear')
       incorrect_view("weight")
       inputWeight=addWeight()
       weight(inputWeight)
    else:return inputWeight

def height(inputHeight):
    """
    This function check rightness of height that you write
    :param inputHeight:height that you write
    :return:height
    """
    if(inputHeight>250 or inputHeight==0):
       system('clear')
       incorrect_view("height")
       inputWeight=addHeight()
       height(inputHeight)
    else:return inputHeight


def age(inputAge):
    """
    This function check rightness of age that you write
    :param inputAge:age that you write
    :return:age
    """
    if(inputAge>110 or inputAge==0):
       system('clear')
       incorrect_view("age")
       inputWeight=addAge()
       age(inputAge)
    else:return inputAge

def count():
    """
    Function that use function from model and return number f callories
    :return:callories
    """
    enter_view("weight")
    Weight=weight(input())
    enter_view("height")
    Height=height(input())
    enter_view("age")
    Age=age(input())
    view_nWeekTreinings()
    Input=input()
    factor=chooseNumberOfT(Input)
    rez=calculation(Weight,Height,Age,factor)
    return rez

def menu_listener():
    """
    This function run view functions and print on the screen callories
    :return:
    """
    last=0
    while(True):
        view_menu()
        Input=input()
        if Input==1:
            system('clear')
            rz=count()
            last=rz
            print "Quantity-",rz
            view_1menu()
            Input=input()
            if Input==2:
                system('clear')
                exit(0)
        elif Input==2:
            system("clear")
            exit(0)
        else:print "Choose correct line"
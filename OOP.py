# -*- coding: utf-8 -*-
"""
Created on Tue Jul 04 01:36:11 2017

@author: Paul

Abstraction
Encapsulation
Inheritance
Polymorphism

"""

class Mobile():
    #class variable 
    numberOfInstances = 0

    def  __init__(self,IEMICode,SIMCard,Processor,InternalMemory,IsSingleSim=True):
         '''illuistration fo encaspulation by declaying IEMICode private'''
         self.__IEMICode = IEMICode #private variable
         self.simCard= SIMCard
         self.processor =Processor
         self.internalMemory = InternalMemory
         self.isSingleSim = IsSingleSim
         Mobile.numberOfInstances +=1
         
    def __del__(self):
        print "Destructor started"
        Mobile.numberOfInstances -=1
            
    def  getIEMICode(self):# getter method for the private variable
        print("The Mobile IEMICode is: {}".format(self.IEMICode))
        return self.IEMICode
        ''' Every Mobile phone can dial ,receive calls and send message'''
    def  dial(self):
        print("Dialing Number...")
        
    def  recieveCall(self):
        print("Receiving Call...")
        
      #Abstration illustration :that's use of methods and functions,So one just call this method ''' 
    def  sendMessage(self):
        print("Want to send message\n")
        receiverNumber = input("Input receiver's number(s):")
        messageToSend = input("Write your message here:")
        print("Message sent\n")
        print("To:{} \n Message:{}".format(receiverNumber,messageToSend))
        
''' Samsung has propeties of a Mobile phnoe: Illustration of Inheritance'''        
class Samsung(Mobile):
  #instance methods for Samsung,for it can connect to wifi and has camera but not all Mobile phones have"""
    def GetWIFIConnection(self):
        print("connected to wifi")
        
    ''' static polymorphism '''
    #This is one method which shows camera functionality  
    def  CameraClick(self):
        print("Camera clicked")
  
    #This is one overloaded method which shows camera functionality as well but with its camera's different mode(panaroma)  
    def  CameraClick(self,cameraMode):
        print ("Camera clicked in " + cameraMode + " Mode");  
        
''' Nokia is a Mobile phone: Illustration of Inheritance'''  
        
class Nokia (Mobile):
  #insatnce methods for Nokia  
    def GetBlueToothConnection(self):
         print("Bluetooth connected")  
         
    ''' Dynamic polymorphism '''
     #New implementation for this method which was available in Mobile Class  
     #This is runtime polymorphism  
    #May be Nokia is able to send multiple messages at once
    def  sendMessage(self):
        print("Want to send message\n")
        receiverNumber = [07889878,07566898,070133656]
        messageToSend = input("Write your message here:")
        
        for person in receiverNumber:
            print("Message sent\n")
            print("To:{} \n Message:{}".format(person,messageToSend))
      
    

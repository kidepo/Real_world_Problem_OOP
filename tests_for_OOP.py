# -*- coding: utf-8 -*-
"""
Created on Tue Jul 04 03:41:33 2017

@author: Paul
"""

import unittest

from OOP import Mobile,Samsung,Nokia

class MobileTestCases(unittest.TestCase):
  def setUp(self):
    self.phone = Mobile("IMEI1234","MTN","2 cores","8 GB",IsSingleSim=True)
    self.samsungPhone=Samsung("IMEI1234","MTN","2 cores","16 GB",IsSingleSim=False)
    self.nokia=Nokia("IMEI1235","Airtel","","32 MB",IsSingleSim=True)
  def tearDown(self):
    del self.phone

    
  def test_instance_Mobile(self):
    self.assertTrue(isinstance(self.phone, Mobile), msg='CurrentAccount is not a subclass of BankAccount')
  
  def test_Access_of_variablesFor_Mobile1(self):
    _processor = self.phone.processor
    self.assertEquals(_processor, "2 cores")
    

    
  def test_Polymorphism_Methods (self):
     self.assertEquals(self.samsungPhone.CameraClick("Paranoma"), "capture")
     
  def test_No_of_Instances_created(self):
    instanceNum = Mobile.numberOfInstances
    self.assertEquals(instanceNum, 5)
    
# test if it throughs error on acces of private variable
  def test_Encaspulation(self):
    _IEMICode = self.phone.IEMICode
    self.assertEquals(_IEMICode, "IMEI1234")

  def test_inherentece (self):
      memory = self.nokia.internalMemory
      self.assertEquals(memory, "32 MB")
      
  def test_abstraction(self):
      thisMethod = self.nokia.sendMessage()# test whether its collable
      self.assertEquals(thisMethod, True)
    
if __name__ == '__main__':
  unittest.main()

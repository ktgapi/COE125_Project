# -*- coding: utf-8 -*-
import unittest
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Login import Log_In
from SignUp import Sign_Up
import resources
from datalogic import DataLogic
import sqlite3


class TestLogin(unittest.TestCase):
    
    dl = DataLogic()
    
    
    def test_UserCheck(self):
        #Test areas  if the login if functioning
        self.assertEqual(Log_In.UserCheck(self,"Pedro"), False)
        self.assertEqual(Log_In.UserCheck(self,"User1"), True)
        self.assertEqual(Log_In.UserCheck(self,123), False)
        self.assertFalse(Log_In.UserCheck(self,-1))
        
        
        
        
    
# -*- coding: utf-8 -*-
import unittest
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Login import Log_In
from SignUp import Sign_Up
from datalogic import DataLogic
import resources
import sqlite3

class SignUpTest(unittest.TestCase):
    dl = DataLogic()
        
    def UserCheckTest(self):
        #test functionality of user check in signup
        self.assertEqual(Sign_Up.UserCheck(self,"User1"), True)
        self.assertEqual(Sign_Up.UserCheck(self,"TEST"), False)
        self.assertEqual(Sign_Up.UserCheck(self, ""), False)
        
if __name__ == '__main__':
    unittest.main()
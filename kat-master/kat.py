# ----------------------------------------------------------------
import os
import sys
import time 
from pathlib import Path

get_tools =os.path.abspath('tools-kat')
sys.path.insert(0, get_tools)
kat_remove =os.path.abspath('')



import katselect
#------------------------------------------------------------------
num_b = ('')
exit = (['exit','exit '])
help = (['kat','kat '])
he = open('help.txt','r')
#-----------------------------------------------------------------
class select2:
      def se2():
          os.system('clear')
          list = open('tools-list.txt','r')
          print ('\033[1;33;40m'+list.read()+'\033[1;37;40m')
          list.close()
          while True:
                   try:
                      sele = input('== > Tool [] : ')
                      if sele in exit :
                           os.system('clear')
                           break
                      else :
                           pass
                      try: 
                          se = katselect.data[int(sele)]
                      except KeyError:
                          se = katselect.data2[int(sele)]
                      print ('==== > Tool : '+se+'\n------------------------------')
                      if 'python3' in se:
                          python = ('python3')
                      else :
                          python = ('python')
                      while True : 
                          try:
                              command = input ('\033[1;33;40m====== > '+python+' '+get_tools+'/'+se+' '+'\033[1;37;40m')
                              os.system(python+' '+get_tools+'/'+se+' '+command)   
                          except :
                              os.system('clear')
                              sys.exit()
                   except:
                     os.system('clear')
                     select2.se2()
                   break
                              
        
          kat.select() 
class kat:
      def banner():
          os.system('clear')
          print ('\033[1;32;40m      +---------------------------------------------------------+')
          print ('      |      KAT MASTER | Version : 1.0 | Author : IT Sat       |')
          print ('      +---------------------------------------------------------+')
          print ('       \      |    Year : 2018    [ open source ]   |         /')
          print ('        +-------------------------------------------------  -+')
          print ('        |           https://itsat1728.blogspot.com          |')
          print ('        +---------------------------------------------------+')
          print ('         \      | Only for Linux [ Termux - Linux ] |      /')
          print ('          +-----------------------------------------------+')
    
          kat.select()
      def select():
          
          print ('\033[1;35;40m')
          print ('                 +--------------------------------+')
          print ('                 | SELCET ONE NUMBER TO CONTIUE ! |')
          print ('                 +--------------------------------+')
          print ('')
          print ('    +---------+  +--------+  +----+  +----------+  +----------+')
          print ('    |1. About |--|2. Menu |--| :3 |--| 4. Check |--| 5. Reset |')
          print ('    +---------+  +--------+  +----+  +----------+  +----------+')
          print ('')
          print ('+---------+  +---------+  +-------------+  +---------+  +---------+')
          print ('| 6. [][] |--|7. Update|--|8. Remove Kat|--| 9. Bugs |--| 10. Exit|')
          print ('+---------+  +---------+  +-------------+  +---------+  +---------+\033[1;37;40m')
          number_n.number()
class number_n:
      def number():
        while True :
          num_b = input ('==> Select : ')
          if num_b == '10' :
             os.system('clear')
             print ('====> { [ Your select : '+num_b+ ' ] == > Sys.exit()  }')
             print (' [ Bye Bye ] ')
             print (' Kat Master - https://itsat1728.blogspot.com ')
             sys.exit()
             
          elif num_b == '9':
             os.system('clear')
             print ('==== > { [ Your select : '+num_b+ ' ]}')
             print ('[ ! ] if you find bugs in my tool. Contact  : sat_1728@outlook.com. Thanks. [ ! ]')
             input ('| Enter to contiue ! |')
             os.system('clear')
             kat.select() 
          elif num_b == '8':
             os.system('clear')
             print ('Del Kat-Master')
             os.system('rm -rf '+kat_remove)
             os.system('clear')
             print ('Thanks you for using my tool [ Kat-master ][ https://itsat1728.blogspot.com ]')
             sys.exit()    
          elif num_b == '7':
             os.system('clear')
             print ('==== > { [ Your select : '+num_b+ ' ]}')
             print ('==== > Xin lỗi ! Phiên bản 1.0 chưa hỗ trợ ')   
             kat.select()
          elif num_b == '6': 
             os.system('clear')
             try :
                 print ('==== > { [ Your select : '+num_b+ ' ]}')
                 tree = open('tree.txt','r')
                 print (tree.read())
                 tree.close()
                 input (' Back to Menu ? ')
                 os.system('clear')
                 kat.select()
             except KeyboardInterrupt :
                 os.system('clear')
                 print (' Ok. Bye Bye ')
                 sys.exit()
             except FileNotFoundError:
                 print ('==== > Sorry. File " tree.txt " not FOUND ! ')
                 kat.select()
          elif num_b == '5':
             kat.banner()
          elif num_b == '4':
             os.system('clear')
             print ('\033[1;31;40m==== > { [ Your select : '+num_b+ ' ]}')  
             print ('==== > [ Author : Truong Van Huong - Trương Văn Hướng ][ https://itsat1728.blogspot.com ] [ Version : 1.0 ]'); os.system('uname -a')  
             print ('==== End ====')
             kat.select()
          elif num_b == '3':
             os.system('clear')
             print(he.read())
             he.close()
             input('================== Enter ===================')
             os.system('clear')
             kat.select()
             print ('==== > None <====')
             kat.select()
          elif num_b == '2':
             select2.se2()
             
          elif num_b == '1':
             about = open('about.txt','r')
             os.system('clear')
             print('\033[1;34;40m'+about.read()+'\033[1;37;40m')
             about.close()
             input('================== Enter ===================')
             os.system('clear')
             kat.select()
             print ('==== > None <====')
             kat.select()
          else :
             print ('+-----------------------------------------------------------------------------------+')
             print ('|                  Sorry ! But you dont understand what I say?                      |')
             print ('+-----------------------------------------------------------------------------------+') 
          
      
           
try:       
        kat.banner()   
except :
        os.system('clear') 
        print ('\n                                          +---------------+')
        print ('                                       [ ! ] Error -- Bye  [ ! ]')
        print ('                                          +---------------+\n')
        print ('                                   [ https://itsat1728.blogspot.com ]')
    
     
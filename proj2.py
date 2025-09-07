# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 10:54:47 2025

@author: Lenovo
"""
#list of contacts program 

#explanations for user to understand how the program works
print('this program manage your contact list' , '\n')
print('commands:')
print('1. *add* for adding a contact')
print('2. *delete* for deleting a contact')
print('3. *search* for searching for an specefic contact')
print('4. *contacts* showes the whole contact list you made')


input_ = input('please enter the list of your contacts and their informations: (spilit with comma ,) ').split(',')

#making a dict out of our input user give to program
dict_user = {} 
for i in range(0 , len(input_) , 3):
    livalue = [input_[i+1] , input_[i+2]]
    dict_user[input_[i]] = livalue
    



is_running = True  
while is_running:  #keeping the program alive until user says done
    command = input('please enter your command / for exiting please enter *exit*: ') #askin for commands
    
    #add command
    if (command == 'add'):
        contact_data = input('please write the name,phone,email of the person you want to add: (spilit with comma): ').split(',')
        list_subcom = [contact_data[1] , contact_data [-1]] 
        dict_user[contact_data[0]] = list_subcom
        print('you add', '\n' , contact_data[0] , ':' , list_subcom , '\n' )
        print('new contact list: ')
        counter = 0
        for k , v in dict_user.items():
            counter += 1
            print(counter , '.' , k , ':' , v )
        print('for exiting please enter *exit*')
        
        
     #delete command   
    elif (command == 'delete'):
        name_command = input('please write the name of the person you want to delete: ')
        if name_command in dict_user:
            dname = dict_user.pop(name_command)
            print('contact' ,name_command, 'with the info of', dname , 'has been deleted' , '\n' )
            print('new contact list: ')
            counter = 0
            for k , v in dict_user.items():
                counter += 1
                print(counter , '.' , k , ':' , v )
        else:
            print("contact with this name doesn't exist")
            print('for exiting please enter *exit*')
            
            
     #search command       
    elif (command == 'search'):
        serchcommand = input('please enter the name of the contact you are searching for: ') 
        if serchcommand in dict_user:
            print('contact' , serchcommand , 'informations: ' , '\n' , dict_user[serchcommand]) 
            print('for exiting please enter *exit*')
        else:
            print('contact' , serchcommand , 'does not exist in your contact list' )
            
     #contacts command      
    elif (command == 'contacts'):
        counter = 0
        print('contacts list:')
        for k , v in dict_user.items():
            counter += 1
            print(counter , '.' , k , ':' , v )   
        print('for exiting please enter *exit*')
            
    elif(command == "exit"):
        is_running = False
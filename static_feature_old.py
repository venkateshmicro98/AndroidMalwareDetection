import os
import numpy as np
from androguard.core.bytecodes.apk import APK

#paths and filenames
benignware_path  = "/home/venkatesh/fyp/github/final_year_project/Benignware/"
permissions_path = "/home/venkatesh/fyp/github/final_year_project/"
permissions_file = "list_of_permissions.txt"

#converting text permission to list
with open(permissions_path + permissions_file) as f:
    permissions_list = f.read().splitlines()

#number of permissions in permission list
permissions_list_length = len(permissions_list)

#print("Permission List : " + str(permissions_list))
print("Length of permission list : " + str(permissions_list_length))

#sorting list to optimise the matching 
permissions_list.sort()

#number of application in benignware
files_count = len(os.listdir(benignware_path))
print ("Total no. of benignware files : " + str(files_count))

#print("Permission List : " + str(permissions_list))

#initialising permission vector
permissions_vector = np.zeros((permissions_list_length,files_count),dtype = int)
#print(permissions_vector)

# read the entries
with os.scandir(benignware_path) as listOfEntries:  
    for appln_num,entry in enumerate(listOfEntries):
        # Application Number
        print (appln_num)
        if entry.is_file():
            #application file name
            print(entry.name)
            current_apk = APK( benignware_path + entry.name)
            #extraction current application permissions
            current_apk_permissions = current_apk.get_permissions()
            print (current_apk_permissions)
            
            #generating vector
            for permission in current_apk_permissions:
                print (permission)
                for index,current_permission in enumerate(permissions_list):
                    if(current_permission == permission):
                        print(index,current_permission)
                        permissions_vector[index,appln_num] = 1


#finalised vector
print (permissions_vector)
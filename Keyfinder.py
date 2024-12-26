import os
import shutil
os.system("")
#Magic to make the colors work in the command prompt, no, I have no clue why.

# C:\Program Files (x86)\Steam\steamapps\common\Arma 3\!Workshop

# Todo:
# Generate a token for quick repeatability [Should be done last]                    - This and the below are on hold due to being not being a huge priority -
# Make a way to dynamically change which keys are accpeted and commbine with above  - On hold -
# Make a system to alert the user if no mod files are found by using the CBA mod    #DONE
# Make a more user friendly interface                                               #This is gonna need a non built in module, might not be worth it. - SCRAPPED -
# Add redundancy for mods with key, or KEYS.                                        #Next todo. Note that this will likely effect the task below. DONE [I'm so happy with it too]
# Add a script that reports which keys were made, and if there are any missing      #DONE

def nameFinder():
    list1 = os.listdir(path)
    #Lists every file within the given directory
    try:
        list1.remove('!DO_NOT_CHANGE_FILES_IN_THESE_FOLDERS')
    except:
        print('O O P S')
    #This just prunes away the warning file for ease of use

    print('\n\033[32mMod names:\033[0m')
    for i in list1:
        print(i)
    print('\033[32mMod names end:\033[0m\n')

def keyFinder():
    authorize = input('\n\033[33mCAUTIONARY:\033[0m This will generate a file on THIS machines desktop named folder_of_keys. Then, it will copy all of the keys in the given file path to that folder.\nAuthorize (Y/N?)')
    if authorize.lower() != 'y':
        print('aborting file creation')
        exit()

    newpath = r"desktop\folder_of_keys"
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    #Generates a folder on the desktop which will house the keys

    modlist = os.listdir(path)
    nokeylist = []
    approvedKeyfolders = ['keys', 'key', 'KEYS', 'KEY', 'PublicKey_GOS_Makhno']

    for modname in modlist:

        pathExists = False

        for keyname in approvedKeyfolders:
            if os.path.exists((os.path.join(path, modname, keyname))):
                searchvar = os.path.join(path, modname, keyname)
                pathExists = True
        if pathExists == False:
            nokeylist.append(os.path.join(path, modname))
        #The above figures out if there is the keys folder in the mod, it also supports dynamically changing what keys it looks for, I'm quite happy with it
        
        if pathExists == True:
            filesearch = (os.listdir(searchvar))
            for modfile in filesearch:
                fileEnd = (modfile.split('.'))[-1]
                if fileEnd == 'bikey':
                    storeValue = modfile
        #This makes sure that only the bikey is copied

            filetocopy = os.path.join(path, searchvar, storeValue)
            shutil.copy(filetocopy, newpath)
            #This finds the bikey and then copies it into the folder created earlier

    if len(nokeylist) > 0:
        print('\n\033[31mADVISORY:\033[0m', 'The following mods did not have a key folder recognized by the program, user action recommended:')
        for missingkeys in nokeylist:
            print(missingkeys)
        print('\033[31mEND ADVISORY:\033[0m\n')
        #This lists out all of the missing keys not found by the above

    print(f'File ready at {newpath}')

def userInput(decision):
    if (decision) == '1':
        nameFinder()
    elif (decision) == '2':
        keyFinder()
    elif (decision) == '3':
        nameFinder()
        keyFinder()
    else:
        print('Invalid entry, please retry')
    #This functions calls the other functions above based on user input

path = input('Please input the file directory AS COPIED from file explorer: ')
userOption = input('Output names[1], output keys[2], output both[3]: ')

while True:
    if not userOption.isdigit():
        userOption = input('Incorrect input, please enter 1, 2, or 3: ')
    elif int(userOption) > 3 or int(userOption) < 1:
        userOption = input('Incorrect input, please enter 1, 2, or 3: ')
    else:
        break
#This while block lets the user make mistakes in inputs and will repeat until they do it right.

isARMA = False
for i in os.listdir(path):
    if i == '@CBA_A3':
        isARMA = True
        break

if isARMA == False:
    programabort = input('\n\033[31mADVISORY:\033[0m\nThis folder does not contain the CBA mod, incorrect directory may have been selected.\n\033[31mEND ADVISORY:\033[0m\n\033[36mAbort?(Y/N?): \033[0m')
    if programabort.lower() == 'y':
        raise Exception('PROGRAM FORCE ENDED')
#This is a failsafe to make sure the user gave the program the ARMA folder, since CBA is almost always used in any modded server

userInput(userOption)

#This version of the code is designed to be run in a PC with python installed through and IDE or the command prompt.

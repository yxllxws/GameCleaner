import os
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

#THIS WAS TESTED ON WINDOWS 11, 21H2

system = os.name #os name

allowed = 0 #allowed int

def osCheck(): #check's operating system
    if (system == 'nt'):
       allowed = 1
       print('You are running Windows')
    elif (system == 'java'):
        allowed = 0
        print('You are running Java')
        print("Sorry this software is only for Windows!")
        time.sleep(9235)
    elif (system == 'posix'):
        allowed = 0
        print('You are running Posix')
        print("Sorry this software is only for Windows!")
        time.sleep(9235)

def dir(): #directories
    print("Loading directories. . .")
    time.sleep(3)
    os.system("dir/s")

def tree(): #tree
    print("Loading tree. . .")
    time.sleep(3)
    os.system("tree")

def netRefresh():
    os.system('ipconfig /flushdns') #this clears your internet cache
    time.sleep(2.5)
    os.system('ipconfig /release') #this will disable your internet connection!
    time.sleep(2.5)
    os.system('ipconfig /renew') #this will reactivate your internet connection!

def killTask(): #kill's all of the game task's so it can remove the cached files!
    os.system('taskkill /f /im epicgameslauncher.exe')
    os.system('taskkill /f /im FortniteClient-Win64-Shipping.exe')
    os.system('taskkill /f /im FortniteLauncher.exe')
    os.system('taskkill /f /im EpicGamesLauncher.exe')
    os.system('taskkill /f /im r5apex.exe')
    os.system('taskkill /f /im csgo.exe')
    os.system('taskkill /f /im steam.exe')
    os.system('taskkill /f /im hl2.exe')
    os.system('taskkill /f /im fivem.exe')
    os.system('taskkill /f /im GTA5.exe')
    os.system('taskkill /f /im origin.exe')
    os.system('cls')

os.system('title Game Cleaner by Yxllxws') #title

osCheck()

def main(): #main menu
    print("""░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░░░███████╗░█████╗░███╗░░██╗███████╗██████╗░
██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░░░██╔════╝██╔══██╗████╗░██║██╔════╝██╔══██╗
██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░╚═╝██║░░░░░█████╗░░███████║██╔██╗██║█████╗░░██████╔╝
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██╗██║░░░░░██╔══╝░░██╔══██║██║╚████║██╔══╝░░██╔══██╗
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝███████╗███████╗██║░░██║██║░╚███║███████╗██║░░██║
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝""")
    print("Made by Yxllxws!") 
    print("THIS SOFTWARE IS NOT TO BE USED FOR SPOOFING HWID TO BYPASS BANS!")
    print("THIS IS USED TO CLEAR CACHE IN GAMES TO SAVE SOME STORAGE ON YOUR PC!")
    time.sleep(2.5)
    os.system("cls")
    print(Fore.YELLOW + "[⚠️] This is FREE and OPEN SOURCE software!")
    print("What would you like to clean?")
    print("[1] Games")
    print("[2] Game Launchers")
    print("[3] Temp Files")
    print("[4] Help")
    print("[5] Network [Disable's internet for around 3 secs]")
    print("[6] Check PC Serial's")
    print("[7] Run a Command")
    print("[8] Exit")
    answer = input()
    if (answer == '1'): #game cleaner
        killTask()
        print("Cleaning Games. . .")
        print("Apex Legends")
        os.system('del /f /s "C:\Program Files (x86)\Steam\steamapps\common\Apex Legends\Crashpad\db" ')
        os.system('del /f /s "C:\Program Files (x86)\Steam\steamapps\common\Apex Legends\cfg\autoexec.cfg" ')
        print("CS : GO")
        os.system('del /f /s "C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\imgui.ini" ')
        os.system('del /f /s "C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cache\downloadcache.db" ')
        os.system('del /f /s "C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\voice_ban.dt" ')
        print("Team Fortress 2")
        os.system('del /f /s "C:\Program Files (x86)\Steam\steamapps\common\Team Fortress 2\imgui.ini" ')
        print("Fortnite")
        os.system('del /f /s "C:\Program Files\Epic Games\Fortnite\FortniteGame\PersistentDownloadDir\CMS\Files\9A71EB4A90946A4A0DCD9B7D82F48C55B49D0880\siphon-1024x512-4cc0ff3407053325e353c4aea55fb30316e6ecf6.jpg"')
        os.system('del /f /s "C:\Program Files\Epic Games\Fortnite\FortniteGame\PersistentDownloadDir\CMS\Files\9A71EB4A90946A4A0DCD9B7D82F48C55B49D0880\Fortnite%2Ffortnite-game%2Ftournaments%2F11BR_Arena_ModeTiles_Squad_ModeTile-1024x512-c543a187ce733be5ee9f6d17bfb74fb1f2e15f4a.jpg"')
        os.system('del /f /s "C:\\Users\\%username%\\AppData\\Local\\NVIDIA Corporation\\GfeSDK\\FORTNI~1.LOG"') #delete's multiple cache files
        os.system('del /f /s "C:\Program Files\Epic Games\Fortnite\FortniteGame\PersistentDownloadDir\CMS\Files\9A71EB4A90946A4A0DCD9B7D82F48C55B49D0880\Fortnite%2Ffortnite-game%2Ftournaments%2F11BR_Arena_ModeTiles_Solo_ModeTile-1024x512-6cee09d7bcf82ce3f32ca7c77ca04948121ce617.jpg"')
        print("Rust")
        print("Fivem")
        os.system('del /f /s "C:\\Users\\%username%\\AppData\\Local\\FiveM\\FiveM.app\\data\\cache\\execut~1.bin"') #delete's multiple cache files
        os.system('del /f /s "C:\\Users\\%username%\\AppData\\Local\\FiveM\\FiveM.app\\data\\cache\\execut~2.bin"') #delete's multiple cache files
        os.system('del /f /s "C:\\Users\\%username%\\AppData\\Local\\FiveM\\FiveM.app\\data\\cache\\execut~3.bin"') #delete's multiple cache files
        os.system('del /f /s "C:\\Users\\%username%\\AppData\\Local\\FiveM\\FiveM.app\\data\\cache\\execut~4.bin"') #delete's multiple cache files
        print("Minecraft")
        os.system('del /s /f "C:\\Users\\%username%\\AppData\\Roaming\\.minecraft\\logs"')
        print("Watch Dog's 2")
        os.system('del /s /f "C:\\Users\\%username%\\Documents\\My Games\\Watch_Dogs 2\\EAC.log"')
        print("Tomb Raider")
        os.system('del /s /f "C:\\Users\\%username%\\Documents\\Tomb Raider"')
        input()
    elif (answer == '2'): #launcher cleaner
        killTask()
        print("Cleaning Launchers. . .")
        print("Epic Games")
        os.system('del /s /f "C:\\Users\%username%\\AppData\\Local\\EpicGamesLauncher\\Saved\\webcache_4430\\Service Worker\\Database\\000003.log')
        os.system('del /s /f "C:\\Users\\%username%\\AppData\\Local\\EpicGamesLauncher\\Saved\\webcache_4430\\Service Worker\\Database\\CURRENT')
        os.system('del /s /f "C:\\Users\\%username%\\AppData\\Local\\EpicGamesLauncher\\Saved\\webcache_4430\\Service Worker\\Database\\LOCK')
        os.system('del /s /f "C:\\Users\\%username%\\AppData\\Local\\EpicGamesLauncher\\Saved\\webcache_4430\\Service Worker\\Database\\LOG')
        os.system('del /s /f "C:\\Users\\%username%\\AppData\\Local\\EpicGamesLauncher\\Saved\\webcache_4430\\Service Worker\\Database\\MANIFEST-000001')
        os.system('del /s /f "C:\\Users\\%username%\\AppData\\Local\\EpicGamesLauncher\\Saved\\webcache_4430\\Service Worker\\ScriptCache')
        os.system('del /s /f "C:\\Users\\%username%\\AppData\\Local\\EpicGamesLauncher\\Saved\\webcache_4430\\Service Worker\\ScriptCache\\index')
        print("Steam")
        os.system('del /s /f "C:\\Program Files (x86)\\Steam\\steamapps\\shadercache"')
        time.sleep(2.5)
    elif (answer == '3'): #temp files
        killTask()
        print("Cleaning Temp. . .")
        os.system('del /s /f "C:\\Users\\%username%\\AppData\\Local\\Temp"')
        time.sleep(2.5)
    elif (answer == '4'): #help
        os.system('cls')
        print("Made by Yxllxws!")
        print("GitHub Profile: https://github.com/yxllxws")
        print("GitHub Repo: https://github.com/yxllxws/GameCleaner\n")

        print("Functions:")
        print("osCheck()")
        print("dir()")
        print("tree()")
        print("netRefresh()")
        print("killTask()")
        print("Press any key to close")
        input()
    elif (answer == '5'): #network cleaner
        killTask()
        os.system('cls')
        print("YOUR INTERNET WILL DISCONNECT DURING THIS! DO YOU WANT TO CONTINUE?")
        print("[1] = Yes")
        print("[2] = No")
        answerNet = input()
        if (answerNet == '1'):
            print('Cleaning Network. . .')
            time.sleep(2.5)
            netRefresh()
            time.sleep(1)
            print('Finished! Press any key to exit. . .')
            input()
        elif (answerNet == '2'):
            print('Closing. . .')
            time.sleep(2.5)
    elif (answer == '6'): #serial checker
        os.system('cls')
        check = os.name
        print("Operating System")
        if (check == 'nt'):
            print("Windows\n")
        elif (check == 'java'):
            print("Java\n")
        elif (check == 'posix'):
            print("Linux\n")
            
        print("Disk Drive")
        os.system("wmic diskdrive get serialnumber")
        print("Memory Chip")
        os.system("wmic memorychip get serialnumber")
        print("Base Board")
        os.system("wmic baseboard get serialnumber")
        print("Press any key to close. . .")
        input()
    elif (answer == '7'): #command line
        os.system('cls')
        print('Enter Command into the command line')
        print('If you dont know any commands type into the command line "help"')
        command = input('|')
        if (command == 'osCheck'):
            osCheck()
        elif (command == 'help'):
            os.system('cls')
            print('osCheck --Checks what OS you are on')
            print('dir --Shows all directories on your pc')
            print('tree --Shows a tree of all directories on your pc')
            print('netRefresh --Refreshs the Network on your PC (ONLY USE IF YOU KNOW WHAT YOUR DOING)')
            print('exit --Exits the program')
            command2 = input('|')
            if (command2 == 'osCheck'):
                osCheck()
            elif (command2 == 'dir'):
                dir()
            elif (command2 == 'tree'):
                tree()
            elif (command2 == 'netRefresh'):
                netRefresh()
            elif (command2 == 'exit'):
                os.system('cls')
                print('Closing. . .')
                time.sleep(1)
        elif (command == 'dir'):
            dir()
        elif (command == 'tree'):
            tree()
        elif (command == 'netRefresh'):
            netRefresh()
        elif (command == 'exit'):
            os.system('cls')
            print('Closing. . .')
            time.sleep(1)
        
    elif (answer == '8'): #closes script
        os.system('cls')
        print("Closing. . .")
        time.sleep(2.5)
main()

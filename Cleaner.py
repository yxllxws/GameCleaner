import os
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

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
    os.system('taskkill /f /im origin.exe')
    os.system('cls')

os.system('title Game Cleaner by Yxllxws') #title

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
    print("What would you like to clean?")
    print(Fore.YELLOW + "[⚠️] This is FREE software!")
    print("[1] Games")
    print("[2] Game Launchers")
    print("[3] Temp Files")
    print("[4] Help")
    print("[5] Exit")
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
        os.system('del /f /s "C:\\Users\\%username%\\AppData\\Local\\NVIDIA Corporation\\GfeSDK\\FORTNI~1.LOG"')
        os.system('del /f /s "C:\Program Files\Epic Games\Fortnite\FortniteGame\PersistentDownloadDir\CMS\Files\9A71EB4A90946A4A0DCD9B7D82F48C55B49D0880\Fortnite%2Ffortnite-game%2Ftournaments%2F11BR_Arena_ModeTiles_Solo_ModeTile-1024x512-6cee09d7bcf82ce3f32ca7c77ca04948121ce617.jpg"')
        print("Rust")
        print("Minecraft")
        os.system('del /s /f "C:\\Users\\%username%\\AppData\\Roaming\\.minecraft\\logs"')
        print("Watch Dog's 2")
        os.system('del /s /f "C:\\Users\\Oliver\\Documents\\My Games\\Watch_Dogs 2\\EAC.log"')
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
        print("GitHub Profile: https://github.com/yxllxws\n")
        print("Press any key to close")
        input()
    elif (answer == 'P'): #closes script
        os.system('cls')
        print("Closing. . .")
        time.sleep(2.5)
main()
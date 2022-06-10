from subprocess import call
import os

cmd = 'play -q bbdaad6a-4b58-492b-998e-36dc015be0e8.mp3'
os.system(cmd)
cmd = 'clear'
os.system(cmd)
cmd = 'figlet Andro-CT | lolcat'
os.system(cmd)

cmd = 'echo  "\e[1;32m                                              BY G-ONE" '
os.system(cmd)
cmd = 'echo  "\e[1;32m                                              Version 1.0.1" '
os.system(cmd)

cmd =  'echo "\n\n Please connect to the Mobile Phone Via USB Cable" '
os.system(cmd)
cmd = 'echo "${RED}[${WHITE}1${RED}]${RED}\e[1;32m Reboot" '
os.system(cmd)
cmd = 'echo "${RED}[${WHITE}2${RED}]${RED}\e[1;32m Screen Mirroring" '
os.system(cmd)
cmd = 'echo "${RED}[${WHITE}3${RED}]${RED}\e[1;32m Execeute Shell" '
os.system(cmd)
cmd = 'echo "${RED}[${WHITE}4${RED}]${RED}\e[1;32m Factory Reset(Risky)" '
os.system(cmd)
cmd = 'echo "${RED}[${WHITE}5${RED}]${RED}\e[1;32m Make a Call" '
os.system(cmd)
cmd = 'echo "${RED}[${WHITE}6${RED}]${RED}\e[1;32m Contact Us" '
os.system(cmd)
cmd = 'echo "${RED}[${WHITE}7${RED}]${RED}\e[1;32m Update" '
os.system(cmd)

c=1
while True :
    pw = input("\nChoose Options:")
    if pw  == '1':
        print("Starting")
        cmd = 'adb reboot'
        os.system(cmd)
        call(["espeak","-s120 -ven+6 -z","Rebooting your Phone"])
    
    if pw  == '2':
        print("Starting")
        call(["espeak","-s120 -ven+8 -z","Screen mirroring started"])
        cmd = 'scrcpy'
        os.system(cmd)
    
    if pw  == '7':
        print("Updating")
        call(["espeak","-s120 -ven+8 -z","Screen mirroring started"])
        cmd = 'cd ..'
        os.system(cmd)
        cmd = 'sudo rm -r Andro-CT'
        os.system(cmd)
        cmd = 'git clone https://github.com/Juniorredcoder/Andro-CT'
        os.system(cmd)
        cmd = 'cd Andro-CT'
        os.system(cmd)
        cmd = 'bash anCT.py'
        os.system(cmd)

    if pw  == '6':     
        cmd = 'xdg-open https://facebook.com/termux.kali4'
        os.system(cmd)

    if pw  == '3':
        print("Starting")
        cmd = 'adb shell'
        os.system(cmd)
        call(["espeak","-s120 -ven+8 -z","Shell Execeuted"])
   
    if pw  == '5':
        print("Usage:\n am start -a android.intent.action.CALL -d tel:+CCXXXXXXXXXX \n 1. cc=country code \n 2. XXXXXXXXXX=Phone Number")
        cmd = 'adb shell'
        os.system(cmd)

    if pw == '4':
        pw = input("This is too Risky\nDo You Want To Continue(Y/N):")
        if pw  == 'Y':
            print("Starting")
            cmd = 'adb shell recovery --wipe_data'
            os.system(cmd)
            cmd = 'adb shell exit'
            os.system(cmd)
            cmd = 'adb reboot recovery'
            os.system(cmd)
            call(["espeak","-s120 -ven+6 -z","Reseting your Phone"])
        else:
           print("Like my FB Page")  


c+=1
if c == 90 :
   print('you reached limit')


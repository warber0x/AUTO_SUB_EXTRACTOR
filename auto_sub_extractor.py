from bs4 import BeautifulSoup
import requests
import sys
import subprocess
import os
import threading
import time

global dead 
dead = False

def spinning_cursor():
	while True:
		for cursor in '|/-\\':
			yield cursor

def loading():
	toolbar_width = 40

	spinner = spinning_cursor()
	while not dead:
		sys.stdout.write(next(spinner))
		sys.stdout.flush()
		time.sleep(0.1)
		sys.stdout.write('\b')
			

print("  _ _ ___        _____ _         __           _ _ ")
print(" | | | _ )_  _  |_   _| |_  ___ /  \ _ _  ___| | |")
print(" |_|_| _ \ || |   | | | ' \/ -_) () | ' \/ -_)_|_|")
print(" (_|_)___/\_, |   |_| |_||_\___|\__/|_||_\___(_|_)")
print("          |__/                           v0.1-2020")
print("========= -Automated SubDomains Extractor- =======")

''' Create thread for loading characters ...'''                                                    
x = threading.Thread(target=loading)

if (len(sys.argv) != 2):
	print("Argument error ...")
	print("Usage: " + sys.argv[0] + " just_url_without_http_https")
	print("example: " + sys.argv[0] + " test.com")
	sys.exit(0)

url="https://crt.sh/?q=" + sys.argv[1] 

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

soup = BeautifulSoup(html_content, "lxml")
counter = 0

table = soup.find_all('table')[1] # Grab the first table
urls_file = open(sys.argv[1] + "_urls.txt", "w")

for tr in table.findAll('tr'):
	for td in tr.findAll('td'):

		if (td.text == "None found"):
			print("Couldn't get subdomains ...")
			sys.exit(0)

		for br in td.findAll('br'):
			br.replace_with('\n')
			#br.replace_with('\n')

		if (counter == 5):
			urls_file.write (td.text+'\n')
			counter = 0
			continue
		counter = counter + 1

urls_file.close()

lines_seen = set() # holds lines already seen
outfile = open("out.txt", "w")
for line in open(sys.argv[1] + "_urls.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()

print ("")
print ("Please wait, validating urls...")
print ("===============================")
x.start()
os.system('rm  '+ sys.argv[1] + '_urls.txt')
os.system("mv out.txt " + sys.argv[1] + "_urls.txt")
out = subprocess.run('cat ' + sys.argv[1] + '_urls.txt| httprobe -c 60 > ' + sys.argv[1] + "_valid_urls_no_dups.txt", shell=True)
dead = True 
os.system('rm  '+ sys.argv[1] + '_urls.txt')
print('')
os.system("cat " + sys.argv[1] + "_valid_urls_no_dups.txt")



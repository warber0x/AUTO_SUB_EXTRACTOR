# Automated subdomains extractor

The AUTO_SUB_EXTRACTOR is an automated tool that allows you to search for subdomains using crt.sh

##### Requirements:

1. You need to have Golang installed. 
2. Download ‘httprobe’ by running "go get -u github.com/tomnomnom/httprobe" & compile "go build main.go"
3. Put the 'httprobe' in the same folder as SUB_EXTRACTOR or put it in /usr/bin folder.
4. Python 3
5. Download BeautifulSoup & requests "pip3 install requests beautifulsoup4"

Here are what AUTO_SUB_EXTRACTOR will perform when executed:

1. It extracts subdomains from crt.sh
2. Remove dups and store in a file
4. Run httprobe to validate urls
5. print URLs & store in file for future usage

=> All the sudomains validated are in the same folder where the Sub_Extractor.py was executed.





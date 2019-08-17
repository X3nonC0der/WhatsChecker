import requests
import sys
import os
import argparse
import time
import json

f = requests.session()

#os.system('clear')

# Python 2.x and 3.x compatiablity
if sys.version > '3':
    import urllib.parse as urlparse
    import urllib.parse as urllib
else:
    import urlparse
    import urllib
    
# In case you cannot install some of the required development packages
# there's also an option to disable the SSL warning:
try:
    import requests.packages.urllib3
    requests.packages.urllib3.disable_warnings()
except:
    pass


G = '\033[92m'  # green
Y = '\033[93m'  # yellow
B = '\033[94m'  # blue
R = '\033[91m'  # red
W = '\033[0m'   # white

def banner():
	print("""%s			                
		

 __          ___           _        _____ _               _             
 \ \        / / |         | |      / ____| |             | |            
  \ \  /\  / /| |__   __ _| |_ ___| |    | |__   ___  ___| | _____ _ __ 
   \ \/  \/ / | '_ \ / _` | __/ __| |    | '_ \ / _ \/ __| |/ / _ \ '__|
    \  /\  /  | | | | (_| | |_\__ \ |____| | | |  __/ (__|   <  __/ |   
     \/  \/   |_| |_|\__,_|\__|___/\_____|_| |_|\___|\___|_|\_\___|_|%s%s

                #Coded By David Ayman - @X3nonC0der
    """ % (R, W, Y))

def parser_error(errmsg):
    banner()
    print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
    print(R + "Error: " + errmsg + W)
    sys.exit()

def parse_args():
    # parse the arguments
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -d google.com")
    parser.error = parser_error
    parser._optionals.title = "OPTIONS"

    parser.add_argument('-c', '--code', help='Enter Country', required=True)
    parser.add_argument('-n', '--number', help='Enter Phone Number', required=True)
    parser.add_argument('-d', '--debuger', help='Enable debugger', nargs='?', default=False)

    return parser.parse_args()

username_fetched = ''
api_fetched = ''

with open('acc.txt') as json_file:
	data = json.load(json_file)
	for p in (data['accounts']):
		username_fetched = p['username']
		api_fetched = p['api']

def main(c_code, m_number, debuger):
	action = 'check'
	cod = c_code
	num = m_number

	r = requests.get("https://webservice.checkwa.com/", params={"user": username_fetched, "apikey": api_fetched, "action": action,"num": num,"cod": cod})
	if (debuger):
		print(r.text)
	else:
		data = r.json()
		print('Number: +' + data['number'])
		print('Last Seen: ' + data['lastseen'])
		print('Status: ' + data['status'])
		print('\n')
		print('Picture: ' + data['picture'])
		print('\n\n')
		print('Warning: ' + str(data['limit']))


def interactive():
    args = parse_args()
    code = args.code
    number = args.number

    banner()

    res = main(code, number, args.debuger)

if __name__ == "__main__":
    interactive()
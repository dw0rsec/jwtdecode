#!/usr/bin/env python3

import base64
import json
import sys

COL = '\033[93m'
ERR = '\033[91m'
RES = '\033[0m'

def jwt_decode(token, part):
	token_splitted = token.split('.')

	if part == 2:
		return token_splitted[2]
	else:
		try:
			jwt_decoded = json.loads(base64.b64decode(token_splitted[part] + '===').decode('utf-8'))
			return jwt_decoded
		except UnicodeDecodeError:
			print(f'{ERR}ERROR:{RES} Invalid JWT format.')
			sys.exit(1)
		except Exception as e:
			print(f'{ERR}ERROR:{RES} {e}')

def main():
	if len(sys.argv) < 2:
		print('Usage: jwtdecode.py [TOKEN]')
		sys.exit(1)
	else:
		token = sys.argv[1]
		header = json.dumps(jwt_decode(token, 0), indent=4)
		payload = json.dumps(jwt_decode(token, 1), indent=4)
		signature = jwt_decode(token, 2)
		print(f'{COL}HEADER:{RES} \n{header}')
		print(f'{COL}PAYLOAD:{RES} \n{payload}')
		print(f'{COL}SIGNATURE:{RES} \n{signature}')

if __name__ == '__main__':
	main()

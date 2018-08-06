#!/usr/bin/env python3
import os
from chall7 import AES_ECB_Encrypt,AES_ECB_Decrypt

class oracle:
	def __init__(self):
		self._key = os.urandom(16)
	def encrypt(self, email):
		return AES_ECB_Encrypt(encodeProfile(profileFor(email)).encode(), self._key)
	def decrypt(self, cipher):
		return AES_ECB_Decrypt(cipher, self._key)

def profileFor(email):
	return {'email':email.split("&")[0].split("=")[0],'uid':10,'role':'user'}

def encodeProfile(profile):
	result=''
	for item in profile.items():
		result += item[0]+'='+str(item[1])+'&'
	return result[:-1]

def decodeProfile(profile):
	res = {}
	for _ in profile.split('&'):
		key, value = _.split('=')
		res[key] = int(value) if value.isdigit() else value
	return res

def injectAdmin(oracle):
	#ecb modu isini blok blok yaptigi icin plain bloklar ayni key ile her zaman ayni cipher bloklarini cikarir
	#ilk seferde maili "xxxxxxxxxxadmin\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b" olarak gonderdigimde 2. blok asagidaki gibi olacaktir.
	#
	#  1.blok             2.blok 											  3.blok                                                 4.blok
	#| email=xxxxxxxxxx | admin\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b	| &uid=10&role=use 									   | r\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f |
	#
	#ikinci seferde maili "mail@mail.com" olarak gonderdigimde "role="den sonrasi ayri bir blok olacagindan ilk islemin 2. blogunu ikinci islemin 3. blogu olarak degistirebilirim.
	#
	#  1.blok             2.blok 											  3.blok
	#| email=mail@mail. | com&uid=10&role=                                  | user\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c |
	#

	adminGenerator = "xxxxxxxxxxadmin\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b"
	adminpart = oracle.encrypt(adminGenerator)[16:32]
	mail = "mail@mail.com"
	otherpart = oracle.encrypt(mail)[:32]
	return otherpart+adminpart

def main():
	oracleObj = oracle()
	adminaccount = injectAdmin(oracleObj)
	print(oracleObj.decrypt(adminaccount))
	#b'email=mail@mail.com&uid=10&role=admin'

if __name__ == "__main__":
	main()
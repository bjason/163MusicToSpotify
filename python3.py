# -*- coding: utf-8 -*-
import json
import sys, io
from urllib.request import urlopen

welcome = '===== Get tracks of your 163 playlist ====='
enterId = 'Enter the playlist id (Enter ? to get help):'
help = 'To get the id of the playlist, go to the page \
of it and look at the address bar.\
 \nPlaylist id is the numbers after \
 "http://music.163.com/#/playlist?id="'
errRetrive = 'No data retrived. \nPlease check the playlist id again.'

while 1:
	print(welcome)
	playlistId = input(enterId)

	#change the playlistId variable 
	if playlistId == '?':
		print(help)
		continue
	urladd = "http://music.163.com/api/playlist/detail?id="\
		+ str(playlistId)
	# Your code where you can use urlopen
	with urlopen(urladd) as url:
		response = url.read().decode('utf-8')
	data = json.loads(response)

	output = ""

	if "result" not in data:
		print(errRetrive)
		print(help)
		continue
		
	tracks = data["result"]["tracks"]
	for track in tracks:
		trackName = track["name"]
		artist = track["artists"][0]["name"]
		output += trackName + ' - ' + artist + '\n'
	playlistName = data["result"]["name"]

	with open(playlistName + '.txt', 'w', encoding='utf-8') as file:
		file.write(output)

	print('=== Success ===\nCheck the directory of this file and find the .txt file!')
	print

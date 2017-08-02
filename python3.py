# -*- coding: utf-8 -*-
import json
import sys, io
from urllib.request import urlopen
enterId = 'Enter the playlist id (Enter ? to get help):'
help = 'To get the id of the playlist, go to the page\
of it and look at the address bar.\
 \nPlaylist id is the numbers after \
 "http://music.163.com/#/playlist?id="'
errRetrive = 'No data retrived. \nPlease check the playlist id again.'

while 1:
	playlistId = 85644225

	#change the playlistId variable 
	if playlistId == '?':
		print
	urladd = "http://music.163.com/api/playlist/detail?id="\
		+ str(playlistId) + "&updateTime=-1"
	# Your code where you can use urlopen
	with urlopen(urladd) as url:
		response = url.read().decode('utf-8')
	data = json.loads(response)

	if "result" not in data:
		print(errRetrive)
		print(help)
		continue
		
	tracks = data["result"]["tracks"]


	with open('list.txt', 'w',encoding='utf-8') as file:
		for track in tracks:
			trackName = track["name"]
			artist = track["artists"][0]["name"]
			file.write(trackName+"@"+artist+"\n")

	print('Success.\nCheck the directory of this file and find the .kgl file!')
	break

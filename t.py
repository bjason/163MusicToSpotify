import json
import sys

enterId = 'Enter the playlist id (Enter ? to get help):'
help = 'To get the id of the playlist, go to the page\
 of it and look at the address bar.\
 \nPlaylist id is the numbers after \
 "http://music.163.com/#/playlist?id="'
errRetrive = 'No data retrived. \nPlease check the playlist id again.'

while 1:
	if sys.version_info[0] == 3:
		playlistId = input(enterId)
		from urllib.request import urlopen
	else:
		# Not Python 3 - today, it is most likely to be Python 2
		# But note that this might need an update when Python 4
		# might be around one day
		playlistId = raw_input(enterId)
		from urllib import urlopen

	#change the playlistId variable 
	if playlistId == '?':
		print
	urladd = "http://music.163.com/api/playlist/detail?id="\
		+ str(playlistId) + "&updateTime=-1"
	# Your code where you can use urlopen
	if sys.version_info[0] == 3:
		with urlopen(urladd) as url:
			response = url.read()
	else:
		response = urlopen(urladd).read()
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

	if sys.version_info[0] == 3:
		with open(playlistName + '.txt', 'wb') as file:
			file.write(output.encode('utf8'))
			file.close
	else:
		with open(playlistName + '.txt', 'w') as file:
			file.write(output.encode('utf8'))
			file.close
	print('Success.\nCheck the directory of this file and find the .kgl file!')

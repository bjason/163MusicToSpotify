import json
import sys
import urllib
import httplib

welcome = '===== Get tracks of your 163 playlist ====='
enterId = 'Enter the playlist id (Enter ? to get help):'
help = 'To get the id of the playlist, go to the page\
of it and look at the address bar.\
 \nPlaylist id is the numbers after \
 "http://music.163.com/#/playlist?id="'
errRetrive = 'No data retrived. \nPlease check the playlist id again.'

while 1:
	print(welcome)
	playlistId = raw_input(enterId)

	#change the playlistId variable 
	if playlistId == '?':
		print(help)
		continue
		
	postContent = {"TransCode":"020111","OpenId":"123456789","Body":{"SongListId":playlistId}}
	encodedContent = urllib.urlencode(postContent)
	
	reqUrl = 'https://api.hibai.cn/api/index/index'
	headerData = {"Host":"api.hibai.cn"}
	
	conn = httplib.HTTPConnection("api.hibai.cn")
	
	conn.request(method = "POST", url = reqUrl, body = encodedContent, headers = headerData)
	
	# Your code where you can use urlopen
	response = conn.getresponse().read()
	print(response)
	data = json.load(response)

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
	
	with open(playlistName + '.txt', 'w') as file:
		file.write(output.encode('utf8'))

	print('===== Success =====\nCheck the directory of this file and find the .txt file!')
	print

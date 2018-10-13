import json
import sys
import urllib
import httplib
import urllib2

# using API provided by dongyonghui(https://github.com/mrdong916)
# instruction page: github.com/mrdong916/DAPI

welcome = "===== Get tracks of your 163 playlist ====="
enterId = "Enter the playlist id (Enter ? to get help):"
help = "To get the id of the playlist, go to the page\
of it and look at the address bar.\
 \nPlaylist id is the numbers after \
 'http://music.163.com/#/playlist?id='"
errRetrive = "No data retrived. \nPlease check the playlist id again."

while 1:
	print(welcome)
	playlistId = raw_input(enterId)

	#change the playlistId variable 
	if playlistId == "?":
		print(help)
		continue
		
	# transCode 020111 assigns to retrieve playlist from 163 music
	postContent = {"TransCode":"020111","OpenId":"123456789","Body":{"SongListId":playlistId}}
	encodedContent = json.dumps(postContent) 
	
	reqUrl = "https://api.hibai.cn/api/index/index"
	
	req = urllib2.Request(reqUrl)
	req.add_header('Content-Type', 'application/json')
	req.add_header('Accept', 'application/json')
	
	response = urllib2.urlopen(req, encodedContent).read()
	data = json.loads(response)
	
	output = ""

	if data["ErrCode"] != "OK":
		print(data["ErrCode"])
		print(errRetrive)
		print(help)
		continue
		
	body = data["Body"]
	playlistName = body["name"]
	tracks = body["songs"]
	
	for track in tracks:
		trackName = track["title"]
		artist = track["author"]
		output += trackName + " - " + artist + "\n" 
	
	with open(playlistName + ".txt", "w", encoding="utf-8") as file:
		file.write(output.encode("utf8"))

	print("===== Success =====\nCheck the directory of this file and find the .txt file!")
	print

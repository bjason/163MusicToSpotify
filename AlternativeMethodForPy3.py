import json
import sys
import urllib.request

# using API provided by dongyonghui(https://github.com/mrdong916)
# instruction page: www.dongyonghui.com/default/20180128-网易云、酷狗、QQ音乐歌单接口API.html

welcome = "===== Get tracks of your 163 playlist ====="
enterId = "Enter the playlist id (Enter ? to get help):"
help = "To get the id of the playlist, go to the page\
of it and look at the address bar.\
 \nPlaylist id is the numbers after \
 'http://music.163.com/#/playlist?id='"
errRetrive = "No data retrived. \nPlease check the playlist id again."

while 1:
	print(welcome)
	playlistId = input(enterId)

	#change the playlistId variable 
	if playlistId == "?":
		print(help)
		continue
		
	# transCode 020111 assigns to retrieve playlist from 163 music
	postContent = {"TransCode":"020111","OpenId":"123456789","Body":{"SongListId":playlistId}}
	encodedContent = json.dumps(postContent).encode('utf-8')
	
	reqUrl = "https://api.hibai.cn/api/index/index"
	
	req = urllib.request.Request(reqUrl)
	req.add_header('Content-Type', 'application/json; charset=utf-8')
	req.add_header('Accept', 'application/json')
	
	response = urllib.request.urlopen(req, encodedContent).read()
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
		file.write(output)

	print("===== Success =====\nCheck the directory of this file and find the .txt file!")
	print

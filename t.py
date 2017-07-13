import json
import sys

if sys.version_info[0] == 3:
    from urllib.request import urlopen
else:
    # Not Python 3 - today, it is most likely to be Python 2
    # But note that this might need an update when Python 4
    # might be around one day
    from urllib import urlopen

#change the playlistId variable 
playlistId = 21329331
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

tracks = data["result"]["tracks"]
for track in tracks:
	trackName = track["name"]
	artist = track["artists"][0]["name"]
	output += trackName + ' - ' + artist + '\n'
playlistName = data["result"]["name"]

if sys.version_info[0] == 3:
	with open(playlistName + '.txt', 'wb') as file:
		file.write(output.encode('utf8'))
else:
	with open(playlistName + '.txt', 'w') as file:
		file.write(output.encode('utf8'))

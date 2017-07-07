import urllib, json

#change the playlistId variable 
playlistId = 21329331
url = "http://music.163.com/api/playlist/detail?id="\
	+ str(playlistId) + "&updateTime=-1"
response = urllib.urlopen(url)
data = json.loads(response.read())

output = ""

tracks = data["result"]["tracks"]
for track in tracks:
	trackName = track["name"]
	artist = track["artists"][0]["name"]
	output += trackName + ' - ' + artist + '\n'
playlistName = data["result"]["name"]

with open(playlistName + '.txt', 'w') as file:
	file.write(output.encode('utf8'))

import json
import urllib2

welcome = "===== Get tracks of your 163 playlist ====="
enterId = "Enter the playlist id (Enter ? to get help):"
help = "To get the id of the playlist, go to the page\
of it and look at the address bar.\
 \nPlaylist id is the numbers after \
 'http://music.163.com/#/playlist?id='"

while 1:
    print(welcome)
    playlistId = raw_input(enterId)

    # change the playlistId variable
    if playlistId == "?":
        print(help)
        continue

    reqUrl = "http://localhost:10086/api/player/0/" + str(playlistId)

    req = urllib2.Request(reqUrl)
    req.add_header('Content-Type', 'application/json; charset=utf-8')

    response = urllib2.urlopen(req).read().decode('utf-8')
    data = json.loads(response)

    output = ""

    meta = data["meta"]
    tracks = data["songs"]

    if len(tracks) == 0:
        print("Empty music list, playlist id = " + str(playlistId) + ". You can continue to input your playlist id")
        continue

    playlistName = meta["name"]

    for track in tracks:
        trackName = track["name"]
        artist = track["artists"][0]["name"]
        output += trackName + " - " + artist + "\n"

    with open(playlistName + ".txt", "w") as file:
        file.write(output.encode("utf8"))

    print("===== Success =====\nCheck the directory of this file and find the .txt file!")
    print
    break

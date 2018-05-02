#!/usr/bin/env python3

import musicpd
import time
from datetime import datetime, timedelta

host = "localhost"
port = 6600
max_len = 25
max_title_len = 20
max_artist_len = 12

client = musicpd.MPDClient()
client.connect(host, port)

def print_status():
    client.command_list_ok_begin()
    client.status()
    client.currentsong()
    results = client.command_list_end()

    state = results[0]['state']

    if state == 'play' or state == 'pause':
        song_info = ""
        dots = u"…"
        a_exists = False
        t_exists = False
        f_exists = False
        file_name = "<no data>"
        keys = results[1].keys()
        if 'artist' in keys:
            a_exists = True
            artist = results[1]['artist']
            artist = artist[:max_artist_len] + dots \
                    if len(artist) > max_artist_len else artist
        if 'title' in keys:
            t_exists = True
            title = results[1]['title']
            title = title[:max_title_len] + dots \
                    if len(title) > max_title_len else title
        if 'file' in keys:
            f_exists = True
            file_name = results[1]['file']
            if 'http' in file_name:
                file_name = "<url>"
            else:
                file_name = dots + file_name[-max_len:] \
                        if len(file_name) > max_len else file_name

        if a_exists and not t_exists:
            song_info = artist + " - " + dots
        elif a_exists and t_exists:
            song_info = artist + " - " + title
        if not a_exists and not t_exists:
            song_info = file_name

        # elapsed_time / total_time
        elapsed = int(float(results[0]['elapsed']))
        length = int(float(results[0]['duration']))
        e = datetime(1,1,1) + timedelta(seconds=elapsed)
        t = datetime(1,1,1) + timedelta(seconds=length)

        info_string = song_info

        if length > 3600:
            info_string += " (%02d:%02d:%02d/%02d:%02d:%02d)" % (e.hour, e.minute,
                    e.second, t.hour, t.minute, t.second)
        else:
            info_string += " (%02d:%02d/%02d:%02d)" % (e.minute, e.second,
                    t.minute, t.second)
        print(info_string)
    else:
        print("---")


#for i in range(1000):
#    print_status()
#    time.sleep(1)
print_status()


client.close()
client.disconnect()
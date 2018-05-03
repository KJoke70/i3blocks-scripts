# i3blocks-scripts
Blocklets for [i3blocks](https://github.com/vivien/i3blocks).

## currently_playing ##
Shows the currently playing title in a fixed width

#### Dependencies ####

* a running mpd server
* [python-musicpd](https://pypi.org/project/python-musicpd/)

#### Usage ####

```
usage: currently_playing [-h] [--host HOST] [--port PORT]
                         [--play_symbol PLAY_SYMBOL]
                         [--pause_symbol PAUSE_SYMBOL]
                         [--stop_symbol STOP_SYMBOL]
                         [--refresh-time REFRESH_TIME]
                         [--text-refresh-rate TEXT_REFRESH_RATE]
                         [--string-length STRING_LENGTH] [--pango]
                         [--unicode-font UNICODE_FONT]
                         [--regular-font REGULAR_FONT] [--no-artist]
                         [--no-title]

optional arguments:
  -h, --help            show this help message and exit
  --host HOST, -s HOST  Specify the host mpd is running on
  --port PORT, -p PORT  Specify the port mpd is running on
  --play_symbol PLAY_SYMBOL
                        Symbol-code for playing music (default is f144)
  --pause_symbol PAUSE_SYMBOL
                        Symbol-code for paused music (default is f28b)
  --stop_symbol STOP_SYMBOL
                        Symbol-code for stopped music (default is f28d)
  --refresh-time REFRESH_TIME, -r REFRESH_TIME
                        Interval for when to check data in seconds (float)
  --text-refresh-rate TEXT_REFRESH_RATE, -R TEXT_REFRESH_RATE
                        Interval for text rotation:index will be increased by
                        x for every r
  --string-length STRING_LENGTH, -l STRING_LENGTH
                        Total length of printed string
  --pango, -m           Enables printing with pango markup. Required for some
                        unicode symbols.
  --unicode-font UNICODE_FONT
                        Font for drawing unicode symbols
  --regular-font REGULAR_FONT
                        Font for regular text
  --no-artist           Disable showing the artist
  --no-title            Disable showing the title
```

The block in your i3blocks config should look something like this:

```
[currently_playing]
command=/path/to/the/script/currently_playing --pango #with all parameters you need
interval=persist
separator=true
markup=pango
align=center
```


#### Examples ####

![currently_playing example 1](images/01_currently_playing.gif)

## connection_name ##
## connection_toggle ##
## wifi_toggle ##
## vpn_active ##


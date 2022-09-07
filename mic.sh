ffmpeg -ar 44100 -ac 1 -f alsa -i plughw:1,0 -f wav -listen 1 tcp://0.0.0.0:5002

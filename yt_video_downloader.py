from pytube import YouTube as yt

link = input('Enter the video link : ')
path = 'D:/'

print('Downloading..................')

Myvideo = yt(link).streams.filter(file_extension = "mp4")
Myvideo.first().download(path)

print('Video downloaded successfully')

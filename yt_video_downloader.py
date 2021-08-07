from pytube import YouTube as yt

link = input('Enter the video link : ')

print('Downloading...................')

yt(link).streams.first().download()

print('Video downloaded successfully')

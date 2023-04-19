########## program to download youtube video ##########

# from pytube import YouTube  # y and t must be capital in youtube

# link = "https://youtu.be/ngiAOoR6at8"  # you tube video link
# youtube_1 = YouTube(link)

# # print('Title is' , youtube_1.title)#title batave
# # print('Thumbnail is ' , youtube_1.thumbnail_url)#thumnnails batavi dese ana use thi

# # videos = youtube_1.streams.all()# All formate (ama ek problem k video download thai 6 but open thato nathi)
# # videos = youtube_1.streams.filter(only_audio=True)#khali audio j avse
# videos = youtube_1.streams.filter(only_video=True)  # khali video j avse

# vid = list(enumerate(videos))  # anumerate na use thi badha numbers shaw karse
# for i in vid:
#     print(i)
# strm = int(input("enter :"))
# videos[strm].download()
# print('Finished')




########## program to download youtube playlist ##########

from pytube import Playlist
py = Playlist("https://youtube.com/playlist?list=PL6Rtnh6YJK7bstsU7KitCvVgRc6Vft73o")
print(f'downloading : {py.title}')

for video in py.videos:
    video.streams.first().download()

print('Finished')

#net puru thai gayu mate try kari nahi k download thai 6 k nai em
#ama download thayela video kya ave?
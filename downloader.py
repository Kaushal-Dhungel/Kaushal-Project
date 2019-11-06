from pytube import YouTube
from pytube.exceptions import RegexMatchError
link = input("Enter the link of the video:-")
try:
    url = YouTube(link)
    print("Title:" + url.title)
    #print("Length:" + url.length)

    myvideo = url.streams.all() # returns all the streams

    a = 1
    for stream in myvideo:
        print(f"{a} {stream}")
        #print(str(a) +" " + str(stream ))
        a+=1


    choose = int(input("Enter your choice:"))

    choice_video = myvideo[choose-1] # indexing starts from zero

    choice_video.download('D:\\kaushal')
    print("download successful")

except RegexMatchError:
    print("Please enter valid url")

except Exception as e:
    print(e)
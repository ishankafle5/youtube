from django.http import FileResponse
import os
from django.shortcuts import render, redirect
from pytube import YouTube
from django.conf import settings
from django.http import HttpResponse
# from  import settings
# Create your views here.
from wsgiref.util import FileWrapper
import traceback
from django.http import StreamingHttpResponse
import mimetypes


def indexpage(request):
    return render(request, 'index.html')


# def get_default_browser_path():
#     app_data = os.getenv('LOCALAPPDATA')
#     browser_path = os.path.join(
#         app_data)

#     path = str(browser_path)
#     path = path.split('\\')
#     del path[-2:]

#     path.append('')
#     print(path)
#     # print(path)
#     # for i in range(len(path)):

#     #     newpath = path.remove()

#     # print(newpath)
#     return browser_path


def download_video(request):
    # Your existing code to fetch the video file
    pass


def downloaderfunc(request):
    link = request.POST.get('link')
    print(link)
    try:
        pass
    except:
        print("eer")
    index(request, link)

    # return redirect('http://192.168.1.72:5000/')


def downloader(request, link):

    link = "https://youtu.be/iuFo6Qg-P-4?list=RDiuFo6Qg-P-4"

    # print(youtube_1.title)
    loop = False
    while loop == False:
        try:
            youtube_1 = YouTube(link, use_oauth=True, allow_oauth_cache=False)
            loop = True

        except:
            loop = False

    a = str(youtube_1.title)
    try:
        videos = youtube_1.streams.filter(only_audio=True)

        vid = list(enumerate(videos))
        for i in vid:
            print(i)
        strm = int(input("E n t e r ::    "))

        videos[strm].download().title
        print('Successfully ')

    except:
        print("error")

    return


def index(request):
    print("This is index")
    link = request.POST['link']

    video = YouTube(link)

    stream = video.streams.get_highest_resolution()

    file_path = os.path.join(settings.MEDIA_ROOT)

    print(file_path)
    hi = stream.download(output_path=file_path)
    # return HttpResponse()
    # file_path = os.path.join(settings.MEDIA_ROOT, video.title+'.mp4')
    # return FileResponse(, content_type='video/mp4')
    # return FileResponse(open(file_path+"\\"+video.title+".mp4", 'rb'), content_type='video/mp4')
    # from wsgiref.util import FileWrapper
    title = video.title
    file = FileWrapper(open(file_path+"\\"+title+".mp4", 'rb'), 8192)
    # response = StreamingHttpResponse(
    #     file, content_type=mimetypes.guess_type(file_path)[0])
    # response["Content-Length"] = os.path.getsize(file_path)
    # print("Gize of patha")
    # print(os.path.getsize(file_path))
    # response['Content-Disposition'] = 'attachment; filename=video.mp4'
    # response['X-Sendfile'] = smart_str(path_to_file)
    # return response
    # excpt Exception as e:
    #     # print(traceback.print_exc())
    #     print(e)
    return render(request, 'index.html', {'error': "Error to download a video"})


def download_file(request):
    the_file = "/some/file/name.png"
    filename = os.path.basename(the_file)
    chunk_size = 8192
    response = StreamingHttpResponse(
        FileWrapper(
            open(the_file, "rb"),
            chunk_size,
        ),
        content_type=mimetypes.guess_type(the_file)[0],
    )
    response["Content-Length"] = os.path.getsize(the_file)
    response["Content-Disposition"] = f"attachment; filename={filename}"
    return response

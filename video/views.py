from django.shortcuts import render,get_object_or_404
from .models import Video,VideoUpload, Banner
from .forms import Form,VideoUploadForm
from django.urls import reverse
from django.views.generic import UpdateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# for the home page
def Home(request):
    banner = Banner.objects.all().first()
    object = Video.objects.all()
    paginator = Paginator(object, 12)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        object = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        object = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        object = paginator.page(paginator.num_pages)
    return render(request,'video/video_list.html',{
                                                    'object': object,
                                                    'page': page,
                                                    'banner':banner})

def DetailView(request,id):
    queryset = get_object_or_404(Video,pk=id)
    cont = {
        'object': queryset
    }
    return render(request, template_name='video/detail_view.html', context=cont)

class EditUserProfileView(UpdateView): #Note that we are using UpdateView and not FormView
    model = Video
    form_class = Form
    template_name = "video/edit_view.html"

    def get_object(self, *args, **kwargs):
        user = get_object_or_404( id=self.kwargs['id'])

        # We can also get user object using self.request.user  but that doesnt work
        # for other models.

        return user.video

    def get_success_url(self, *args, **kwargs):
        return reverse("some url name")


def userform(request):
        form = Form(request.POST or None)
        if form.is_valid():
            form.save(commit=False)
            form.save()
        else:
            form = Form()

        return render(request, 'video/form.html', {'newform': form})

def Create(request,POST,*args,**kwargs):
    if request.method == POST:
        form = Form.request.POST
        if  form.is_valid():
            form.save()


def showvideo(request):
    form = VideoUploadForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context = {
               'form': form
               }

    return render(request, 'video/user_upload.html', context=context)








# def Home(request):
#     GOOGLE_API_KEY = "AIzaSyCYx8MrytsaBfyFXBBCzYJVEPKErkcKHq4"
#     CHANNEL_ID = "UC2nd2XJDCPRY5h2K8QZ8cIQ"
#     MAXRESULTS = 50
#     myArray = []
#     GET_URL = "https://www.googleapis.com/youtube/v3/search?key={}&channelId={}&part=snippet,id&order=date&maxResults={}".format(GOOGLE_API_KEY,CHANNEL_ID,MAXRESULTS)
#
#     response = requests.get(GET_URL)
#     response = response.json()
#     pprint(response)
#     for items in response['items']:
#         if items['id']['kind'] == 'youtube#video':
#             video_id = items['id']['videoId']
#             iframe = "<iframe src='https://www.youtube.com/embed/{}></iframe>".format(video_id)
#             Video.objects.create(title=items['snippet']['title'],
#                                  Description=items['snippet']['description'],
#                                  Embed_code=iframe,
#                                  )
#
#     context = {
#     'videos':myArray,
#     }
#     return render(request,'video/video_list.html',context)
#










# # def get_all_video_in_channel(channel_id):
# #     api_key = "AIzaSyCsxg8xVsY7CGU1MqGGiIPtxJFN3NDQhXQ"
# #
# #     base_video_url = 'https://www.youtube.com/watch?v='
# #     base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
# #
# #     first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)
# #
# #     video_links = []
# #     url = first_url
# #     while True:
# #         inp = urllib.request.urlopen(url)
# #         resp = json.load(inp)
# #         video_links.append(resp)
# #     #     # pprint(resp)
# #     #     for i in resp['items']:
# #     #     #     a = i["snippet"]
# #     #     #     b = a["title"]
# #     #         if i['id']['kind'] == "youtube#video":
# #     #             video_links.append(base_video_url + i['id']['videoId'])
# #     #
# #     #     try:
# #     #         next_page_token = resp['nextPageToken']
# #     #         url = first_url + '&pageToken={}'.format(next_page_token)
# #     #     except:
# #     #         # break
# #     return video_links
#
# import urllib
# import json
#
# def get_all_video_in_channel(channel_id):
#     api_key = "AIzaSyCsxg8xVsY7CGU1MqGGiIPtxJFN3NDQhXQ"
#
#     base_video_url = 'https://www.youtube.com/watch?v='
#     base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
#
#     first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)
#
#     video_links = []
#     url = first_url
#     while True:
#         inp = urllib.request.urlopen(url)
#         resp = json.load(inp)
#         pprint(resp)
#         # for item in resp['data']['items']:
#         #     video_list.append(item)
#         # return video_list
#         for i in resp['items']:
#             if i['id']['kind'] == "youtube#video":
# #                 video_links.append(base_video_url + i['id']['videoId'])
#         try:
#             next_page_token = resp['nextPageToken']
#             url = first_url + '&pageToken={}'.format(next_page_token)
#         except:
#             break

#     return video_links
#
# # get_all_video_in_channel("UC2nd2XJDCPRY5h2K8QZ8cIQ")
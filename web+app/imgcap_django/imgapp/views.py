from django.shortcuts import render, HttpResponse, redirect
from imgapp.models import IMG
from imgapp.algrithm_pkg import imgcap2django
from imgapp.ch_image_cap import generate_caption
import os
import tensorflow as tf
graph = tf.get_default_graph()

# Create your views here.
def show(request):
    if request.method == 'GET':
        content = {
            'img_url': '',
            'caption': '',
        }
        return render(request, 'imgapp/upload2show.html', content)
    if request.method == 'POST':
        new_img = IMG(
            # img=request.FILES.get('img')
            img=request.FILES['img']
        )
        new_img.save()
        img_url = IMG.objects.all()[::-1][0].img.url
        # img = IMG.objects.get(name='img')
        # if not img.exists():
        #     img = IMG(img='default.jpg')
        language = int(request.POST.get('language'))
        print(language, type(language))
        if language == 1 or language == 0:
            global graph
            with graph.as_default():
                caption = generate_caption.generate_caption('/home/anna/pycharm_proj/imgcap_django'+img_url)
        elif language == 2:
            caption = imgcap2django.cal_caption(img_url='/home/anna/pycharm_proj/imgcap_django'+img_url, beam_size=5)
        else:
            caption = '此种语言翻译功能暂未上线'
        content = {
            'text1': 'This is your submit:',
            'text2': 'This is a caption for your image:',
            'img_url': img_url,
            'caption': caption,
        }
        agent = ''.join(request.META.get('HTTP_USER_AGENT'))
        # print(agent)
        if 'Android' in str(agent):
            print('There is a Android')
            return HttpResponse(caption)
        elif 'iPhone' in str(agent):
            print('There is a iPhone')
            return HttpResponse(caption)
        elif 'Linux' in str(agent):
            print('There is a Linux')
            return render(request, 'imgapp/upload2show.html', content)
        elif 'Windows' in str(agent):
            print('There is a Windows')
            return render(request, 'imgapp/upload2show.html', content)

# def show(request):
#     if request.method == 'POST':
#         new_img = IMG(
#             # img=request.FILES.get('img')
#             img=request.FILES['img']
#         )
#         new_img.save()
#
#     img_url = IMG.objects.all()[::-1][0].img.url
#     # img = IMG.objects.get(name='img')
#     # if not img.exists():
#     #     img = IMG(img='default.jpg')
#     caption = imgcap2django.cal_caption(img_url='/home/anna/pycharm_proj/imgcap_django'+img_url, beam_size=5)
#     content = {
#         'img_url': img_url,
#         'caption': caption,
#     }
#     return render(request, 'imgapp/upload2show.html', content)

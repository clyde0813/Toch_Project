from django.shortcuts import render


def oneroom_index(request):
    return render(request, 'mobile_template/oneroom/oneroom.html')

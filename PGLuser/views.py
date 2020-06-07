from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from .models import Pgluser

# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):

    if request.method == 'GET':
        return render(request, 'register.html')

    elif request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}

        email_all = [x.email for x in Pgluser.objects.all()]

        if not (email and password and re_password):
            res_data['error'] = '모든 값을 입력해야합니다.'

        elif email in email_all:
            res_data['error'] = '이미 존재하는 이메일입니다.'

        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'

        else:

            pgluser = Pgluser(
                email=email,
                password=make_password(password)
            )

            pgluser.save()

        return render(request, 'register.html', res_data)

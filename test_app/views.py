#コード05
#\test_pro\test_app\views.py

from django import forms
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import TestForm

class TestView(TemplateView):

    def __init__(self):
        self.params = {
                'message': 'テストの点数を入力し、計算ボタンを押して下さい。',
                'average': '',
                'form': TestForm(),
            }

    def get(self, request):
        return render(request, 'test_app/index.html', self.params)

    def post(self, request):
        goal = request.POST['goal']
        ko_score = int(request.POST['kokugo'])
        sa_score = int(request.POST['sannsuu'])
        ri_score = int(request.POST['rika'])
        sya_score = int(request.POST['syakai'])
        ave = (ko_score+sa_score+ri_score+sya_score) / 4
        if goal == '':
            msg = '目標平均点が未入力です。'
        elif int(goal) > ave:
            msg =  '残念！目標平均点は（' + str(goal) + '点）です。'
        else:
            msg =  '目標達成！目標平均点は（' + str(goal) + '点）です。'
        self.params['average'] = ave
        self.params['message'] = msg
        self.params['form'] = TestForm(request.POST)
        return render(request, 'test_app/index.html', self.params)
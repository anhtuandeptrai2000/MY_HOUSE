from django.shortcuts import render
from datetime import datetime

# Create your views here.

def show_info(request, name):
    info = {
        'countries': [
            'Viet Nam',
            'England',
            'Japan',
            'United States',
        ],
        'now': datetime.now()
    }
    return render(request, name + '.html', info)

def country_info(request, country_name):
    info = {
            "Viet Nam":"Việt Nam, tên gọi chính thức là Cộng hòa Xã hội Chủ nghĩa Việt Nam, là một quốc gia nằm ở cực Đông của bán đảo Đông Dương thuộc khu vực Đông Nam Á, giáp với Lào, Campuchia, Trung Quốc, biển Đông và vịnh Thái Lan",
            "England": "",
            "Japan": "",
            "United States": "",
    }
    country_info = info[country_name]
    return render(request, 'country_info_detail.html', {"country_info": country_info})
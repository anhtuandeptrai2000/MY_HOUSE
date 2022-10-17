from django.shortcuts import render
from .models import Customer
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

def listing(request):
    customer_list = Customer.objects.all()
    panigator = Paginator(customer_list,5)

    pageNumber = request.GET.get('get')

    try:
        customer = panigator.page(pageNumber)
    except PageNotAnInteger:
        customer = panigator.page(1)
    except EmptyPage:
        customer = panigator.page(panigator.num_pages)

    return render(request,'listcustomer.html',{'customer':customer})

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages

# import memo form and models
 
from .forms import memoForm
from .models import memo
 
###############################################
 
 
def index(request):
 
    item_list = memo.objects.order_by("-date")
    if request.method == "POST":
        form = memoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('memo')
    form = memoForm()
 
    page = {
        "forms": form,
        "list": item_list,
        "title": "keep-Note",
    }
    return render(request, 'memo/index.html', page)
 
 
### function to remove item, it receive memo item_id as primary key from url ##
def remove(request, item_id):
    item = memo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('memo')

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from markdown2 import markdown
from . import util
from . import page
import os

def index(request):
    if 'q' in request.GET:
        substring = request.GET.get('q')
        filtered_list = [item for item in util.list_entries() if substring.lower() in item.lower()]
        return render(request, "encyclopedia/index.html",{
            "entries": filtered_list
        })
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def topic(request,topic):
    if topic in util.list_entries():
        html = markdown(util.get_entry(topic))
        return render(request, "encyclopedia/topic.html",{
            "html": html,
            "page_topic": topic
        })
    else:
        return render(request, "encyclopedia/404.html")
    
def new_page(request):
    if request.method == "POST":
        form = page.NewPageForm(request.POST)

        if form.is_valid():
            topic = form.cleaned_data["topic"]
            if topic in util.list_entries():
                return render(request,"encyclopedia/new_page.html", {
                    "form": form,
                    "error" : "Page is already exists."
                })  
            content = form.cleaned_data["content"]
            page.save_data_to_file(topic,content)


            return HttpResponseRedirect(reverse("encyclopedia:topic",kwargs={'topic': topic}))
        else:
            return render(request,"encyclopedia/new_page.html", {
                "form": form
            })

    else:
        return render(request,"encyclopedia/new_page.html", {
            "form": page.NewPageForm()
        })
    
def edit_page(request,topic):
    if request.method == "POST":
        form = page.EditPageForm(topic,request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            page.save_data_to_file(topic,content)
            return HttpResponseRedirect(reverse('encyclopedia:topic', kwargs={
                'topic' : topic
            }))
        else:
            return render(request,"encyclopedia/edit_page.html",{
                "form": page.EditPageForm(topic),
                "topic": topic,
            })
    else: 
        return render(request,"encyclopedia/edit_page.html",{
            "form": page.EditPageForm(topic),
            "topic": topic
        })
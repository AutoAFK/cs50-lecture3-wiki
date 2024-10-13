from django.shortcuts import render
import markdown2
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def topic(request,topic):
    if topic in util.list_entries():
        html = markdown2.markdown(util.get_entry(topic))
        return render(request, "encyclopedia/topic.html",{
            "html": html,
            "page_topic": topic
        })
    else:
        return render(request, "encyclopedia/404.html")
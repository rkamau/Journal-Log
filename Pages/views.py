from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib.auth.decorators import login_required

from learning_logs.models import Topic, Entry
from learning_logs.forms import TopicForm, EntryForm

# Create your views here.
def home_view(request):
    context = {}
    return render(request, "home_page.html", context)

@login_required
def topic_view(request):
    """Returns the topics in order of date"""
    topics = Topic.objects.filter(owner = request.user).order_by("date_added")
    #queryset = Topic.objects.all()
    #if topics.owner != request.user:
        #raise Http404
    context = {
        "topics" : topics,
        #"object_list" : queryset
    }
    return render(request, "topic_page.html", context)

@login_required
def entries_view(request, id):
    """Returns the entries as per the topic."""
    topic = Topic.objects.get(id = id)
    entries = topic.entry_set.order_by("-date_added")
    context = {
        "topic" : topic,
        "entries" : entries,
   }
    return render(request, "entries.html", context)

@login_required
def addtopicview(request):
    """Form for a new topic"""
    form = TopicForm(request.POST or None)
    if form.is_valid():
        new_topic = form.save(commit = False)
        new_topic.owner = request.user
        new_topic.save()
        form = TopicForm()
    else:
        print(form.errors)

    context = {
        "form" : form,

    }
    return render(request, "topiccreate.html", context)

@login_required
def addentryview(request, topic_id):
    """Add an entry to a topic"""
    topic = Topic.objects.filter( owner = request.user).get(id = topic_id)

    form = EntryForm(request.POST or None)
    if form.is_valid():
        new_entry = form.save(commit = False)
        new_entry.topic = topic
        new_entry.save()
        form = EntryForm()

    context = {
        "form" : form,
        "topic" : topic,
    }
    return render(request, "entrycreate.html", context)

@login_required
def navigatetopicview(request):
        """Returns the topics in order of date"""
        topics = Topic.objects.filter(owner = request.user).order_by("date_added")
        #queryset = Topic.objects.all()
        context = {
            "topics" : topics,
            #"object_list" : queryset
        }
        return render(request, "nav_topic.html", context)

@login_required
def editentryview(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != "POST":
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/topic/")
        if topic.owner != request.user:
            raise Http404
    context = {
        "entry" : entry,
        "topic" : topic,
        "form" : form,
    }
    return render(request, "editentry.html", context)

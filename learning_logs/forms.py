from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """Generates a form for adding a topic"""
    class Meta:
        model = Topic
        fields = ["topic"]
        #labels = {"text" : ""}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["text"]
        labels = {"text" : "Entry"}
        widgets = {"text" : forms.Textarea(attrs={"cols" : 80})}

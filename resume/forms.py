from django import forms

class ContactForm(forms.Form):
    name= forms.CharField(max_length=50,widget= forms.TextInput
                           (attrs={'placeholder':'Name'}))
    email= forms.EmailField(max_length=50,widget= forms.TextInput
                           (attrs={'placeholder':'Email'}))
    subject= forms.CharField(max_length=50,widget= forms.TextInput
                           (attrs={'placeholder':'Subject'}))
    message=forms.CharField(widget=forms.Textarea
                           (attrs={'placeholder':'Message'}))
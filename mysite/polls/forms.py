from django import forms
from .models import Question	
import datetime

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	email = forms.EmailField(required=False, label='Your email address')
	message = forms.CharField(widget=forms.Textarea)
	
class QuestionForm(forms.ModelForm):
	question_text = forms.CharField(help_text="Please enter the question text.")
	pub_date = forms.DateTimeField(help_text="Date",initial=datetime.datetime.now())
	
	class Meta:
		model = Question
		
		fields = ('question_text','pub_date')
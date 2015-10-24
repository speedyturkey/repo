from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
import datetime
from django.core.mail import send_mail

from .forms import ContactForm, QuestionForm
from .models import Question, Choice

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'
	
	def get_queryset(self):
		"""Return the last five published questions."""
		return Question.objects.filter(
				pub_date__lte=timezone.now()
		).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

	def get_queryset(self):
		"""Excludes any questions that aren't published yet."""
		return Question.objects.filter(pub_date__lte=timezone.now())
	
class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'
	
def vote(request, question_id):
	p = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'polls/detail.html', {
			'question': p,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
		
def search_form(request):
	return render(request, 'polls/search_form.html')
	
	
def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Enter a search term.')
		elif len(q) > 20:
			errors.append('Please enter at most 20 characters.')
		else:
			questions = Question.objects.filter(question_text__icontains=q) 
			return render(request, 'polls/search_results.html',
				{'questions': questions, 'query': q})
	return render(request, 'polls/search_form.html', {'errors': errors})
	

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email', 'noreply@example.com'),
				['siteowner@example.com'],
			)
			return HttpResponseRedirect('/contact/thanks')
	else:	
		form = ContactForm(
			initial={'subject': 'I love your site!'}
		)
	return render(request, 'polls/contact_form.html', {'form': form})
	
def add_question(request):
	context = RequestContext(request)
	
	if request.method == 'POST':
		form = QuestionForm(request.POST)
		
		if form.is_valid():
			form.save(commit=True)
			return render(request, 'polls/index.html')
		else:
			print form.errors
	else:
		form = QuestionForm()
	#assert False
	return render_to_response('polls/add_question.html', {'form': form}, context)
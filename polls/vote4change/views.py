from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Question, Choice

from django.http import JsonResponse
# Create your views here.


# first view: Get question and display them
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {
		'latest_question_list': latest_question_list
	}
	return render(request, 'vote4change/index.html', context)

def detail(request, pk):
	question_obj = get_object_or_404(Question, id=pk)
	context = {
		'question': question_obj
	}
	return render(request, 'vote4change/detail.html', context)

def result(request, pk):
	question_obj = get_object_or_404(Question, id=pk)
	return render(request, 'vote4change/result.html', {'question': question_obj})

def vote(request, pk):
	question = get_object_or_404(Question, id=pk)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'vote4change/detail.html',
			{
			'question': question,
			'error_message': 'You did not select a choice'
			}
			)
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return redirect(reverse('vote4change:result', args=(question.id,)))


#  for chart
def result_data(request, object_id):
	votedata = []

	question = Question.objects.get(id=object_id)
	votes = question.choice_set.all()
	for i in votes:
		votedata.append({i.choice_text: i.votes})
	print(votedata)
	return JsonResponse(votedata, safe=False)


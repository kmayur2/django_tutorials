from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #response=','.join([q.question_text for q in latest_question_list])
    #return HttpResponse(response)

    #template = loader.get_template('polls/index.html')
    context = {
            'latest_question_list': latest_question_list,
            }
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)


def detail(request, q_id):
    #return HttpResponse("You are looking at question %s" % q_id)
    '''try:
        q = Question.objects.get(pk=q_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')'''

    q = get_object_or_404(Question, pk=q_id)

    return render(request, 'polls/detail.html', {'question':q})



def results(request, q_id):
    #return HttpResponse("You are looking at result for question %s" % q_id)
    question = get_object_or_404(Question, pk=q_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, q_id):
    #return HttpResponse("You are voting for question %s" % q_id)
    #q = get_object_or_404(Question, pk=q_id)
    #return render(request, 'polls/detail.html', {'question':q, 'error_message': "You didn't select a choice."})
    question = get_object_or_404(Question, pk=q_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def errormessage(request):
    raise Http404("Test error")

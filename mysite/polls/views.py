from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader
from django.shortcuts import render, get_object_or_404

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
    return HttpResponse("You are looking at result for question %s" % q_id)

def vote(request, q_id):
    return HttpResponse("You are voting for question %s" % q_id)

def errormessage(request):
    raise Http404("Test error")

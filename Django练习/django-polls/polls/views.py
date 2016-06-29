from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
# from django.template import loader, RequestContext
from .models import Question, Choice


class IndexView(generic.ListView):
    """docstring for IndexViews"""
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    # ?疑问，这里应该是不可以直接通过字符串前面的lastest求得前五，而是通过下面get_queryset()函数求的
    def get_queryset(self):
        '''Return the last five published questions.'''
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
        

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
#     # template = loader.get_template('polls/index.html')
#     # context = RequestContext(request, {
#     #     'latest_question_list': latest_question_list,
#     #     })
#     # return HttpResponse(template.render(context))

# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
# #     return HttpResponse("{}".format(question_id))

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_chice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question_id': p,
            'error_message': "You didn't select a choice",
            })
    else:
        selected_chice.votes += 1
        selected_chice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
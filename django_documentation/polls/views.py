from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]


# render http response un shortcut'ı
# 1. parametresi request, 2.si sayfaya bastırılacak template, 3.sü de request atarken gönderilecek diictionary.
# o  yüzden context değişkenini tanımlayıp dictionary yaptık


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


# result ve detail view fonksiyonlarının model'ları Question olduğu için result.html ve detail.html sayfalarında kullanılan "question" değişkenini django temin edebiliyor


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        #print("try")
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        #print("except")
        # Redisplay the question voting form.
        # Her şekilde bir kez except'e giriyor ve formu basıyor
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        #print("else")
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

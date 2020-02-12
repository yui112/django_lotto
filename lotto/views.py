from django.shortcuts import render,redirect
from django.http import HttpResponse
from lotto.models import GuessNumbers
from lotto.forms import PostForm

# Create your views here.

def index(request):
    lottos = GuessNumbers.objects.all()
    return render(request, 'lotto/default.html', {'lottos':lottos})

def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")

def post(request):
    # print("********")
    # print(request.method)
    # print("********")
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            lotto = form.save(commit = False) #github에서의 컴밋과 같은
            #무언가를 더 할때 false로 설정
            lotto.generate()

            return redirect('index')

    else:
        form = PostForm() #empty form
        return render(request, "lotto/form.html", {"form":form})


def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk = lottokey)
    return render(request, "lotto/detail.html", {"lotto":lotto})

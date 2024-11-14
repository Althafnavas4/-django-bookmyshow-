from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req,"index.html")



def movie(req):
    return render(req,"movie.html")

def LuckyBaskhar(req):
    return render("LuckyBaskhar.html")
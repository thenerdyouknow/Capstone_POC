from django.shortcuts import render
from django.http import HttpResponse
from .forms import TweetForm

# Create your views here.

def index(request):
	form = TweetForm()
	return render(request, 'index.html', {'form': form})


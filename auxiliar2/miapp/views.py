from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'miapp/index.html')
	
def pestaña(request):
	return render(request, 'miapp/pestaña.html')
	

def edocente(request):
	return render(request, 'miapp/edocente.html')
	
def extra(request):
	return render(request, 'miapp/extra.html')
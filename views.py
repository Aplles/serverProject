from server.routing import render


def index(request):
    return render(request, 'index.html', context={
        'name': 'Максим'
    })


def home(request):
    return render(request, 'home.html')
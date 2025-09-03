from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406433112',
        'name': 'Naira Ammara Putri',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)

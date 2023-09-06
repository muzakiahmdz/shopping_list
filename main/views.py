from django.shortcuts import render
def show_main(request):
    context = {
        'name': 'Muzaki Ahmad Ridho Azizy',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
# Create your views here.

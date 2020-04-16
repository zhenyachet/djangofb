from django.shortcuts import redirect

def redirect_bboard(request):
    return redirect('homepage', permanent=True)
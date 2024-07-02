from django.http import HttpResponse

def fileFetch(request):
    return HttpResponse ("File Fetch view")

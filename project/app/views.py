from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request, "count.html")

def result(request):
    text = request.POST['text']
    no_blank = text.replace(" ", "")
    total_len = len(text)
    no_blank_len = len(no_blank)
    word_count_list = text.split()
    word_count = len(word_count_list)
    return render(request, "result.html", {
        'total_len' : total_len,
        'text' : text,
        'no_blank_len' : no_blank_len,
        'word_count' : word_count
    })
from django.shortcuts import render

# Create your views here.

def layout(request):
    return render(request, 'layout.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dic = {}
    for word in words:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1

    return render(request, 'result.html', 
    {
        'full':text,
        'word_dic':word_dic.items(),
        'total':len(words)
    })


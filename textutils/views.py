#i have created this file ayush
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #it will show the home page that is text area index.html ater return
    return render(request,'index.html')
def analyse(request):
    # getting the text through post
    djtext=request.POST.get('text','default')

    # getting the checkbox on or off
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    capitalize=request.POST.get('capitalize','off')
    rmnewline=request.POST.get('rmnewline','off')
    spremover=request.POST.get('spremover','off')
    exspremover=request.POST.get('exspremover','off')
    charcount=request.POST.get('charcount','off')

    # variable for dictionary value
    task=""
    val=''
    kya=False

    # analysing the text

    # removing punctuation
    if(removepunc=='on'):
        analysed = ''

        punctuations='''!()-[]{};:'<>./\?@#$%^&*_~'''

        task="remove punctuation"
        kya=True
        for i in djtext:

            if i not in punctuations:
                analysed += i
        djtext=analysed
        val=analysed

    #converting to UPPERCASE
    if fullcaps=='on':
        kya=True
        analysed = ''
        task="converted into UPPERCASE"
        analysed=djtext.upper()
        djtext=analysed
        val=analysed

    #capitalizing the text
    if capitalize=='on':
        kya=True
        analysed = ''
        task='after Capitalizing the text'
        analysed=djtext.capitalize()
        djtext=analysed
        val=analysed

    # removing new line
    if rmnewline=='on':
        kya=True
        analysed = ''
        task="after removing new line"
        for i in djtext:
            if(i!='\n' and i!="\r"):
                analysed+=i
        djtext=analysed
        val=analysed

    # removing space
    if spremover=='on':
        kya=True
        analysed = ''
        task='after removing spaces'
        for i in djtext:
            if i!=' ':
                analysed+=i
        djtext=analysed
        val=analysed

    #Extra space remover
    if exspremover=='on':
        kya=True
        analysed = ''
        task="after removing extra spaces"
        for index,char in enumerate(djtext):
            if not(djtext[index]==' ' and djtext[index+1]==' '):
                analysed+=char
        djtext=analysed
        val=analysed

    # charcount
    ctask=''
    count=''
    if charcount=='on':
        kya=True
        ctask="Total charcount is:"
        count=len(djtext)

    # if all the condition false this will work
    if kya==False:
     return HttpResponse("Error")
    else:
        # if one of condition or many condition is on then this will work
        params = {'purpose': task, 'analysed_text': val,'ctask':ctask,'count':count}
        return render(request, 'analyse.html', params)

#it will show about page
def about(request):
    return render(request,'about.html')

# it will show contact page
def contact(request):
    return render(request,'contact.html')














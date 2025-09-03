from django.shortcuts import render, HttpResponse

# Create your views here.

def books_list(request):
    return HttpResponse("""<li>1</li>
    <li>2</li>
    <li>3</li>
    <li>4</li>
    <li>5</li>""")


def books_special(request):
    return HttpResponse("""
                        
    <div>
        <div>
            <h1>Book one</h1>
        </div>
        <div>
            <h1>Book Two </h1>
        </div>
    </div>

""")

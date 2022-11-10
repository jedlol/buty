from django.shortcuts import render

count = 0
def index(request): # without event because I use `command=` instead of `bind`
    global count
    if request.method == "POST":
        count = count + 1

    return render(request=request, template_name="casa.html", context={"count": count})

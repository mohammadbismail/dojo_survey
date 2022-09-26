from django.shortcuts import render, redirect


def index(request):
    return render(request, "index.html")


def result(request):
    name_from_form = request.POST["name"]
    location_from_form = request.POST["location"]
    language_from_form = request.POST["language"]
    comment_from_form = request.POST["comment"]
    context = {
        "name_on_template": name_from_form,
        "dojo_location": location_from_form,
        "favorite_language": language_from_form,
        "comment": comment_from_form,
    }
    return render(request, "result.html", context)


# def result(request):

#     return render(request, "result.html")

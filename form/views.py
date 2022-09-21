from django.shortcuts import render, redirect


def index(request):
    return render(request, "index.html")


def create_users(request):
    name_from_form = request.POST["name"]
    location_from_form = request.POST["location"]
    language_from_form = request.POST["language"]
    comment_from_form = request.POST["comment"]
    print(request.POST)
    context = {
        "name_on_template": name_from_form,
        "dojo_location": location_from_form,
        "Favorite_language": language_from_form,
        "comment": comment_from_form,
    }
    return redirect("/result")


def result(request):

    return render(request, "result.html")

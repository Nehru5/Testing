from django.shortcuts import render, redirect
from myapp.models import UserDetail


def Users(request):
  if request.method == "POST":
    username = request.POST.get("username")
    email = request.POST.get("email")
    age = request.POST.get("age")
    
    UserDetail.objects.create(
      name = username, email = email, age = age
    )
    return redirect("Users")
  return render(request,"./users.html")
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# from django.contrib.auth.backends import BaseBackend
from .models import UserManager, UserCollaborator

def home(request):
    # userManag = UserManager.objects.all()
    # userCollab = UserCollaborator.objects.all()
    return render(request, 'home/index.html') #{'usersManag': userManag, 'usersCollab': userCollab}

# def cadastro(request):
#     if request.method == "GET":
#         return render(request, 'home/index.html')
#     else:
#         username = request.POST.get('name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         function = request.POST.get('function')

#         userManag = UserManager.objects.filter(email=email)
#         userCollab = UserCollaborator.objects.filter(email=email)
#         if userManag or userCollab:
#             return HttpResponse('E-MAIL JÁ CADASTRADO!')
#         else:
#             userManag = UserManager.objects.filter(function=function)
#             userCollab = UserCollaborator.objects.filter(function=function)
#             if userManag:
#                 userManag = UserManager.objects.create(name=username, email=email, password=password, function=function)
#                 userManag.save()
#                 userManag = UserManager.objects.all()
#                 return render(request, 'home/index.html', {'users': userManag})

#             if userCollab:
#                 userCollab = UserCollaborator.objects.create(name=username, email=email, password=password, function=function)
#                 userCollab.save()
#                 userCollab = UserCollaborator.objects.all()
#                 return render(request, 'home/index.html', {'users': userCollab})

# def editar_user_manag(request, id):
#     userManag = UserManager.objects.get(id=id)
#     return render(request, 'home/update_manag.html', {'users': userManag})

# def editar_user_collab(request, id):
#     userCollab = UserCollaborator.objects.get(id=id)
#     return render(request, 'home/update_collab.html', {'users': userCollab})

# def delete_user_manag(request, id):
#     userManag = UserManager.objects.get(id=id)
#     userManag.delete()
#     return redirect(home)

# def delete_user_collab(request, id):
#     userCollab = UserCollaborator.objects.get(id=id)
#     userCollab.delete()
#     return redirect(home)

# def update_user_manag(request, id):
#     new_name = request.POST.get('name')
#     new_email = request.POST.get('email')
#     new_function = request.POST.get('function')

#     userManag = UserManager.objects.get(id=id)
#     userManag.name = new_name
#     userManag.email = new_email
#     userManag.function = new_function
#     userManag.save()        
#     return redirect(home)
    
# def update_user_collab(request, id):
#     new_name = request.POST.get('name')
#     new_email = request.POST.get('email')
#     new_function = request.POST.get('function')

#     userCollab = UserCollaborator.objects.get(id=id)
#     userCollab.name = new_name
#     userCollab.email = new_email
#     userCollab.function = new_function
#     userCollab.save()        
#     return redirect(home)

# def login(request):
#     if request.method == "GET":
#         return render(request, 'home/login.html')
#     else:
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         userManag = UserManager.objects.filter(email=email, password=password)
#         userCollab = UserCollaborator.objects.filter(email=email, password=password)

#         if userManag or userCollab:
#             return HttpResponse('CADASTRADO!')
#         else:
#             return HttpResponse('E-MAIL OU SENHA INVÁLIDOS!')


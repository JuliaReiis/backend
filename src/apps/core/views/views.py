from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..serializers.serializers import UserSerializer

from ..models.model import Company, User, Doc
# from .forms import CompanyForm, UserForm, DocForm

import json

@api_view(['GET'])
def list_company_by_user(request, user_id):

    if request.method == 'GET':
        user_companies = User.objects.filter(usuario_id=user_id)
        companies = [uc.company for uc in user_companies]
        serializer = UserSerializer(companies, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_users(request):

    if request.method == 'GET':
        users = User.objects.all()
        users = [uc.usuario for uc in user_companies]
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def list_users(request):

    
    return Response({"teste":"teste"})

@api_view(['PUT'])
def list_users(request):

    
    return Response({"testePUT":"testePUT"})


@api_view(['GET'])
def list_docs_by_company_and_user(request, company_id, user_id):

    if request.method == 'GET':
        doc_associations = Doc_Association.objects.filter(company_id=company_id, usuario_id=user_id)
        docs = [da.doc for da in doc_associations]
        serializer = UserSerializer(docs, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# def criar_company(request):
#     if request.method == 'POST':
#         form = CompanyForm(request.POST)
#         if form.is_valid():
#             company = form.save(commit=False)
#             company.save()
#             return redirect('listar_company_por_usuario')
#     else:
#         form = CompanyForm()
#     return render(request, 'criar_company.html', {'form': form})

# def criar_usuario(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.save()
#             return redirect('listar_usuario_por_company')
#     else:
#         form = UserForm()
#     return render(request, 'criar_usuario.html', {'form': form})

# def criar_doc(request):
#     if request.method == 'POST':
#         form = DocForm(request.POST)
#         if form.is_valid():
#             doc = form.save(commit=False)
#             doc.save()
#             return redirect('listar_doc_por_company_e_usuario')
#     else:
#         form = DocForm()
#     return render(request, 'criar_doc.html', {'form': form})

# def atualizar_company(request, company_id):
#     company = Company.objects.get(pk=company_id)
#     if request.method == 'POST':
#         form = CompanyForm(request.POST, instance=company)
#         if form.is_valid():
#             form.save()
#             # Atualizar entradas na tabela associativa User_Company
#             User_Company.objects.filter(company=company).update(company=form.instance)
#             return redirect('listar_company_por_usuario')
#     else:
#         form = CompanyForm(instance=company)
#     return render(request, 'atualizar_company.html', {'form': form})

# def atualizar_usuario(request, user_id):
#     user = User.objects.get(pk=user_id)
#     if request.method == 'POST':
#         form = UserForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('listar_usuario_por_company')
#     else:
#         form = UserForm(instance=user)
#     return render(request, 'atualizar_usuario.html', {'form': form})


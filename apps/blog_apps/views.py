# -*- coding: utf-8 -*-

from django.shortcuts import render,HttpResponse,redirect
def index(request):
	response="Placeholder to display all the list of blogs"
	return HttpResponse(response)

def new(request):
	response="placeholder to display a new form to create a new blog"
	return HttpResponse(response)

def create(request):
	
	return redirect('/')

def show(request,number):
	
	return HttpResponse('Placeholder to display blog '+number)

def edit(request,number):
	
	return HttpResponse('Placeholder to edit blog '+number)

def destroy(request,number):
	
	return redirect('/')


# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

#Views for Student

def students_list(request):
	students = (
		{'id':1, 
		'first_name': u'Петро',
		'last_name': u'Пілонов',
		'ticket': 235,
		'image': 'img/1.png'},
		{'id': 2, 
		'first_name': u'Андрій',
		'last_name': u'Корост',
		'ticket': 2123,
		'image': 'img/2.png'},
		{'id': 3, 
		'first_name': u'Олександр',
		'last_name': u'Кірєв',
		'ticket': 3476,
		'image': 'img/s4.png'}
		)

	return render(request, 'students/students_list.html', 
		{'students': students})

def students_add(request):
	return HttpResponse('<h1> Student Add Form </h1>')

def students_edit(request, sid):
	return HttpResponse('<h1> Edit Student %s </h1>' %sid)

def students_delete(request, sid):
	return HttpResponse('<h1> Delete Student %s </h1>' %sid)

#Views for Groups

def groups_list(request):
	return HttpResponse('<h1> Groups Listing </h1>')

def groups_add(request):
	return HttpResponse('<h1> Group Add Form </h1>')

def groups_edit(request, gid):
	return HttpResponse('<h1> Edit Group %s </h1>' %gid)

def groups_delete(request, gid):
	return HttpResponse('<h1> Delete Group %s </h1>' %gid)




	
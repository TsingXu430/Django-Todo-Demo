import leancloud
from django.shortcuts import render
from django.http import HttpResponseRedirect
from leancloud import Object, LeanCloudError, Query
from settings import LC_APP_ID, LC_APP_KEY


class Todo(Object):
    pass


TRASHED, PLANNED, COMPLETED = -1, 0, 1

leancloud.init(LC_APP_ID, LC_APP_KEY)


def show(request, **status):
    status = int(status.get('status', 0))
    try:
        todos = Query(Todo).add_descending('createdAt').equal_to('status', status).find()
    except LeanCloudError as e:
        todos = []
        print(e.error)
    todos_list = []
    for todo in todos:
        todo_list = {}
        todo_list['id'] = todo.get('objectId')
        todo_list['content'] = todo.get('content')
        todo_list['createAt'] = todo.get('createdAt')
        todos_list.append(todo_list)
    context = {'status': status, 'todos': todos_list}
    return render(request, 'todos.html', context)


def add(request):
    content = request.POST['content']
    todo = Todo()
    todo.set('content', content)
    todo.set('status', PLANNED)
    try:
        todo.save()
    except LeanCloudError as e:
        print(e.error)
    return HttpResponseRedirect('/todo/')


def delete(request, todo_id, status):
    todo = Todo.create_without_data(todo_id)
    try:
        todo.set('status', TRASHED)
        todo.save()
    except LeanCloudError as e:
        print(e.error)
    return HttpResponseRedirect('/todo/' + status)


def done(request, todo_id, status):
    todo = Todo.create_without_data(todo_id)
    try:
        todo.set('status', COMPLETED)
        todo.save()
    except LeanCloudError as e:
        print(e.error)
    return HttpResponseRedirect('/todo/'+status)


def undone(request, todo_id, status):
    todo = Todo.create_without_data(todo_id)
    try:
        todo.set('status', PLANNED)
        todo.save()
    except LeanCloudError as e:
        print(e.error)
    return HttpResponseRedirect('/todo/' + status)

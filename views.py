from django.shortcuts import render,redirect

from django.http import HttpResponseRedirect

# Create your views here.
lst = [
    
]

def index(request):
    global lst
    if request.method == 'POST':
        if request.POST['新添代办事项'] == '':
            content = {'list':lst,'warning':"输入为空!"}
            return render(request, 'todo_list/index.html',content)
        else:
            lst.append({'新添代办事项':request.POST['新添代办事项'],'done':False})    
            content = {'list':lst,'添加成功':"添加成功!"}
            return render(request, 'todo_list/index.html',content)
    
    elif request.method == 'GET':
        content = {'list':lst}
        return render(request, 'todo_list/index.html',content)

def inform(request):
    return render(request, 'todo_list/inform.html')

def edit(request,forloop_counter):
    global lst
    if request.method == 'POST':
        if request.POST['修改的事项'] == '':
            return render(request, 'todo_list/edit.html',{'warning':"输入为空!"})
        else:
            lst[int(forloop_counter) - 1]['新添代办事项'] = request.POST['修改的事项']
            # content ={"待更改事项" :lst[int(forloop_counter) - 1]['新添代办事项']}
            return redirect ('todo_list:主页')
    elif request.method == 'GET':
        content ={"待更改事项" :lst[int(forloop_counter) - 1]['新添代办事项']}
        return render(request, 'todo_list/edit.html', content)

def delete(request,forloop_counter):
    global lst
    lst.pop(int(forloop_counter) - 1)
    return redirect ('todo_list:主页') 

def status(request,forloop_counter):
    global lst
    if request.POST['status'] == '已完成':
        lst[int(forloop_counter) - 1]['done'] = True
    else:
        lst[int(forloop_counter) - 1]['done'] = False
    return redirect ('todo_list:主页') 

    
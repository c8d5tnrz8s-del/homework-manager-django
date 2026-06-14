from django.shortcuts import render, redirect
from .models import Homework
from .forms import HomeworkForm


def homework_list(request):

    query = request.GET.get('q')

    if query:
        homeworks = Homework.objects.filter(
            description__icontains=query
        )
    else:
        homeworks = Homework.objects.all()

    return render(
        request,
        'tasks/homework_list.html',
        {
            'homeworks': homeworks
        }
    )


def homework_create(request):

    if request.method == 'POST':
        form = HomeworkForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('homework_list')

    else:
        form = HomeworkForm()

    return render(
        request,
        'tasks/homework_form.html',
        {'form': form}
    )

def homework_update(request, pk):

    homework = Homework.objects.get(pk=pk)

    if request.method == 'POST':
        form = HomeworkForm(
            request.POST,
            instance=homework
        )

        if form.is_valid():
            form.save()
            return redirect('homework_list')

    else:
        form = HomeworkForm(instance=homework)

    return render(
        request,
        'tasks/homework_form.html',
        {'form': form}
    )

def homework_delete(request, pk):

    homework = Homework.objects.get(pk=pk)

    if request.method == 'POST':
        homework.delete()
        return redirect('homework_list')

    return render(
        request,
        'tasks/homework_confirm_delete.html',
        {'homework': homework}
    )
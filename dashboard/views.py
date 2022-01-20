from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy

class Calls(ListView):
    model = Call
    context_object_name = 'calls'
    template_name = 'dashboard/calls.html'

class CallsAnswered(Calls):
    queryset = Call.objects.filter(status='Answered')
    template_name = 'dashboard/calls_answered.html'

class CallsMissed(Calls):
    queryset = Call.objects.filter(status='Missed')
    template_name = 'dashboard/calls_missed.html'

class CallCreate(CreateView):
    model = Call
    fields = '__all__'
    success_url = reverse_lazy('calls')

class CallEdit(UpdateView):
    model = Call
    fields = '__all__'
    success_url = reverse_lazy('calls')

class CallDelete(DeleteView):
    model = Call
    context_object_name = 'call'
    template_name = 'dashboard/call_delete.html'
    success_url = reverse_lazy('calls')

class Customers(ListView):
    model = Customer
    context_object_name = 'customers'
    template_name = 'dashboard/customers.html'

class Customer(DetailView):
    model = Customer
    template_name = 'dashboard/customer.html'
    def get_context_data(self, **kwargs):
        ctx = super(Customer, self).get_context_data(**kwargs)
        ctx['calls'] = Call.objects.all()
        return ctx

class Tasks(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'dashboard/tasks.html'

class TasksCompleted(Tasks):
    queryset = Task.objects.filter(status="Completed")
    template_name = 'dashboard/tasks_completed.html'

class TasksIncompleted(Tasks):
    queryset = Task.objects.filter(status="Incompleted")
    template_name = 'dashboard/tasks_incompleted.html'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskEdit(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'dashboard/task_delete.html'
    success_url = reverse_lazy('tasks')

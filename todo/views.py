"""
This module renders the views for each webpage of the todo app.
The views are the mechanism by which the front-end users of the app
are able to communicate with the back-end data.
"""
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


def get_todo_list(request):
    """
    Render todo_list template and displays the todo items. Query set
    all the items in the db. Create context dictionary store all the
    items in it. Add context as third argument to ensure that you
    have access to the template.
    """
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    """
    Allows front-end users to interact with back-end data by creating
    their own items. The ItemForm class inherits from Django form
    model and the Item model to leverage the built in functionality.
    This ensures that Django handles validation.
    """
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)


def edit_item(request, item_id):
    """
    Allows users to edit a specific item in the to do list using the
    item_id. The ItemForm class inherits from Django form model and
    the Item model to leverage the built in functionality. This
    ensures that Django handles validation.
    """
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)


def toggle_item(request, item_id):
    """
    Providing another facet of update functionality as it allows
    users to toggle the 'done' status of a specific item. Using 'not'
    to flip the status of done.
    """
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')


def delete_item(request, item_id):
    """
    Allows users to delete a specific item from the todo list.
    The item is deleted from the db.
    """
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')

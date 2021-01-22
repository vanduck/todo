from django.http import HttpResponse
from django.shortcuts import render, reverse, redirect
from todo_item.models import ListItem
from main.models import ListModel
from todo_item.forms import ItemForm


def item_view(request, pk):
    list_ = ListModel.objects.select_related('user').get(id=pk)
    list_items = ListItem.objects.filter(
        list_model_id = list_
    )

    context = {
        'lists': list_items,
        'list_name': list_.name,
        'user_name': request.user.username,
        'pk': pk
    }
    return render(request, 'list.html', context)


def create_view(request, pk):
    form = ItemForm
    if request.method == 'POST':
        form = ItemForm(
            data={
                'name': request.POST.get('name'),
                'list_model': pk,
                'expare_date': request.POST.get('expare_date')
            }
        )

        if form.is_valid():
            success_url = reverse('todo_item:item', kwargs={'pk': pk})
            form.save()
            return redirect(success_url)

    context = {
        'form': form,
        'pk': pk
    }

    return render(request, 'new_item.html', context)

def edit_item_view(request, pk):
    item= ListItem.objects.get(id=pk)

    if request.method == 'POST':
        form = ItemForm(
            data={
                'name': request.POST.get('name'),
                'list_model': item.list_model,
                'expare_date': request.POST.get('expare_date')
            }, instance=item
        )

        if form.is_valid():
            success_url = reverse('todo_item:item', kwargs={'pk':item.list_model_id})
            form.save()
            return redirect(success_url)

    else:
        form = ItemForm(instance=item)

    context = {
        'form': form,
        'list_model_id': item.list_model_id,
        'pk': pk
    }

    return render(request, 'edit_item.html', context)

def delete_item_view(request, pk):
    item = ListItem.objects.filter(
        id=pk,
        list_model__user=request.user
    ).first()

    if item:
        item.delete()
        success_url = reverse('todo_item:item', kwargs={'pk': item.list_model_id})
        return redirect(success_url)
    return HttpResponse(status=404)
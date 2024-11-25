from django.shortcuts import render, redirect , get_object_or_404
from .models import Watches
from .forms import WatchForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def all_watches(request):
    watches = Watches.objects.all() 
    context = {
        'watches': watches
    }
    return render(request, 'blog_temp/all_watches.html', context)


@login_required
def create_watch(request):
    if request.method == "POST":
        form = WatchForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.created_by = request.user
            form.save()
            new_form.save()
            
            return redirect('all_watches')
        else:
            return redirect('create_watch')
    else:
        form = {
            'watch_form': WatchForm()
        }
        return render(request, 'blog_temp/create_watch.html', form)



def detail_watch(request, pk):
    watch = get_object_or_404(Watches, id=pk)
    context = {
        'watch': watch
    }
    return render(request, 'blog_temp/detail_watch.html', context)


@login_required
def update_watch(request, pk):
    watch = get_object_or_404(Watches, id=pk)
    if watch.created_by != request.user:
        messages.error(request, "Siz yalnız öz yaratdığınız watch-u yeniləyə bilərsiniz.")
        return redirect('all_watches') 
    if request.method == "POST":
        form = WatchForm(request.POST, instance=watch)
        if form.is_valid():
            form.save()
            return redirect('detail_watch', watch.pk)
        else:
            for price in form.errors:
                messages.error(request, WatchForm.errors[price])
                return redirect(request.path)
    else:
        form = WatchForm(instance=watch)

        context = {
            'watch_form': form
        }
        return render(request, 'blog_temp/update_watch.html', context)




@login_required
def delete_watch(request, pk):
    watch = get_object_or_404(Watches, id=pk)
    if watch.created_by != request.user:
        return redirect('all_watches')
    watch.delete()
    messages.success(request, 'Melumat ugurla silindi')
    return redirect('all_watches')






 






from django.shortcuts import render, redirect
from .models import ClickCounter

def click_counter(request):
    click_counter = ClickCounter.objects.first()
    print("Current level:", click_counter.level)
    if not click_counter:
        click_counter = ClickCounter.objects.create(clicks=0)
    return render(request, 'clicker_app/click_counter.html', {'click_counter': click_counter})

def increment_click(request):
    click_counter = ClickCounter.objects.first()
    if click_counter is None:
        # Если объект ClickCounter отсутствует в базе данных, создаем его
        click_counter = ClickCounter.objects.create(clicks=0)
    click_counter.clicks += 1
    click_counter.save()
    return redirect('click_counter')

def reset_clicks(request):
    click_counter = ClickCounter.objects.first()
    click_counter.clicks = 0
    click_counter.save()
    return redirect('click_counter')

def decrement_clicks(request):
    if request.method == 'POST':
        click_counter = ClickCounter.objects.first()
        if click_counter:
            if click_counter.clicks >= 10:
                click_counter.clicks -= 10
                click_counter.save()
                click_counter.reset_count += 1
                click_counter.save()
                click_counter.level = click_counter.reset_count // 10 + 1
                click_counter.save()
    return redirect('click_counter')

def your_view(request):
    click_counter = ClickCounter.objects.first()
    context = {
        'level': click_counter.level  # Передаем уровень в контекст шаблона
    }
    return render(request, 'your_template.html', context)

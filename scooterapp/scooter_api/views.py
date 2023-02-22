from django.shortcuts import render, get_object_or_404, redirect
from .models import Scooter, Trip, User
from django.db.models import Sum
from django.db.models.functions import TruncYear
from django.views.generic import ListView
from django.urls import reverse_lazy
from .forms import ImageForm, AddScooter, BookingScooter
from django.views.generic import UpdateView
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import csv


# Главная старинца
def index(request):
    return render(request, 'index.html')


# Для dashboard получаем всю информацию об поездках и пользователях
def get_all_info(request):

    contact_list_scooter = Scooter.objects.all()
    paginator = Paginator(contact_list_scooter, 5)
    page_number = request.GET.get('page')
    page_obj_scooter = paginator.get_page(page_number)

    contact_list_trip = Trip.objects.all()
    paginator = Paginator(contact_list_trip, 5)
    page_number = request.GET.get('page')
    page_obj_trip = paginator.get_page(page_number)

    context = {
        'page_obj_scooter': page_obj_scooter,
        'page_obj_trip': page_obj_trip
    }
    return render(request, 'dashboard/dashboard.html', context)


# Считаем стоимость всех поездок и группируем их по дате
def get_data_per_data(request):
    trips = Trip.objects.values('date_of_trip').annotate(total=Sum('cost'))

    context = {
        'trips': trips,
    }

    return render(request, 'dashboard/dashboard_day.html', context)


# Считаем стоимость всех поездок и группируем их по годам (используем TruncYear)
def get_data_per_year(request):
    trips = Trip.objects.values(year=TruncYear(
        'date_of_trip')).annotate(total=Sum('cost'))

    context = {
        'trips': trips
    }

    return render(request, 'dashboard/dashboard_year.html', context)


# Группируем поездки по тем, кто совершил поездки и считаем сумму
def get_data_per_made_a_trip(request):

    trips = Trip.objects.values('rider').annotate(total=Sum('cost'))

    context = {
        'trips': trips,
    }

    return render(request, 'dashboard/dashboard_user.html', context)


''' 
    Создаем профиль пользователей в качестве slug передаем pk(primary key)
    Используем декоратор @login_required (Проверяет аутентифицирован ли пользователь,
    если нет, то пренаправляет его на URL-адрес логирования.)
'''

@login_required
def profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    count_trips = Trip.objects.filter(rider=user).count
    context = {
        'users': user,
        'count_trips': count_trips,
    }
    return render(request, 'profile.html', context)


# В проофиле пользователь может поменять свою аватарку
def update_image(request, pk):
    user = get_object_or_404(User, pk=pk)
    form = ImageForm(request.POST, files=request.FILES, instance=request.user)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("profile", pk=user.id)
    return render(request, 'image_edit.html', {'form': form, 'user': user})




'''Админ сайта может поменять статус самоката(
    Свободен - пользователь может его забронировать в приложении
    Занят - Кто-то уже катается на самокате
    На ремонте - Идет обслуживание самоката и его нельзя забронировать
    Заряжается - Самокат находится на зарядке и его нельзя забронировать
    )
    P.S. На карте отображаются значки
'''
class UpdateScooter(UpdateView):
    model = Scooter
    template_name = 'dashboard/update_scooters.html'
    success_url = reverse_lazy('dashboard')
    fields = ['active',]


# Ошибка 404, если страница не найдена
def page_not_found(request, exception):
    return render(request, "misc/404.html", status=404)


# Ошибка 500 проблемы с сервером
def server_error(request):
    return render(request, "misc/500.html", status=500)


# Админ сайта может посмотреть информацию об самокате
def scooter_detail(request, pk):
    scooters = get_object_or_404(Scooter, pk=pk)
    count_trip = Trip.objects.filter(scooter=scooters).count
    context = {
        'scooters': scooters,
        'count_trip': count_trip,
        'trips': Trip.objects.all()
    }
    return render(request, "dashboard/detail_scooter.html", context)


# Кнопка у пользователей на которой можно посмотреть, где находятся самокаты
def view_scooter(request):

    places = Scooter.objects.all()

    context = {
        'places': places
    }
    return render(request, "view_a_scooters.html", context)


# Добавить новый самокат
def add_scooter(request):
    form = AddScooter(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_scooter.html', context)

# Забронировать самокат
def book_scooter(request):
    if request.method == 'POST':
        form = BookingScooter(request.POST)
        if form.is_valid():
            form.instance.rider = request.user
            form.save()
            return redirect('index')
    else:
        form = BookingScooter()
    return render(request, 'booking_scooter.html', {'form': form})


# Экспорт данных по самокатам в формат csv
def export_to_csv_scooter(request):
    scooters = Scooter.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=scooter.csv'
    writer = csv.writer(response)
    writer.writerow(['id','serial_number', 'latitude', 'longitude', 'charge', 'active'])
    scooter_fields = scooters.values_list('id','serial_number', 'latitude', 'longitude', 'charge', 'active')
    for scooter in scooter_fields:
        writer.writerow(scooter)
    return response



def export_to_csv_trip(request):
    trips = Trip.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=trips.csv'
    writer = csv.writer(response)
    writer.writerow(['id', 'rider_id', 'date', 'cost', 'scooter_id'])
    trip_fields = trips.values_list('id', 'rider', 'date_of_trip', 'cost', 'scooter')
    for trip in trip_fields:
        writer.writerow(trip)
    return response


def export_to_csv_users(request):
    users = User.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=users.csv'
    writer = csv.writer(response)
    writer.writerow(['id', 'username', 'city', 'first_name', 'last_name', 'email'])
    user_fields = users.values_list('id', 'username', 'city', 'first_name', 'last_name', 'email')
    for user in user_fields:
        writer.writerow(user)
    return response
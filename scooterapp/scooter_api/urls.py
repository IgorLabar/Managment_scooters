from . import views
from django.urls import path
from users.views import register_user, login_user, logout_user


urlpatterns = [
    #Страница 'админки' для заказчика
    path('dashboard/', views.get_all_info, name='dashboard'),

    #Страница с диаграммами
    path('chart/', views.get_data_per_data, name='chart revenue by day'),

    #Страница с диаграммами по пользователям
    path('chart-user/', views.get_data_per_made_a_trip, name='chart revenue by user'),

    #Страница с диаграммой по году
    path('chart-year/', views.get_data_per_year, name='chart revenue by year'),
    
    #Страница регестрации пользователя
    path('register/', register_user, name='register'),
    
    #Страница входа пользователя, который зарегистрировался
    path('login/', login_user, name='login'),
    
    #Страница личного профиля для зарегистрировавшегося пользователя
    path('profile/<int:pk>', views.profile, name='profile'),
    
    #Выход из аккаунта
    path('logout/', logout_user, name='logout'),
    
    #В профиле пользователя можно изменить картинку
    path('update/<int:pk>', views.update_image, name='update'),
    
    #Страница с информацией о самокате
    path('scooter-detail/<int:pk>', views.scooter_detail, name='detail_scooter'),
    
    #Посмотреть, где находятся самокаты на карте
    path('view-scooter/', views.view_scooter, name='view_scooter'),
    
    #Страница обновления статуса самоката
    path('update-scooter/<int:pk>', views.UpdateScooter.as_view(), name='update_scooter'),
    
    #Добавить новый самокат
    path('add-scooter/', views.add_scooter, name='add_scooter'),

    # Страница бронирования самоката
    path('book-scooter/', views.book_scooter, name='booking'),


    path('export-to-csv-scooter/', views.export_to_csv_scooter, name='export_to_csv_scooter'),


    path('export-to-csv-trip/', views.export_to_csv_trip, name='export_to_csv_trip'),


    path('export-to-csv-user/', views.export_to_csv_users, name='export_to_csv_user'),

    
    #Главная страница
    path('', views.index, name='index'),
]
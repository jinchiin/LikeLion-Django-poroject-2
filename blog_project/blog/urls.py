from . import views
path('update/<int:id>/', views.update, name = 'update')
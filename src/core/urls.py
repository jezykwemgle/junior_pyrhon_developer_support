from django.contrib import admin
from django.urls import path

from .exchange_rates_hw import exchange_rate, exchange_rate_history

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exchange-rates/', exchange_rate),
    path('exchange-rates/history', exchange_rate_history)
]

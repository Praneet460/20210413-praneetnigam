from django.urls import path, include
from .views import BMIView, BMI_Stats_View

urlpatterns = [
    path('bmi/', BMIView.as_view(), name="bmi_view"),
    path('bmi/stats', BMI_Stats_View.as_view(), name="bmi_stats")
]

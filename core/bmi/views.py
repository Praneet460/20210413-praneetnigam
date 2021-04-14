from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .utils import BMI_Cal

class BMIView(APIView):

    def get(self, request, *args, **kwargs):
        data = {"message": "This request is not Allowed."}
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        bmi_cal = BMI_Cal(jsonData=request.data)
        bmi_values = bmi_cal.bmi_logic()
        response_data = bmi_cal.df_to_dict(json_df=bmi_values)
        return Response(response_data, status=status.HTTP_200_OK)

class BMI_Stats_View(APIView):
    
    def post(self, request, *args, **kwargs):
        bmi_cal = BMI_Cal(jsonData=request.data)
        bmi_stats_resp = bmi_cal.bmi_stats()
        return Response(bmi_stats_resp, status=status.HTTP_200_OK)


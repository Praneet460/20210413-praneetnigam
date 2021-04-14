from django.test import TestCase
from django.urls import reverse
import json

class BMITests(TestCase):
    
    def test_bmi_response(self):

        post_data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, 
                { "Gender": "Male", "HeightCm": 161, "WeightKg":85 }]

        resp_data = [{
            "Gender": "Male",
            "HeightCm": 171,
            "WeightKg": 96,
            "bmi": 56.14,
            "bmi_catg": "Very Severely Obese",
            "health_risk": "Very High Risk"
        },
        {
            "Gender": "Male",
            "HeightCm": 161,
            "WeightKg": 85,
            "bmi": 52.8,
            "bmi_catg": "Very Severely Obese",
            "health_risk": "Very High Risk"
        }]

        response = self.client.post(reverse('bmi_view'), json.dumps(post_data), 
                        content_type='application/json')
        # Checks
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data, resp_data)

    def test_bmi_stats(self):
        post_data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, 
                { "Gender": "Male", "HeightCm": 161, "WeightKg":85 }]

        resp_data = {
            "Very Severely Obese": 2,
            "Very High Risk": 2
        }

        response = self.client.post(reverse('bmi_stats'), json.dumps(post_data), 
                        content_type='application/json')
        # Checks
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, resp_data)


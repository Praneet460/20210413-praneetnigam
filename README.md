## BMI Calculator API
It is a bmi API, build purely using Python (programming language), Django and Django-Rest-Framework (opensource framework written in python).

### Current Features
Listing the features of the API
- Given ```weight``` and ```height```, calculates ```bmi index```, ```bmi category```
and ```health risk```
- Gives the stats of count of each category of ```bmi category``` and ```health risk```

### API EndPoints
API Endpoints defines the structure of the API and how end users access data from our application using the HTTP methods - POST

| Endpoint | HTTP Method | CURD Method | Result |
|---|---|---|---|
| ```api/v1/bmi``` | POST | CREATE | Create 3 new key-value pair ```bmi index```, ```bmi catg``` and ```health risk``` |
| ```api/v1/bmi/stats``` | POST  | CREATE  | Gives back common stats of the data |

### URL of Main Code

- API View Ends Path : core.bmi.views
- BMI Business Logic Path : core.bmi.utils
- API Tests Path : core.bmi.tests

### Run Tests
- ```python manage.py test bmi.tests.view.BMITests```
    - 2 Tests Passed

### Example
- <b>BMI Details</b>
    - <b>POST</b>
    ```http://localhost:8000/api/v1/bmi/```
        - </b>Body</b>
            ```
            [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, 
            { "Gender": "Male", "HeightCm": 161, "WeightKg":85 }]
            ```
        - <b>Response</b>
            ```
            [
                {
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
                }
            ]
            ```

    - <b>POST</b>
    ```http://localhost:8000/api/v1/bmi/stats```
        - <b>Body</b>
            ```
            [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, 
            { "Gender": "Male", "HeightCm": 161, "WeightKg":85 }]
            ```
        - <b>Response</b>
            ```
            {
                "Very Severely Obese": 2,
                "Very High Risk": 2
            }
            ```


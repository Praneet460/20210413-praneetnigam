import pandas as pd

class BMI_Cal():
    """
    Class Perform Body-Mass-Index Calculations
    """

    def __init__(self, jsonData):

        self.jsonData = jsonData

    def bmi_logic(self):
        
        jsonData = self.jsonData
        json_df = pd.DataFrame(jsonData)
        json_df['bmi'] = round(json_df['WeightKg'] / (json_df['HeightCm']/100), 2)
        json_df['bmi_category'] = json_df['bmi'].apply(lambda val: self.bmi_catg(val))
        json_df[['bmi_catg', 'health_risk']] = pd.DataFrame(json_df['bmi_category'].tolist())
        json_df.drop('bmi_category', inplace=True, axis=1)
        return json_df

    def bmi_stats(self):

        json_df = self.bmi_logic()
        bmi_catg_stats = json_df['bmi_catg'].value_counts()
        health_risk_stats = json_df['health_risk'].value_counts() 
        return {**dict(bmi_catg_stats), **dict(health_risk_stats)}

    @staticmethod
    def bmi_catg(val):

        bmi_index = val
        if bmi_index <= 18.4:
            return ('Underweight', 'Malnutrition Risk')
        elif 18.5 <= bmi_index <= 24.9:
            return ('Normal Weight', 'Low Risk')
        elif 25 <= bmi_index <= 29.9:
            return ('Overweight', 'Enhanced Risk')
        elif 30 <= bmi_index <= 34.9:
            return ('Moderately Obese', 'Medium Risk')
        elif 35 <= bmi_index <= 39.9:
            return ('Severely Obese', 'High Risk')
        else:
            return ('Very Severely Obese', 'Very High Risk')

    @staticmethod
    def df_to_dict(json_df):
        
        return json_df.to_dict('records')

    

    
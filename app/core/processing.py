import pandas as pd
from io import BytesIO
from typing import Dict, Any
from datetime import datetime


class DataProcessor:
    def __init__(self, path:str):
        self.path = path
        self.df = None
    
    def process(self):
        self.df = pd.read_csv(self.path)
        self.df.dropna(subset=['amount', 'category'], inplace=True)
        self.df['description'] = self.df['description'].fillna('No description')
        self.df['timestamp'] = pd.to_datetime(self.df['timestamp'])
        self.df['amount'] = pd.to_numeric(self.df['amount'])

        income = self.df[self.df['flow_type'] == 'IN']['amount'].sum()
        expense = self.df[self.df['flow_type'] == 'OUT']['amount'].sum()

        net_cash_flow = income - expense
        category_sum = self.df.groupby('category')['amount'].sum().to_dict()
        report_path = f"data/report_{datetime.now().strftime('%d%m%Y_%H%M%S')}.xlsx"
        self.df.to_excel(report_path, index=False)

        return {
            "summary":{
                "total_income": income,
                "total_expense": expense,
                "net_cash_flow": net_cash_flow,
                "transaction_count": len(self.df),
            },
            "category_analysis": category_sum,
            "report_file": report_path
        }
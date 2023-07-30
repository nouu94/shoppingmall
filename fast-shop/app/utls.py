from datetime import datetime

import requests

from app.models import DeliveryCompany
from fast_shop.settings import ST_API
from pytz import timezone

def now():
    return datetime.now(timezone('Asia/Seoul'))

# https://info.sweettracker.co.kr/api/v1/companylist?t_key=IWPxh3eQttGyMcrUovr1Vw
def save_delivery_company():
    uri = f"https://info.sweettracker.co.kr/api/v1/companylist?t_key=IWPxh3eQttGyMcrUovr1Vw"
    res = requests.get(uri)
    header = {"accept":  "application/json;charset=UTF-8"}
    company = res.json().get("Company")
    print(company)
    for c in company:
        DeliveryCompany.objects.create(code=c.get("Code"), name=c.get("Name"))

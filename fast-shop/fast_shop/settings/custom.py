import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "app_db",
        "USER": "root",
        "PASSWORD": "choi201302133!",
        "HOST": "localhost",
        "PORT": "3306",
        "OPTIONS": {"autocommit": True, "charset": "utf8mb4"},
    }
}

ST_API = "IWPxh3eQttGyMcrUovr1Vw"
EMAIL_ID = "ck12qw@gmail.com"  # 보안 수준이 낮은 앱 허용된 구글 이메일?
EMAIL_PW = "choi201302133!"

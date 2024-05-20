### To run this prjoect
1. Change the setting in `setting.py` file:
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "lecmanagement",
        "USER": "root",
        "PASSWORD": "your_password",
        "HOST": "localhost",
        "PORT": 3306,
    }
}
Make sure you have created a Database name `lecmanagement`
2. cd to quanlygiangvien with cmd: cd quanlygiangvien
3. To create or change the data models of this application, you need to synchronize the database structure with these 2 commands:
 run cmd: python manage.py makemigrations 
 run cmd: python manage.py migrate
4. To import `home_department` data to Mysql Sever
   run cmd: py manage.py insert_data_from_sql

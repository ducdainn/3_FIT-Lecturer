### How to Run This Project

1. **Update Database Settings:**

   Update the database settings in the `settings.py` file as follows:

   ```python
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
   ```

   Ensure that you have created a database named `lecmanagement`.

2. **Navigate to the Project Directory:**

   Open your command prompt or terminal and navigate to the `quanlygiangvien` directory using the following command:

   ```
   cd quanlygiangvien
   ```

3. **Synchronize Database Structure:**

   To create or update the data models for this application, synchronize the database structure by running the following commands:

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Import Data from SQL:**

   If required, import the `home_department` data into the MySQL server by running the following command:

   ```
   py manage.py insert_data_from_sql
   ```

5. **Run the Django Development Server:**

   Start the Django development server by executing the following command:

   ```
   python manage.py runserver
   ```

   This will start the development server at `http://127.0.0.1:8000/login/`.

6. **Access the Application:**

   Open your web browser and navigate to `http://127.0.0.1:8000/login/` to access the application.

Feel free to adjust these steps according to your project's requirements and configurations.

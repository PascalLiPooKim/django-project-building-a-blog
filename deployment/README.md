# Deployment Information

This created blog was not made to be deployed for production. However, deployment can be done as follows:

1. Update the ```settings.py``` file as follows as a starting setup:

   - **DEBUG** should be changed from *True* to *False*.
   - Check if all the **INSTALLED_APPS** and the **MIDDLEWARE** are setup correctly (they should be normally fine by default).
   - Add **STATIC_ROOT** = **BASE_DIR** / <name_of_folder> to collect all the static files.

2. Collect all the static files by running: ```python manage.py collectstatic``` in the appropriate directory.
3. These static files in the created folder (with name given above) should be served by adding ```static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)``` in the ```urls.py``` file of ```my_site``` folder.
4. Make sure that all the required dependencies are found in a ```requirements.text``` file by using the command  ```python -m pip freeze > requirements.txt``` (it is best to do it a virtual environment so that only the required dependencies are saved in the text file and not all dependencies that were installed outside the project).

5. Going back to the ```settings.py``` file

   - In the **ALLOWED_HOSTS** list, add ```getenv(<name_of_environment_variable></name_of_environment_variable>)```.

6. First choice server for development would be to use <span style="color:orange">*AWS Elastic Beanstalk*</span> (free tier) to create an application. Choose the appropriate option during the setup.
7. To be able to ```Upload your code```, more preparations need to be done in our project. Create an ```.ebextensions``` folder and in it add a ```django.config``` file.
8. Compress the required files and folders and upload the zipped folder on <span style="color:orange">*AWS*</span>.
9. Click on ```Configure more options```, go to ```Edit``` **Software** and in the "Environment properties" section,, fill with:

   - IS_DEVELOPMENT = False
   - APP_HOST = xxx (it is not known until deployed for the first time unless it is known in advance)
10. Create the application. The domain will be then seen. Copy it and in the Configuration - Software - Environment properties, replace the placeholder with the domain. Apply the changes.

## Additional Information

1. SSL and custom domains can be configured (depending on *AWS* tier used).

2. Connecting to PostgreSQL:
   1. Instead of using **SQLite**, other databases can be used such as **PostgreSQL**. More information can found on [django Databases](https://docs.djangoproject.com/en/4.1/ref/databases/) (additional dependencies may be needed and after installation, make sure to update the ```requirements.txt```).
   2. <span style="color:orange">*AWS RDS*</span> (free tier) would be the first database choice.
   3. Moreover, in the ```settings.py```, the **DATABASES** configuration should be changed accordingly based on details of the <span style="color:orange">*RDS*</span>.
   4. Run ```python manage.py migrate```.
   5. As a new database was created and added, a super user need to be created. No posts will be seen on the (deployed) website as the database is empty.
   6. Re-upload on <span style="color:orange">*AWS Elastic Beanstalk*</span> should be done after compressing the right files and folders as some files were updated. Deploy again.
   7. Regarding the **Security Groups** of the  <span style="color:orange">*RDS*</span>, change the inbound rules to ```Anywhere```.


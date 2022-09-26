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

6. First choice server for development would be to use <span style="color:orange">*AWS Elastic Beanstalk*</span> to create an application. Choose the appropriate option during the setup.
7. To be able to ```Upload your code```, more preparations need to be done in our project. Create an ```.ebextensions``` folder and in it add a ```django.config``` file.
8. Compress the required files and folders and upload the zipped folder on <span style="color:orange">*AWS*</span>.
9. Click on ```Configure more options```, go to ```Edit``` **Software** and in the "Environment properties" section,, fill with:

   - IS_PRODUCTION = False
   - APP_HOST = xxx (it is not known until deployed for the first time unless it is knwon in advance)
10. Create the application. The domain will be then seen. Copy it and in the Configuration - Software - Environment properties, replace the placeholder with the domain. Apply the changes.

# image_gallery

Image gallery app where we can upload photos and assign a category to it from a set of predefined categories.

**Prerequisites:**

virtualenv

python3.8 >=

.env file


For running this project you need to have the **.env** file in the root directory, which can be downloaded from the following Google Drive link:

https://drive.google.com/drive/folders/1X6FyebrWtTfyh4ANBWIVHmgH2qRcNRNN?usp=sharing

Steps:

1. Download the .env file from above Google Drive link into image_gallery project.

2. Change **DJANGO_ENV** from 'production' to 'local' in .env

3. Create virtual environment and activate it.

4. Run `pip install -r requirements.txt`

5. Run `python manage.py runserver`



You can find it hosted on Heroku:

https://images-gallery-demo.herokuapp.com/
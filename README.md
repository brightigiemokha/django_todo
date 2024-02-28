

# ANYIADOR TODO TASK APP

Always dreaming of making life easier for everyone especially for the working class and moms, its always a big deal. been a mother to kids and even while you are nor might not be working in an office your role is still 1st and best, its often a challenge keeping track of things we want to do either in the office , visiting friends or buying that special thing for our loved once. this is where this Todo App come in . to make life easier for both the young and elderly. its easy features make it very understandable and convinent to use.

![Responsive website image](staticfiles/image/todo-responsive-design.png)

Visit the live site [Here.](https://ckz8780-django-task-app-2295e6f698e4.herokuapp.com/"Link to Anyiador Todo Task App")

---

## CONTENTS

* [Project Overview](#project-overview)
  * [Project Goals](#project-goals)

* [User Experience](#user-experience)
  * [User Expectations](#user-expectations)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Imagery](#imagery)
  * [Structure](#structure)
  * [Database Design](#database-design)
  * [Wireframes](#wireframes)

* [Agile Project Management](#agile-project-management)

* [Features](#features)

* [Future Implementations](#future-implementations)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Programs Used](#programs-used)

* [Deployment](#deployment)

* [Testing](#testing)

* [Credits](#credits)
  * [Code used and adapted](#code-used-and-adapted)
  * [Websites visited for info and solutions](#websites-visited-for-info-and-solutions)
  * [Acknowledgments](#acknowledgments)

---
## Automated Testing

### **W3C HTML Validator**

The [HTML W3C HTML Validator](https://validator.w3.org/#validate_by_uri+with_options) was used to validate the HTML code used, showing no errors except on single report page, 'strike' element is obsolete. As this is a feature (text censoring from admin site) and works as intended.



 - Login
 <br>

 ![Login](staticfiles/image/w3c_html_check.png)

 - SignUp
 <br>

 ![Signup](staticfiles/image/w3c_html_signup.png)

- Task Page
 <br>
 ![Task page](staticfiles/image/w3c_taskpage.png)

 - Create Task
 <br>

 ![Create Task](staticfiles/image/w3c_createtask.png)

 - Delete Report
 <br>

 ![Delete Task](staticfiles/image/w3c_deletepage.png)


### **W3C CSS Validator**

The [CSS Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri) was used to validate the CSS code used, showing no errors on the customized style.css, uploaded by direct input.

 - CSS validation
 <br>

 ![CSS Validation](staticfiles/image/w3c_css.png)

### **JSHINT Javascript Validator**

The [JsHint](https://jshint.com/) was used to validate the Javascript code used, showing no errors.

 - Javascript validation
 <br>

 ![Javascript validation](staticfiles/image/jshint.png)

### **CI Python Linter**

The [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the Python code used, showing no errors except for one 'line too long' in settings.py. This could not be resolved despite best efforts.

 - admin.py
 <br>

 ![admin.py](staticfiles/image/python_admin.png)

 - forms.py
 <br>

 ![apps.py](staticfiles/image/python_apps.png)

 - manage.py
 <br>

 ![manage.py](staticfiles/image/python_manage.png)

 - models.py
 <br>

 ![models.py](staticfiles/image/python_mode.png)

 - settings.py
 <br>

 ![settings.py](staticfiles/image/python_settings.png)

 - urls.py
 <br>

 ![urls.py](staticfiles/image/python_url.png)

 - urls.py-project
 <br>

 ![views.py](staticfiles/image/python_view.png)

### **Lighthouse**

The [LightHouse](https://developer.chrome.com/docs/lighthouse/overview/) was used for testing performance.
App is fully responsive and best practice was followed for a great score

#### **Desktop**


 - Login
 <br>

 ![Login](staticfiles/image/lighthouse_login_desktop.png)
 

 - SignOut
 <br>

 ![Signup](staticfiles/image/lighthouse_signup_desktop.png)
 

 - Add Task
 <br>

 ![Create Task](staticfiles/image/lh_addtask_desktop.png)
 

 - Edit Task
 <br>

 ![Edit Task](staticfiles/image/lh_editpage.desktop.png)
 

 - Delete Report
 <br>

 ![Delete report](staticfiles/image/lh_deletepage.desktop.png)
 

#### **Mobile**

  - Login
 <br>

 ![Login Mobile](staticfiles/image/lighthouse_login_mobile.png)

 - SignOut
 <br>

 ![Signup Mobile](staticfiles/image/lighthouse_signup_mobile.png)

 - Add Task
 <br>

 ![Create Task Mobile](staticfiles/image/lh_addtask_mobile.png)

 - Edit Task
 <br>

 ![Edit Task Mobile](staticfiles/image/lh_editpage.mobile.png)

 - Delete Report
 <br>

 ![Delete report Mobile](staticfiles/image/lh_deletepage.mobile.png)

[Back to top ⇧]

---
## **Accessibility**

### **WAVE WebAim**

The [W.A.V.E.](https://wave.webaim.org/) was used to test for accessibility, showing no errors except for a single report page on censored (blacked-out) text. As this is a feature and works as intended.


 - Login
 <br>

 ![Login](staticfiles/image/wave_login.png)

 - SignUp
 <br>

 ![SignUp](staticfiles/image/wave_signup.png)
 

[Back to top ⇧]

---
## **Project Overview**

The idea for this project was to make life easier and to keep everyone in track for their daily / weekly / yearly task they have planned out. as it is general believe "one who fail to plan , has already planned to fail" but the truth is been able to remember your plans and able to track them are the main factor to a successful life. this app help to keep you reminded of all you plans, either about your groceries, your birthday plans, your school project or your leissure this todo app is right for you. its easy to save and delete items off list, you could also have items completed but not deleted for future references .

---

### **Project Goals**

 - Develop Task Todo App using Django and python frameworks
 - Present the App in a clean and easy to understand manner
 - Keep good UX principles regarding layout/colours/interaction
 - Robust Python code without issues/bugs
 - Fully responsive and immersive

[Back to top ⇧](#anyiador-todo-task-app)

---

## **User Experience**

### **User Expectations**

 - Able to quickly understand what the purpose of the site is
 - Responsive across many different devices and screen sizes
 - Able to find basic information and set task
 - Find additional info if needed
 - User-friendly

### **User Stories**

#### **First Time Visitor**
   - I want to know what Task Todo App is
   - I want to navigate the App easily
   - I want to find additional information on how to use
   - I want to check out Control

  #### **Returning User/Agent**
   - I want to log in securely
   - I want to submit my own task
   - I want to see my task
   - I want to modify my task
   - I want to delete my task
   - I want to add my comment to a task
   - I want to complete / delete task
   - I want to access my task

  #### **Website Admin/Director**
   - I want to log in securely and have admin access
   - I want to approve and publish user task
   - I want to see published and approved user
   - I want to modify user task
   - I want to delete user  

[Back to top ⇧]

---

## **Design**

### **Colour Scheme**

the colors used are very warm and visable colors. user friendly



### **Structure**

  - Task todo app is structured in a user friendly and easy to navigate way.

  - *Signup page which also introduce user to the App:*

    - with index page been the signup page with instructions of how to get the best from the app. after which the todo page is opened with a greeting to user, there are add buttons to add a task, edit button to change or modify , the view botton to view what have been written then the delete botton to delete any task that is no longer needed. the user also have the option to complete a task which makes the task color go red.
    -  base template is created with head, navigation and footer being the same on signup and login pages, adding specific page content to it.
    - User can signin and view their already saved task, as the index page give option for users who are already registered to signin to the page.
    

  - *Registerig, logging in/out:*  
    - First time/unregistered user is immediately directed to the signin page on as index page and without an account user can not get through this page. this page also contains links to signup pages.

    - First time user can register on the register page. upon registration user is redirected to the Todo task page,
    - New user get a message after successful registration, "Congratulations, You are now Registered".
    
    - Upon registering, the 'Register' link is replaced by 'Logout' link, allowing the user to sign out from the site.
    - Logged in users will see their username and a greeting displayed in the top left corner, in the style of 'Hello: "username"'.
    - The user can now open the 'Task' and 'create Task' pages.
    - When logging in the user is brought to the Task Todo page .
    - When logging out, the user is asked 'Are you sure' before signing out.
    - When signed out, the user is brought to the index/Signin page.

  - *Footer:*
    - Footer is retained on signup and signin pages and contains information and contact details of the designer .
    - Footer also contains copyright for both this project.
   
  - *Error pages*
    - Two error pages are supported, 404 (page not found) and 500 (internal server error), both with buttons that guide the user back to the home page.   




### **Wireframes**

Wireframes for the project were developed right after the idea for the project was chosen.
Wireframes for Assessment Guide and Project Planning have been added. not much understanding on building and using wireframe but for the sake of the project i have added something

<details>
<summary>Assessment guide wireframe</summary>

![Assessment guide wireframe](staticfiles/image/wireframes.png)
![Assessment guide wireframe](staticfiles/image/flow_chat.jpg)
</details>



## **Agile Project Management**

This project was developed using the Agile methodology.
The key principles adopted were; focus on the essential features first, work in small iterations and add extra features/expand scope as time permitted.


The structure of development was: Milestone => Task/User Story.
Epics were considered as iterations, and all of them contained 9 issues. all issues where planned in the user story and task set completed

Colored text was used when possible (using Tex) for organizing, color-coding and visual distinction.

**Agile Planning**

Before writing any code, everything was considered and planned as much as possible.



1. EPIC - Django Setup and early deployment
2. EPIC - Set up models and views
3. EPIC - User registration/login, CRUD
4. EPIC - Content and navigation - basic
5. EPIC - Content and navigation beautify/Testing

6. EPIC - Logic/functionality enhancements
7. EPIC - Ux/content enhancements

8. EPIC - Logic/functionality enhancements
9. EPIC - Ux/content enhancements

10. EPIC - README update and finish up
</details>




### **Home**

<details>
<summary>Index page is the login page for user and unregistered users can easily click on the register now button to get registered for access</summary>

![Unregistered user modals](staticfiles/image/Homepage)
</details>

### **Sign Up**

<details>
<summary>Cross-links between Sign-up and Log In</summary>

![Cross-links between Sign-up](staticfiles/image/signup_page.png)
</details>

<details>
<summary>Successful registering success message</summary>

![Successful registering success message](staticfiles/image/registration_confirmation.png)
</details>

### **Log In/Out**

<details>
<summary>Successful login success message, Agent name in top right corner</summary>

![Successful login success message, Agent name in top right corner](staticfiles/image/login_greeting.png)
</details>



<summary>Sure you want to log out page, logging out success message, no Agent name in top right corner</summary>

![Sure you want to log out page, logging out success message, no Agent name in top right corner](staticfiles/image/signout_confirmation.png)
</details>


### **Admin page**

<details>
<summary>Admin can approve and publish report, visible on Reports page to a normal user</summary>

![Admin can approve and publish report, visible on Reports page to a normal user](staticfiles/image/admin_page.png)
</details>


## **Future Implementations**

The following features could be added to Task Todo in the future. .

  - Adding social account to the signup and login page to make easier for users to login and register.
  - Wireframe design could have been improved on
  - more feautures could be added to the task App


[Back to top ⇧](#anyiador-todo-task-app)

---

## **Technologies Used**

### **Languages Used**

- [HTML](https://en.wikipedia.org/wiki/HTML5) - For adding content and formatting.
- [CSS](https://en.wikipedia.org/wiki/CSS) - For adding style and colours.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - For adding interactive features.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - High-level, general-purpose programming language.

### **Django and Python Packages**

- [Django](https://www.djangoproject.com/) - A Python-based web framework that follows the model-template-view architectural pattern, used for building the project.
- [django-allauth](https://django-allauth.readthedocs.io/) - A Django application used for account registration, management, and authentication.
- [cloudinary_storage](https://cloudinary.com/) - A Django storage backend for Cloudinary, used for image hosting and storage.
- [django_summernote](https://django-summernote.readthedocs.io/) - A Django application that integrates the Summernote WYSIWYG editor into Django projects.
- [crispy_forms](https://django-crispy-forms.readthedocs.io/) - A Django application that makes it easy to style Django forms.
- [crispy_bootstrap5](https://pypi.org/project/crispy-bootstrap5/) - A package that provides Bootstrap 5 styling for Django crispy-forms.

### **Programs/Tools Used**

- [GitHub](https://github.com/) - Source code hosted on GitHub, deployed using Git Pages.
- [GitPod](https://www.gitpod.io/) - Used to commit, comment and push code during the development process.
- [Font Awesome](https://fontawesome.com/) - Font Awesome use dto source necessary icons used in the project.
- [Google Keep](https://keep.google.com/) - Used to make notes during the project duration.
- [Google Fonts](https://fonts.google.com/) - Used to import fonts to the project.
- [GifCap](https://gifcap.dev/) - Used to capture gif-s of the project .
- [Heroku](https://www.heroku.com/) - Used to deploy the project.
- [ElephantSQL](https://www.elephantsql.com/) - Free and open-source relational database management system (RDBMS).
- [JsHint](https://jshint.com/) - Used for validating the javascript code.
- [CI Python Linter](https://pep8ci.herokuapp.com/#) - Used for validating the python code.
- [HTML W3C HTML Validator](https://validator.w3.org/#validate_by_uri+with_options) - Used for validating the HTML.
- [CSS Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri) - Used for validating the CSS.
- [Chrome Del Tools](https://developer.chrome.com/docs/devtools/) - For debugging the project.
- [W.A.V.E.](https://wave.webaim.org/) - Used for testing accessibility.
- [LightHouse](https://developer.chrome.com/docs/lighthouse/overview/) - Used for testing performance.

[Back to top ⇧](#anyiador-todo-task-app)

---

## **Deployment**

- Clone Code Institute Template Repository
- Initialize GitPod Workspace by clicking on the GitPod button on the repository
- Install support libraries and Django according to the guide on Code Institute
- Create requirements.txt
- Create Django project
- Set up ElephantSQL Account
- Set up Cloudinary Account
- Create env.py to hold sensitive data
- Create Heroku app
- For the final deployment, the debug setting in settings.py must be set to false
- Before final deployment, the DISABLE_COLLECTSTATIC config var in Heroku was removed
- From Heroku connect to github repository 
- Deploy from selected GitHub branch
- Click on Deploy button => project is now deployed.

An early deployment guide was made before project start to ensure success in creating the project:
<details>
<summary>Early deployment guide</summary>

---

Create repo as usual, from template

Create user stories/issues - LOOK UP PREVIOUS GUIDE ABOUT PROJECTS/about milestones etc

GITPOD

IF ERROR BUILDING IMAGE - REFRESH PAGE
- pip3 install 'django<4' gunicorn
- pip3 install dj_database_url==0.5.0 psycopg2
- pip3 install dj3-cloudinary-storage
- pip3 freeze --local > requirements.txt

=====  DONT FORGET THE FULL STOP  ====

<django-admin startproject PROJ_NAME .>   


python3 manage.py startapp APP_NAME

=== in settings.py, to INSTALLED_APPS array, add APP_NAME

python3 manage.py migrate

python3 manage.py runserver  ===> for TESTING, should see django install congrats

DO NOT COMMIT

HIDING SECRET KEY
- Create File => .env
- Cut this from settings.py =>
- SECRET_KEY = '-----your secret key-----'
- Paste in .env
- Write this in settings.py =>
- from decouple import config
- SECRET_KEY = config("SECRET_KEY")
- Write this in terminal or cmd =>
- pip install python-decouple

FOLLOW HEROKU INSTRUCTIONS

FOLLOW ESQL INSTRUCTIONS

in env.py 
- import os
- os.environ["DATABASE_URL"]="<copiedURL>"     === url from ESQL
- os.environ["SECRET_KEY"]="my_super^secret@key"    === Django Secret key

in settings.py
- import os
- import dj_database_url
- if os.path.isfile('env.py'):
- import env

replace Django secret with === SECRET_KEY = os.environ.get('SECRET_KEY')

replace this:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
  }
}
```
with this:
```
 DATABASES = {
     'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
 }
```

!!! IMPORTANT  -  CTRL+S everything

python manage.py migrate

CONNECTION CHECK ON ESQL

Add, commit, push
RE CHECK python3 manage.py runserver

Add secret key and secret database to heroku config vars, key=PORT value=8000

Cloudinary
- in env.py do 
- os.environ["CLOUDINARY_URL"] = 'API_KEY_HERE'
- add it to Heroku config vars
- add to Heroku config vars:
- key=DISABLE_COLLECTSTATIC    value=1


to INSTALLED_APPS in settings.py add:
```
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'blog',
```

below STATIC_URL = '/static/'  add
- STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
- STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
- STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

- MEDIA_URL = '/media/'
- DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

below BASE_DIR = Path(__file__).resolve().parent.parent add
- TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

update to this:
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

update ALLOWED_HOSTS = ['<APP NAME>.herokuapp.com', 'localhost']

CREATE FOLDERS
- media, templates, static

create Procfile and put === web: gunicorn codestar.wsgi

git add, commit and push

deploy from Heroku via GitHub.
</details>

[Back to top ⇧]

---

## **Testing**

Testing information can be found in a separate testing file [TESTING.md](/TESTING.md).

[Back to top ⇧]

---

## **Credits**

### **Code used and adapted**


 - All characters, events and situations depicted (except for user self-made entries) are products of and copyrighted by [Remedy Entertainment Plc](https://www.remedygames.com/).

 - Code Institute guide/lessons were heavily relied on while working on development, mainly for the back-end. After the back end was developed the front end was adjusted.

 - [Django documentation](https://docs.djangoproject.com/en/4.2/) was relied on to find code for back-end solutions and code.

 - How do create url to django Admin within user page (HTML), code found on [Stack Overflow](https://stackoverflow.com/questions/55917136/how-do-create-url-to-django-admin-within-my-user-page-html).

 - Error pages how-to, found [here](https://frontendshape.com/post/bootstrap-5-404-page-examples) and [here](https://studygyaan.com/django/how-to-use-custom-500-error-template-in-django).


 - Adding Social Authentication to Django, found [here](https://testdriven.io/blog/django-social-auth/).

 - Changing Text Animation CSS, found on [CodePen](https://codepen.io/codingyaar/pen/LYJQaBe).

 - Censor Bars Text Animation For Del Text, found [here](https://codemyui.com/censor-bars-%E2%96%88%E2%96%88%E2%96%88%E2%96%88-text-animation-for-del-text/).

 - CSS 3D Rotate Animation, found on [CodePen](https://codepen.io/sungaila/pen/LzMgjE).


### **Websites visited for info and solutions**

There were many sites visited during the duration of the project.
[Google](https://google.com/ "Google home page") was used to produce results of the specific query, and [Stack Overflow](https://stackoverflow.com/ "Stack Overflow home page") proved to be the best source of information for various queries/issues. 

Standouts are [Django documentation](https://docs.djangoproject.com/en/4.2/), [Bootstrap documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/) and [Django-blog](https://djangocentral.com/building-a-blog-application-with-django/) that helped immensely.

A lot of other projects were looked into to help with development, standouts are [ Destiny Franks (Desphixs)](https://www.youtube.com/@desphixs/about), [BError By Night](https://www.youtube.com/watch?v=0VF5twldC2Y&t=3147s).

I watched some of the videos from (https://www.youtube.com/@desphixs/about)

###  **Acknowledgments**

This whole project is dedicated to my family who in the most difficult position we faced through out my coding career have remained strong and supportive to me. its has been a long ride and we have faced alot of storms, most bitter part of out life so far but in all we are always gratfuly to our Lord and saviour Jesus Christ for giving us the streight and grace to come out of everything.
- To my wife, thank you for your support and cheering me on, lifting me back up when it got hard. Thank you for taking care of all the housework and food, children and numerous other responsibilities while I was busy with full time job and doing this project on the side. Without you this journey would never be possible. And when it got hard and complicated, you never gave up on me and this dream of career change.
- To Shalon my beautiful girl. Thank you for being so understanding during the project work. Thank you from the bottom of my heart for being who you are, wonderful and delightful souls. You make me proud to be your dad.

- Special mentions to Destiny Franks (Desphixs) thank you so much for been there for me every single step of this project this is all to you . i am gratful for your kindness and understanding. you where the back born to this project success. 
- To Error By Night thanks alot for showing me the light and helping to answer my questions. i am gratfult for the team at discord for all your support.
- To my most amazing Coach/co-student Tomislav_5P. i am not sure what to say to you for always making yourself available to answer and see me succeed. you have become more of a brother that i have never met . you love and support is truly appreciated. you will always be so special to me for there is no way i will write my coding career success without you on the front page.
- To student support (Sarah) i got fedup of using this feature but when i was able to get in contact with you , you showed me i have missed alot for not using it. i am gratful for you help and patient.
- Student support of Code Institute, thank you for granting the project deadline extension, it was much needed and appreciated.
- 
- Special thanks to Bojan Bakaric (co-student) whose Readme for project (FEDERAL BUREAU OF CONTROL) was used as a template for my readme. thanks alot for your support and advise.


[Back to top ⇧]

***
# Update

Changed Number Sequence For Semseter
1 for spring and 2 for fall to fetch transcript in acsendong order


# QRSMS-V1.65

To start a semester, Create semester object. Add Courseloads. Run following methods.
- make_semester()
- make_elective_semester()
- pre_offer()
- offer_core_courses()
- offer_elective_courses()

To alot a Teacher to a Course Section. Use Admin Portal.
Make sure that teacher User Object has is_teacher == True

# QRSMS-V1.50

> **The Big Update is here.**

For Course API:
course_type =  1 refers to Core Course.
course_type =  2 refers to Core Elective.
course_type =  3 refers to Core Elective(X).

Djnago Signals would certainly improve efficiency and reliability, but due to time constraints we resort to some very promiscuous functions such as 

    Semesterinstance.make_semeter() 
    Semesterinstance.pre_offer()
    CourseStatusinstance.save() # Over-ridden Method

After 1 hour:
I ended up setting up signals for attendance and marks tables generation. :P 
signals.py holds all the signals.

PostgreSQL Database Added, Use SQLite in development:
To Dump Pre-existing Data:

    python manage.py dumpdata --natural-foreign --exclude auth.permission --exclude contenttypes --indent 4 > dump2.json

To Load json in DB:

    python .\manage.py loaddata dump2.json


**Links:** 
Will check if dumpdata continues to fail me.
[https://django-extensions.readthedocs.io/en/latest/dumpscript.html](https://django-extensions.readthedocs.io/en/latest/dumpscript.html)

[https://django-configurations.readthedocs.io/en/latest/](https://django-configurations.readthedocs.io/en/latest/)

[https://dev.to/coderasha/how-to-migrate-data-from-sqlite-to-postgresql-in-django-182h](https://dev.to/coderasha/how-to-migrate-data-from-sqlite-to-postgresql-in-django-182h)

[https://tutorialinux.com/today-learned-migrating-sqlite-postgres-easy-sequel/](https://tutorialinux.com/today-learned-migrating-sqlite-postgres-easy-sequel/)


# QRSMS-V1.49
Actor.models holds CURRENT_SEMESTER and CURRENT_SEMESTER_CODE, necessary for registration into started semester. Will be updated to a Singleton Class.

**Links:**

[https://blog.bam.tech/developer-news/redux-persist-how-it-works-and-how-to-change-the-structure-of-your-persisted-store](https://blog.bam.tech/developer-news/redux-persist-how-it-works-and-how-to-change-the-structure-of-your-persisted-store)

[https://stackoverflow.com/questions/5036357/single-django-model-multiple-tables](https://stackoverflow.com/questions/5036357/single-django-model-multiple-tables)  
[http://chris.photobooks.com/json/](http://chris.photobooks.com/json/)

https://stackoverflow.com/questions/33795000/subclass-django-modelbase-metaclass-for-django-models
https://dynamic-models.readthedocs.io/en/latest/pdfindex.html

# QRSMS-V1.48
Added Endpoints for Login and Logout. Student Also has a Signup Endpoint.

Endpoint Structures are as follows 
**Student:**

    POST(username, password) -> /student/login/ -> RESPONSE-Success -> {'status':'success','message'  :  'User Logged In',  **user}
    
    POST -> /student/logout/ -> RESPONSE-Success ->
    {'status':'success','message'  :  'User Logged Out'}
    
    GET -> /student/home_json/ -> RESPONSE-Success ->
    {'status':'success',**data_dict,**user_data}

**Teacher:**

    POST(username, password) -> /teacher/login/ -> RESPONSE-Success -> {'status':'success','message'  :  'User Logged In',  **user}
    
    POST -> /teacher/logout/ -> RESPONSE-Success ->
    {'status':'success','message'  :  'User Logged Out'}
    
    GET -> /teacher/home_json/ -> RESPONSE-Success ->
    {'status':'success',**data_dict,**user_data}

**Faculty:**

    POST(username, password) -> /faculty/login/ -> RESPONSE-Success -> {'status':'success','message'  :  'User Logged In',  **user}
    
    POST -> /faculty/logout/ -> RESPONSE-Success ->
    {'status':'success','message'  :  'User Logged Out'}
    
    GET -> /faculty/home_json/ -> RESPONSE-Success ->
    {'status':'success',**data_dict,**user_data}



# QRSMS-V1.47
Folder Hierarchy is First Git Clone the QRSMS-v1(Backend). Open it and inside it Git Clone the QRSMS-Front(Frontend). This is ensures proper working of webpack.

A User Education History Model Needs to be designed (Relegated to Version - 2). That will hold student/teachers Educational Background such as marks in Matric, FSC, Certificates and Publications.

Details of Changes are relegated to v1.50.

**links:**

[https://github.com/Nifled/drf-cheat-sheet](https://github.com/Nifled/drf-cheat-sheet)



# QRSMS-V1.46
User and Account management logic will be confined to Actor App.
Three new apps also have been constructed,

 - student_portal
 -  teacher_portal
 -  faculty_portal

For interaction with these apps respective Apis are:

    /student
    /teacher
    /faculty

On requesting any view that the client does not have permission for a JSON Object will be returned currently of the following structure.

    {'message':'Not Authenticated'}
   
  Sending valid status codes is responsibility of back-end devs, Frontend Dev needs to check status messages.
  Http-middleware-proxy dependency is added to initial_frontend. Helps in various issues of proxying requests. 

**links:**

React Patterns:
[https://reactpatterns.com/](https://reactpatterns.com/)


for changing axios base url:
[https://alligator.io/react/axios-react/](https://alligator.io/react/axios-react/)

setting env variables in js

[https://stackoverflow.com/questions/4870328/read-environment-variables-in-node-js](https://stackoverflow.com/questions/4870328/read-environment-variables-in-node-js)

http proxy middleware
[https://medium.com/@Pavan_/set-up-proxy-to-work-with-multiple-apis-in-create-react-app-be595a713eb2](https://medium.com/@Pavan_/set-up-proxy-to-work-with-multiple-apis-in-create-react-app-be595a713eb2)

noman bhai check this:
[https://docs.djangoproject.com/en/2.2/topics/conditional-view-processing/](https://docs.djangoproject.com/en/2.2/topics/conditional-view-processing/)

[https://stackoverflow.com/questions/4597401/django-user-permissions-to-certain-views](https://stackoverflow.com/questions/4597401/django-user-permissions-to-certain-views)

react, django ,cors
[https://medium.com/@zoltankohalmy/react-and-django-57f949b0f012](https://medium.com/@zoltankohalmy/react-and-django-57f949b0f012)

if all else fails
[https://medium.com/@praveen.beatle/avoiding-pre-flight-options-calls-on-cors-requests-baba9692c21a](https://medium.com/@praveen.beatle/avoiding-pre-flight-options-calls-on-cors-requests-baba9692c21a)





# QRSMS-V1.45
Added RegularCoreCourseload, Updated several Mangagement Functions. Added courses with thier credit hours and option to add pre-Requisities.

Ahsan can login using
    /test_student_login
Signup using
    /test_signup_view
and see student details using
    /home_json

**links:**

https://www.revsys.com/tidbits/tips-using-djangos-manytomanyfield/

https://www.webforefront.com/django/setuprelationshipsdjangomodels.html

https://docs.djangoproject.com/en/2.2/topics/db/sql/





# QRSMS-V1.44
Dummy Data inserted for students, Management Commands setup to quickly run scripts relating to Django data and debug. 
Crispy Forms inserted that provide quick and simple manipulation(Though we wont use it fully). It allows us to write basic HTML forms that are then beautified using Bootstrap.
 Student Table has been extended with several attributes. 
No work could be done on Front-end React Components. 

**Links:** 

https://rogerdudler.github.io/git-guide/

https://www.mockaroo.com/schemas/192990

Nouman Bhai specially check this:

https://mmcardle.github.io/django_builder/#!/home

Redux Reading Material :

[https://blog.bitsrc.io/react-communication-between-components-c0cfccfa996a](https://blog.bitsrc.io/react-communication-between-components-c0cfccfa996a)  
  
[https://towardsdatascience.com/passing-data-between-react-components-parent-children-siblings-a64f89e24ecf](https://towardsdatascience.com/passing-data-between-react-components-parent-children-siblings-a64f89e24ecf)  
  
[https://medium.com/tkssharma/react-js-new-context-api-for-data-passing-fa4bb952862f](https://medium.com/tkssharma/react-js-new-context-api-for-data-passing-fa4bb952862f)  
  
[https://dev.to/email2vimalraj/react-hooks-lift-up--pass-down-state-using-usecontext-and-usereducer-5ai0](https://dev.to/email2vimalraj/react-hooks-lift-up--pass-down-state-using-usecontext-and-usereducer-5ai0)  
  
[https://medium.com/javascript-in-plain-english/the-only-introduction-to-redux-and-react-redux-youll-ever-need-8ce5da9e53c6](https://medium.com/javascript-in-plain-english/the-only-introduction-to-redux-and-react-redux-youll-ever-need-8ce5da9e53c6)  
  
[https://medium.com/javascript-scene/do-react-hooks-replace-redux-210bab340672](https://medium.com/javascript-scene/do-react-hooks-replace-redux-210bab340672)  
  
[https://jaketrent.com/post/remove-array-element-without-mutating/](https://jaketrent.com/post/remove-array-element-without-mutating/)

# QRSMS-V1.43

    login_type:props.user_type  ==  undefined  ?  "Undefined User Login"  :  props.user_type,

four user types:
admin : 0, faculty : 1, teacher : 2, student : 3

**links:**


[https://learnwithparam.com/blog/how-to-pass-props-in-react-router/](https://learnwithparam.com/blog/how-to-pass-props-in-react-router/)

[https://blog.pshrmn.com/simple-react-router-v4-tutorial/](https://blog.pshrmn.com/simple-react-router-v4-tutorial/)

[https://codeburst.io/getting-started-with-react-router-5c978f70df91](https://codeburst.io/getting-started-with-react-router-5c978f70df91)

[https://www.freecodecamp.org/news/beginner-s-guide-to-react-router-53094349669/](https://www.freecodecamp.org/news/beginner-s-guide-to-react-router-53094349669/)




# QRSMS-V1.42
minor changes to Front HomePage.


**links**:
Ahsan please check these out.
--React Forms, 
[https://blog.stvmlbrn.com/2017/04/07/submitting-form-data-with-react.html](https://blog.stvmlbrn.com/2017/04/07/submitting-form-data-with-react.html)

[https://www.freecodecamp.org/news/learning-react-roadmap-from-scratch-to-advanced-bff7735531b6/](https://www.freecodecamp.org/news/learning-react-roadmap-from-scratch-to-advanced-bff7735531b6/)

[https://dev.to/amanhimself/using-react-router-to-optimize-single-page-applications-4mim](https://dev.to/amanhimself/using-react-router-to-optimize-single-page-applications-4mim)

[https://www.freecodecamp.org/news/the-react-handbook-b71c27b0a795/](https://www.freecodecamp.org/news/the-react-handbook-b71c27b0a795/)

[https://medium.com/the-many/adding-login-and-authentication-sections-to-your-react-or-react-native-app-7767fd251bd1](https://medium.com/the-many/adding-login-and-authentication-sections-to-your-react-or-react-native-app-7767fd251bd1)

[https://medium.com/@zoltankohalmy/react-redux-router-authentication-e8a77107db46](https://medium.com/@zoltankohalmy/react-redux-router-authentication-e8a77107db46)

[https://www.freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-4b12e369d10/](https://www.freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-4b12e369d10/)

[https://dev.to/amanhimself/using-react-router-to-optimize-single-page-applications-4mim](https://dev.to/amanhimself/using-react-router-to-optimize-single-page-applications-4mim)

[https://stackoverflow.com/questions/44232828/folder-structure-for-react-and-django-rest](https://stackoverflow.com/questions/44232828/folder-structure-for-react-and-django-rest)

[https://hackernoon.com/serving-react-and-django-together-2089645046e4](https://hackernoon.com/serving-react-and-django-together-2089645046e4)

# QRSMS-V1.41
fixed webpack fonts issue. implemented a preliminary version of ahsans sign in page. 
**links:**
[https://github.com/owais/django-webpack-loader](https://github.com/owais/django-webpack-loader)

[https://www.sitepoint.com/beginners-guide-webpack-module-bundling/](https://www.sitepoint.com/beginners-guide-webpack-module-bundling/)

[http://www.cdrf.co/](http://www.cdrf.co/)

[https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/](https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/)

[https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api](https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api)

[https://medium.com/backticks-tildes/lets-build-an-api-with-django-rest-framework-part-2-cfb87e2c8a6c](https://medium.com/backticks-tildes/lets-build-an-api-with-django-rest-framework-part-2-cfb87e2c8a6c)

[https://wsvincent.com/django-rest-framework-authentication-tutorial/](https://wsvincent.com/django-rest-framework-authentication-tutorial/)

[https://medium.com/capital-one-tech/how-to-work-with-forms-inputs-and-events-in-react-c337171b923b](https://medium.com/capital-one-tech/how-to-work-with-forms-inputs-and-events-in-react-c337171b923b)


# QRSMS-V1.4
Separated University, Campus, Department, Degree Classes to 'institution' app. 
CSRF Authentication ready to be implemented.
Session management needs to be worked on.
Included Ahsans Login Page to code base.

**links**:
[making-react-and-django-play-well-together-single-page-app-model](https://fractalideas.com/blog/making-react-and-django-play-well-together-single-page-app-model/)

[session-handling-in-react-with-redux-express-session-and-apollo-18j8](https://dev.to/tmns/session-handling-in-react-with-redux-express-session-and-apollo-18j8)

[local-storage-react](https://www.robinwieruch.de/local-storage-react)

[https://stackoverflow.com/questions/42420531/what-is-the-best-way-to-manage-a-users-session-in-react](https://stackoverflow.com/questions/42420531/what-is-the-best-way-to-manage-a-users-session-in-react)

[https://ltslashgt.com/2007/07/08/one-model-many-db-tables/](https://ltslashgt.com/2007/07/08/one-model-many-db-tables/)

[https://stackoverflow.com/questions/5036357/single-django-model-multiple-tables](https://stackoverflow.com/questions/5036357/single-django-model-multiple-tables)


# QRSMS-V1.3

Some changes have been made to `UserAdmin` to allow us to interact with new attributes of `User` in Django Admin.  
Added Django-Restful-admin. This will allow for admin access and manipulation to our React App Using Axios.
New Endpoint for this is as follows:

[*/rest_admin*](http://qrsms-v1.herokuapp.com/rest_admin)

This will branch into different models that are registered in admin.py file.

**links:**
Ahsan can ignore these.
[https://pypi.org/project/django-restful-admin/](https://pypi.org/project/django-restful-admin/)

[https://medium.com/agatha-codes/options-objects-customizing-the-django-user-model-6d42b3e971a4](https://medium.com/agatha-codes/options-objects-customizing-the-django-user-model-6d42b3e971a4)

[https://stackoverflow.com/questions/15012235/using-django-auth-useradmin-for-a-custom-user-model](https://stackoverflow.com/questions/15012235/using-django-auth-useradmin-for-a-custom-user-model)

[https://docs.djangoproject.com/en/2.2/ref/contrib/admin/actions/](https://docs.djangoproject.com/en/2.2/ref/contrib/admin/actions/)

[https://docs.djangoproject.com/en/2.2/ref/contrib/admin](https://docs.djangoproject.com/en/2.2/ref/contrib/admin)

[https://docs.djangoproject.com/en/2.2/topics/auth/customizing/](https://docs.djangoproject.com/en/2.2/topics/auth/customizing/)




# QRSMS-V1.2

  

**Moving Onwards**

The basic Django **User** model was replaced with **AbstractUser** that we will will used to create accounts for Students, Teachers and Faculty Members.

The Current Users had to be deleted and recreated(multiple times😢).

  
  
  
  

**Links:**

[Django Model Structure](https://simpleisbetterthancomplex.com/tips/2018/02/10/django-tip-22-designing-better-models.html)

[Models, Fields, Mangers, QuerySets, Backends Intro](https://medium.com/@jairvercosa/manger-vs-query-sets-in-django-e9af7ed744e0)

  

[Django QuerySets](https://simpleisbetterthancomplex.com/tips/2016/08/16/django-tip-11-custom-manager-with-chainable-querysets.html)

[Multiple User Models](https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html)

[Django Custom Authorization](https://docs.djangoproject.com/en/2.2/topics/auth/customizing/#auth-custom-user)

  

[Serializers](https://medium.com/better-programming/how-to-use-drf-serializers-effectively-dc58edc73998)









# QRSMS-V1

  

**Starting Project**

  

*Current Application link* : [https://qrsms-v1.herokuapp.com/](https://qrsms-v1.herokuapp.com/)

This is extensively articulated because I tend to forget things, so this will help us all to document everything as we go through.

  

python .manage.py createsuperuser --email admin@hassan11196.com --username admin11196

  

password:

  

Two More Super Users Have been added.

  

**admin3755**

  

**admin3650**

  

Currently All models are in initial phase and database is SQLite. Our file management system is ephemeral. Which means that all changes that you make last as long as you keep the session active. We will move on to more permanent solutions as we progress.

  

Please read about naming conventions such as Camel Case,Pascal-Case,snake_case etc.

  

Please read about cookies and how basic auth works with authorization header. We will possibly shift to Oauth later on in the project.

  

All Endpoints as of version 1 require admin login. This will be processed using basic auth.

  

Current Endpoints are

  

- /admin

  

- /course_info

  

- /api-auth/login

  

- api-auth/logout

  

I suggest you play around with **course_info** and **admin** endpoints.

  

I have bundled a basic react app that fetches course using axios, Please learn how api request pagination works. And how to send auth parameters using axios.

  

Please read about web-pack, babel, transpilers. How web-pack bundles. Also read up on how loaders work for web-pack. I wasted too much time on that. CSS loaders are specially tricky to work with. Know the difference between Global CSS and CSS modules.

  

Read about difference between `--save-dev` and `--save` when installing dependencies using `npm`.

  

Nouman Bhai please see how serializers work and how we use the rest framework view-sets. and django-webpack-loader.

  

**How To Build and Run Project:**

  

Clone the project into your System.

  

git clone https://github.com/hassan11196/QRSMS-V1.git

  

**For Back-End:**

  

Cd to QRSMS-V1 Folder.

  

Run the Following Command.

  

pipenv shell

  

Cd to QRSMS

  

python manage.py runserver

  

**For Front-end**

  

Open the initial_frontend folder and run the following command to first download dependencies

  

npm install

  

and then to start the webserver.

  

npm start

  

**Set Your Admin Authorization For Front-End.**

  

open the credential.js file in **initial_frontenc/src**

  

  

const credential = {

'REACT_APP_ADMIN_USERNAME':'YOUR ADMIN USERNAME HERE',

'REACT_APP_ADMIN_PASSWORD':'YOURADMIN PASSWORD HERE'

}

  

This is temporary. We will move to more secure methods as we progress.

  

**To build Web Pack Bundles.**

  

./node_modules/.bin/webpack --config webpack.config.js

  

or Alternatively,

  

npx webpack --config .webpack.config.js

  

**links :**

  

[React bundling with Django using Webpack 1

](https://owais.lone.pw/blog/webpack-plus-reactjs-and-django/) [React bundling with Django using Webpack 2

](https://www.easyaslinux.com/tutorials/devops/how-to-setup-reactjs-with-django-steps-with-examples/)

[React bundling with Django using Webpack

](https://medium.com/labcodes/configuring-django-with-react-4c599d1eae63) [React Bootstrap Documentation](https://react-bootstrap.github.io/components/buttons/)  [Django Rest Framework Tutorial](https://medium.com/backticks-tildes/lets-build-an-api-with-django-rest-framework-32fcf40231e5)

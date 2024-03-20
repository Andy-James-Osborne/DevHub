# Devhub- Social Media Site

# Project Overview:

This is a Full-Stack project with the use of django for the framework. I had two weeks to design and create a site. The choosen project was a social media site with the idea to be able to connect user with each for social interaction. Due to the sort time for this project the are a few features that I would include in the next sprint of this project to get it the standard of a full functing site. However I have completed all MVP requirements within the timeframe and used KISS (keep it simple silly) with some features to ensure the site is was ready for deployment.

+ Key Features:
   - Post feed for all users to see.
   - Interactive post feed to show post details once clicked on
   - All users can make their own post once they have logged in
   - Are only able to view the post feed page if not created an account
   - Sign in function allows users to have their own profile page which they can edit themseleves
   - Able to view other user info once logged in in a profile list of other users
   - Users have the ability to edit and delete their own post
   - Users can comment on other users post
   - Users can like other users post
   - Image are able to be upload from their desktop to the image fields in the profile and post forms


<img src="static/images/Social-media.JPG" alt="Image of homescreen" width="900" height="500">

## Index Table

1. [Key Features](#key-features)

2. [UX](#ux)

3. [Wireframes](#wireframes)

4. [Agile Methodolgy](#agile-methodolgy)

5. [User Stories](#user-stories)

6. [Database design](#database-design)

7. [Kanban Board](#kanban-board)

8. [Deployment](#deployment)

9. [Testing](#testing)

10. [Bug Fixes](#bug-fixes)

11. [Credits](#credits)

12. [Frameworks](#frameworks)

13. [Languages Used](#languages-used)

14. [Future Features](#future-features)

15. [Acknoledgements](#acknoledgements)

## UX:
### Design of site
I have kept with simple colours with a white background to make the website stand out without being too bright.
   - #252525
   -  #118cd3
   - #ffc107

+ I have used Bootstraps Primary colours of "btn-primary and btn-warning" throught my website for easy of use not to over complicate the design and aim for a higher functioning website.
+ This was decided early on to able me to focus on the database and functionality of the website. 
+ I also used a cdn simply css to help with styling of the site.
+ I have decided on the Bootstrap font-family that comes as standard as i know this is well tested and will work on most devices and browsers.
+ Also used colour which was selected from the colour wheel.  
<img src="static/images/color-select.JPG" alt="" width="200" height="100">

## Wireframes:
Home page  
<img src="static/images/HomepageDevHub.JPG" alt="Image of homescreen wireframes" width="700" height="500">

Post detail page  
<img src="static/images/PostdetailDevHub.JPG" alt="" width="700" height="500">

Login page  
<img src="static/images/LoginDevHub.JPG" alt="" width="700" height="500">

Logout page  
<img src="static/images/LogoutDevHub.JPG" alt="" width="700" height="500">

Sign up page  
<img src="static/images/SignupDevHub.JPG" alt="" width="700" height="500">

Profile page  
<img src="static/images/ProfileDevHub.JPG" alt="" width="700" height="500">

Profile list page  
<img src="static/images/ProfileListDevHub.JPG" alt="" width="700" height="500">

## Agile Methodolgy:
Before starting this project I tired to keep to the agile methodogy following best practise to planning and working on a project.

To do this User stories were created to be able to get the nessisary designs in place.

After gathering all the user stories put them onto my github repositor to create issue and create them labels and milstones to be organised and set into tasks.

Then make a project board in github projects.

You will see this further down the readme document in the kanban board.

## User Stories:

### Epic User Management:
+ Sign Up- As a user, I want to sign up for an account using my username and a password.  

+ Login- As a user, I want to log in to my existing account.  

+ Logout user- As a user, I want to logout with a are you sure request before logging out.  

+ Notifactions- As a user, I want to receive notifications for confirmation of e.g login/out.  

+ View my profile- As a user, I want to view my profile and see my posts, followers, and following.  

+ Edit my profile- As a user, I want to edit my profile information.  

+ Account shown in nav- As a user, I want to be able to be notified I am in my account by seeing the username in the navbar.  

### Epic Conent Management:
+ Responsive website- As a user, I want to use the site for all devices.  

+ Admin CRUD- As an owner, I want to access the admin of the site to be able to Create/Read/Update/Delete all of the data add to my site.  

+ Delete posts- As a user, I want to delete my posts if I no longer want to share it.  

+ Edit posts- As a user, I want to edit my posts if a mistake was made.  

+ Create a profile- As a user, I want a profile with a username, bio, and profile picture.  

+ Search bar- As a user, I want to search for other users by username.  

### Epic Social Interaction:
+ Comment on post- As a user, I want to comment on posts to share my thoughts or ask questions.  

+ Like posts- As a user, I want to like posts from other users.  

+ Create Posts- As a user, I want to create posts that can include text and images.  

+ View other user profile- As a user, I want to view profiles of other users and see their posts.  

+ DM messages- As a user, I want to send private messages to other users.  

+ Follower feed- As a user, I want to see a feed of posts from the people I follow.  

+ Following users- As a user, I want to follow other users to see their posts in my feed.  

+ Unfollow users- As a user, I want to unfollow users I no longer want to see posts from.  

## Database design
<img src="static/images/DB-design.JPG" alt="" width="700" height="500">

## Kanban Board

<img src="static/images/Kanban-board-for-DevHub.JPG" alt="Image kanban board gitHub" width="900" height="400">  

Link to my github project board  
https://github.com/users/Andy-James-Osborne/projects/9

## Deployment:
### Step 1
1. To deploy the site I had to start by setting up a repository in GitHub.
2. Then opened up my online IDE, I used Gitpod.
3. First thing to do is download django with command pip install django I used the lastest version.
4. Then you will need to install pip install gunicorn
5. Once these where installed I created my project folder with django (django-admin startproject socialproject .)
6. Now create an app in django this is where you will be mostly working in on this project (python manage.py startapp social)
7. Then I installed database (pip install dj_database_url) again i installed the lastest version
8. Also install Cloudinary with two installs (pip install dj3_cloudinary-storage, pip install urllib3)
9. Also don't forget to pip freeze > requirements.txt to store all the requirements in a txt file

### Step 2
1. Added app name to setting.py file in the INSTALLED_APPS = ['social',]
2. Migrate this change with python manage.py migrate
3. Now run your local server (python manage.py runserver)
4. will need to allow your local host by copy the HTTP header. I set mine out like this ALLOWED_HOSTS = ['.gitpod.io', '.herokuapp.com']

### Step 3
1. Now we need to deploy to Heroku by login/ make an account
2. Start a new app
3. Also open a database, the external database i used was ElephantSQL
4. Attach the database to heroku in the config vars
5. Will need to create an env.py file in dicretory so that the database is not published to github.
6. Import the os into the env.py file
7. os.environ["DATABASE_URL"] = "Paste in ElephantSQL database URL"
8. os.environ["SECRET_KEY"] = "Make up your own randomSecretKey"
9. Added 7 and 8 into the env.py file and then add secret key to config vars in heroku settings

### Step 4
1. Now we need to set up settings.py for the new database and secrect key
2. import os
import dj_database_url
if os.path.isfile("env.py"):
import env
3. SECRET_KEY = os.environ.get('SECRET_KEY')
4. Put 3 and 4 into your settings.py file
5. comment out or delete the SQL lite database that come with django
6. Add this in its place 
DATABASES = {
   'default':
   dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
7. Now we need to mirgate the changes again

### Step 5
1. Open cloudinary and get the url from the dashboard
2. Put this into your env.py file os.environ["CLOUDINARY_URL"] ="cloudinary://************************"
3. Heroku now needs the cloudinary url added to the config vars
4. Also add DISABLE_COLLECTSTATIC

### Step 6
1. Go to settings.py again to add cloudinary into installed apps
INSTALLED_APPS = [
…,
'cloudinary_storage',
'django.contrib.staticfiles',
'cloudinary',
…,
]
2. In the settings.py file under the static url add-
STATICFILES_STORAGE =
'cloudinary_storage.storage.StaticHashedCloudin
aryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR,
'static'), ]
STATIC_ROOT = os.path.join(BASE_DIR,
'staticfiles')
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE =
'cloudinary_storage.storage.MediaCloudinaryStor
age'
3. Also make sure templates are set up to settings.py
4. TEMPLATES_DIR = os.path.join(BASE_DIR,'templates')
5. Will also need to add a templates folder the best place to put it is inside your app mine is name social.
6. make sure to add another file inside templates this file needs to have the same name as you app so the path would be social/temaplates/social/
7. This is so django knows where to look for your HTML files.

### Step 7
1. You will also need to add media file and static files into the main directory
2. Now make a Procfile to include web: gunicorn PROJ_NAME.wsgi
3. Now it is all set up make sure to git add, git commit and git push
4. You will also need to go back to heroku into the deploy tab to manually link your github
5. Then in the deploy tab of heroku you will need to deploy branch

### Forking project
1. If you are folking this project make sure that to create a env.py and this is not pushed to github and make sure yours doesn't as well!
2. To do this make sure the env.py file is in .gitignore
3. Also you will need to install all the requirements.txt with the command pip install -r requirements.txt
4. You should be then good to go as long as you have made an heroku account and elephantSQL account
5. You can find the deployed link to the site in your deployments in github

## Testing:

+ You can reference the Testing.md page for a full breakdown of the site manual tests that have been preformed.

## Bug Fixes:

### Production bugs:
+ Logo image: The logo for my website in the top corner was not rendering on the screen. The path from static files was wrong.
   - Solution: Fixed by updating link in the path on the html page inside the img tag was an error in spelling jpg.  
+ Login automatically: Doesn't login automatically once sign up has been completed.
   - Solution: Not fixed, still a bug with site, however the site redirect to login page once sign up so does effect user experience.
+ Image placeholder: No placeholder image for if user does not add a image to the post or profile. 
   - Solution: Not fixed, need to add placeholder image to the project for post creation and profile.
+ Logout confirm: When logging out the user didn't have a confirm to ensure they wanted to logout.
   - Solution: Fixed by added another html page called logout with an extention to my views.py function to enable a request.method = 'POST'.
+ Profile editing: Tried to allow users to edit there profiles once signed up.
   - Solution: Fixed wanted uses to sign up and instantly make a profile. Once they click the profile page edit the image and text fields, had an error on my html page with my POST form as had action='POST' instead of method='POST'.
+ Edit and delete comments: Editing and deleting comment function not working when trying to render into post_detail.html page.
   - Solution: My function in my views.py file works with models if I change the {% if request.user.is_authenticated and post.author == request.user %} to {% if comment %} however this allows every user to edit and delete anyones comment.
+ A tags: My link tags in html for login and sign up do not heighlight to show users they are clickable.
   - Solution: Added text-decoration back to these tags to show user they are clickable.
+ Edit profile: Need information that is already on profile to render in form when edit at the moment the fields are blank when you edit the profile form.
   - Solution: Needed to add this in the if statement of my edit profile views.py function 'form = ProfileForm(instance=request.user.profile)'.
+ Comment on posts: Stop working when added like if statement to post_detail function in my views.py file.
   - Solution: Had to rearrange the if statements in the function as the likes if statement was in wrong position.
### Responsive Testing:
+ Lougout: When testing the responsiveness the logout image is slightly off middle of page.
   - Solution: Add a media queiry so when on moblie view the logout is position center.
+ Profile image: Slightly squashed in mobile view.
   - Added a media queiry so before the image start to get squashed it resizes.
+ Home page buttons: On the home page the buttons on the side of the post feed relocate to the bottom of the page on mobile screens this is because of bootstrap cols.
   - This was a problem due to if the post feed gets very long it would take a long time to find these buttons. Fixed by keeping buttons to side of post on mobile screen.

## Credits:

+ https://www.freepik.com/free-photos-vectors/logo- Freeoik use to source images for logo and user profile pictures
+ https://ui.dev/amiresponsive- To showcase the site for my README.md
+ Git: was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
+ GitHub: is used as the repository for the project's code after being pushed from Git and for UX Kanban Board.
+ Balsamiq: was used to create the wireframes during the design process.
+ Stackoverflow was used to get advice from software developers.
+ Google Gemini: used throughtout the project to read my code and help improve errors. Also used to help plan out my logic and my models.
+ https://www.w3schools.com/django/index.php- Used W3Schol throughout the whole project for reference to django and css.
+ https://developer.chrome.com/docs/lighthouse/pwa/pwa-cross-browser- lighthouse use to see how well the site functions.
+ https://realpython.com/build-a-blog-from-scratch-django/- Real python site use to follow steps to make a basic blog walkthrough.
+ https://www.youtube.com/watch?v=xSUm6iMtREA&t=12577s- Social media app walkthrough with free code camp.
+ https://www.youtube.com/watch?v=FdVuKt_iuSI&t=1915s- Youtube walkthrough for ideas for profile.
+ https://www.youtube.com/watch?v=RhJIMUMJ_Do&t=140s- Youtube walkthrough for static files.
+ https://www.youtube.com/watch?v=CQ90L5jfldw&t=38s- Youtube walkthrough for updating user profile.
+ https://dbdiagram.io/d- To design my database models.

## Technologies used:

+ Git - (git add, git commit -m "" and git push)
+ GitHub - Store code for public access
+ GitPod - online IDE
+ ElephantSQL - Database use to store the website models and user infomation
+ Heroku - To be able to deploy the site
+ Cloudinary - For user to upload their images with cloud store
+ Balsamiq - To design my wireframes
+ WhiteNoise, however had to use python manage.py collectstatic command to enable the css to show in heroku



### Frameworks:

+ Bootsrap 5 - https://getbootstrap.com/
+ Simple css - https://simplecss.org/
+ Django - https://www.djangoproject.com/

### Languages Used

+ HTML
+ CSS
+ Python

## Future Features:

+ DM messages- To enable user to have a connect link to their own private chat room with another users  

+ Follower post feed- To only be able to see the users that you follow post feed

+ Following users- The ability to follow users you are intrested in

+ Unfollow users- The ability to unfollow any users that are no longer of interest.

+ Search bar- To search for a specific username. 

## Acknowledgements

+ Thanks to my fellow Code Institute students for all the support and a special thanks to Ben Fashan for constant support and help for past two weeks of final project.
+ Thanks to Iris Smok for all the constant support.
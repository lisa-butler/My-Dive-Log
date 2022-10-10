# Portfolio-Project 4
## My Dive Log
### This web application was built as portfolio project four in the diploma in software development at the code institute. The web application is intended to be used as a digital log for dives. Divers use paper log books to record their depths, times, locations etc of dives and Diving officers (dive organisers) also use a paper copy to keep track of divers, their buddies and their dive details. This application aims to provide a digital resource to tackle this.


### Lisa Butler


## **[Live Site] (https://lisa-butler.github.io/Portfolio-Project1/index.html)**


------------------------------------------------------------------

## **[Repository](https://github.com/lisa-butler/portfolio-project1)**

------------------------------------------------------------------

## Contnets

 1. [User Experience](#ux)
 2. [Application Features](#features)
 3. [Technology Used](#tech)
 4. [Testing](#testing)
 5. [Bugs](#bugs)
 6. [Deployment](#deploy)
 7. [Credits](#credits)
 8. [Content](#content)



 ![Home Page](assets/images/readme-images/picture1.jpg)

## User Experience

<a name="ux"></a>
### **Pre project planning**

I decided to create this dive log for my project as a digital dive log is not something that is avalible yet but is something that many people would find very useful. I have had this idea for a while so i have enjoyed seeing it coming together.
Pre project planning involved developing user stories, wireframe mock ups, logic flow diagrams and researching some basic styling ideas.
I also researched the software stack to use for this specific project. As it is Django based i was tied to using Django and Python, however, I looked into using React and various alternatives for Bootstrap.

**Strategy:**
Determining the best approach meant investigating the needs of the potential users. This included the needs of the divers logging and reviewing their dives and the diving officers reviewing club logs and club members.

**User stories:**
As a diver:
I want to be able to log into an account so that my dives are password protected.
I want to be able to log a dive, including depth, time, buddy, location etc.
I want to be able to make a note when logging a dive.
I want to be able to edit my logged dives.
I want to be able to delete my logged dives.
I want to be able to review my logged dives in a dive log page.
I want my data to be stored in a database so that it is avalible each time i log into the system.

As a diving officer:
I want to be able to log and review my own dives as a diver.
I want to be able to view all dives logged by members in my club.
I want to be able to view all of my club members.

**Scope:**
The web application should have a clear and consistent layout including navigation and login, logout functionality.
The web application should be accessible on all devices for divers to log their dives on the go.
The web application should have a navigation bar that is self explanitory.
Logging a dive should be as straight forward and quick as possible.
Reviewing logged dives should be simple and easy to view.
Logging in and out should be staright forward and easy to do.
Viewing club logs should be able to be done sepertely from personal logs so that the diving officer can just have one account.
The application should be easy to use and require as few clicks as possible to log a dive quickly after returing from the water.

### **Structural planning**

In order for the web application to achieve these goals it was decided to have three pages avalible for the diver; the Home page, Dive log page and Log a dive page. For the diving officer a fourth page labelled Diving officer was avalible, this consisted of two options, to view the club logs and to view the club members.
There was also a login/logout/register functionality at the top of each page and pages such as dive logs and log a dive required login to acess.

**Home page wireframe utilising Balsamiq**

![Home page wireframe using Balsamiq](log/static/images/balsamiq-home.jpg)

**Home:**
This page should contain an overview of what the purpose of the site is.
The navigation bar should be clear and easy to access.
A prompt to take the diver to the log a dive section and a prompt to view thir log should be present to speed up navigation.
Login and logout functionality should be present with a register option for non logged in users.

**Log a dive:**
This page should contain the same theme as the other pages.
There should be a navigtion bar with the active tag indicated somehow.
The logging functionality should be straightforward and fairly unbounded so that the user can input information in a way that suits them, ie can record two dive buddies if needed, can record depth as 30m or 30 meters or 60 foot etc.
Logging should be quick and effortless for on the go logging.
Hitting log at the bottom of the logging page should take the diver to their logged dives.
This page should not be avalible to users who are not logged in.

**Log a Dive page wireframe utilising Balsamiq**

![Log a Dive page wireframe using Balsamiq](log/static/images/balsamiq-logadive.jpg)

**My logs:**
This page should contain the same theme as the other pages.
This page should display all of the divers logged dives specific to them.
Content fileds from their logged dives such as buddy, depth etc should be visible.
The option to edit or delete these dives should exist.
This page should not be avalible to users who are not logged in.

**Logs page wireframe utilising Balsamiq**

![Logs page wireframe using Balsamiq](log/static/images/balsamiq-log.jpg)

**Diving officer:**
This page should contain the same theme as the other pages.
This page should provide the diving officer with the options to view the club logs or to view the club members.
The club logs hsould contain every dive logged by members of this club with their username visible.
The members section should show all members in the club.
This page should not be avalible to users who are not logged in and to members who do not have staff status.

**Login/Logout/Register:**
Login:
This page should contain a simple input form with username and password inputs.
This page should have the same styles as the other pages in the app.
Clicking login should redirect to the home page when the login is sucessful.
There should be an option for those who are not yet registered to click register now and be redirected to the register page.
Failed login should indicate that the login failed and return the login page again.

**Login page wireframe utilising Balsamiq**

![Login page wireframe using Balsamiq](log/static/images/balsamiq-login.jpg)

Register:
This page should have the same styling as the rest of the application.
It should include a registration form requesting; email, username, first and last names and a password to be entered and confrimed.
There should be an offer to login instead if you already have an account.
There should be prompts as to what should be entered in each input field.
On sucessful registration the user should be redirected to the home page of the app.

Logout:
Selecting logout should redirect the user to a page that cofirms they are logged out.
This page should have the same styling as the rest of the application.
There should be a prompt for the user to login again.

**Logged out page wireframe utilising Balsamiq**

![Logged out page wireframe using Balsamiq](log/static/images/balsamiq-loggedout.jpg)



**Wireframes:**
A wireframe was done for each page of the application using Balsamiq before progressing into developing it.
The basic plan for the application was to keep it as uncluttered and minimalistic as possible while providing the required functionality. As the mean age of divers is generally older, it was intended that the application be as intuitive as possible.
Wireframing helped with deciding on a general look of the application and how it would be navigated by a user, leading to changes in design happening before any coding began.


### **Style**

Background: It was decided to stick with a very basic and modern theme of a white background with content kept neat and centrally placed. This benefitted accessibility as the elderly population in diving who would not be as tech savvy, generally, would have a better chance of navigating the application. A basic icon that was used on an earlier application was selected as this had a nice color pallet and fitted the theme in a visually pleasing way. A small banner of photographs was used to add some life to the quieter pages.

**Color:**
The white background was chosen as it enabled the content to be very legible and to stand out for the user, making the site more navigatable.

The colors eventually selected for use were;

* White #FFF -used for the background.
* Grey #D3D3D3 -used for hover over functions and detailing.
* Teal #008080 -used for heading, sub-headings and buttons.
* Black #000 -used for text as black on white is widely known as the most legible combination of colors.


![Colors in use](assets/images/readme-images/picture4.jpg)

**Fonts:**
The font selected was based on what was clear and easy to read as well as feeling like it was suited for a diving-based theme.
The fonts chosen was;
	-Ubuntu
	-Sans-Serif
The focus of this font being to provide the information in a non-distracting manner that was viable for the visually impaired user or someone trying to use the site on a mobile device.

------------------------------------------------------------------

## Application Features

<a name="ux"></a>

### **Index.html**

**Title:**
The title of the application "My Dive Log" is a link to return the user to the home page of the application, allowing for easier navigation.

**Login/Logout/Register:**
This function sits above the navigation bar to the left on all of the pages in the application. It grey in color and teal on mouseover, keeping with the general color theme of the application.
When the user is not logged in the options on display are Login and Register. When the user is logged in these options are replaced with their username and Logout.

**The navigation bar:**
This is a simple banner containing the four pages inn the application.. As seen below, the active page is depicted by the page heading being teal, while a mouseover changes the color to black indicating it is ready to be clicked on. This navigation bar was taken from the Bootstrap 5 library and ammended for my own use.

![Navigation bar](assets/images/readme-images/picture5.jpg)

**Icon:**
The dive mask icon was used throughout the application to provide a visual contiunation throughout the pages. This is a simple and aesthetically pleasing symbol that reiterated the theme of the application. The round shape contrasts well with the otherwise quite blocky theme.

![Icon](assets/images/readme-images/picture6.jpg)

**Cards:**
The cards containing the prompts to log a dive or view your log are there to provide another way to navigate into these main areas of the application with ease.

**Banner images:**
This trio of images was chosen to form the banner instead of using a single image as they worked well together and provided an appealing insight into the application theme.

![Banner images](assets/images/readme-images/picture7.jpg)

**Footer:**
The footer contains links to various social media; Facebook, Twitter, YouTube and Instagram.
These links are done using Font Awesome icons. The links do not currently go to specific areas within these social medias, however, if this application was to be put into real use, a youtube for videos from dives, an instagram for images and short videos, a facebook for communication and marketing and a twitter for news and marketing would be very beneficial.

![Footer](assets/images/readme-images/picture9.jpg)

### **logadive.html**

**Log a dive form:**
This is a straightforward and easy to naviagte 6 input field form. The user simply inputs their values and hits the Log My Dive button at the bottom. I was tempted when creating this form to have the input of depth and time automatically record as meters and minutes, respectively. I opted against this as i wanted the application to be as versatile as possible. So each input filed has a limit on characters but otherwise the user can input whatever readings they please. This means a diver who had completed a one hour and 30 minute dive doesnt need to write 90minutes and a diver that uses feet rather than meters for their depth can input feet/ft, whatever their prefered annotation is.
This is also beneficial for the buddy section, as a diver generally has only one buddy, i was inclined to have a drop down of other members in the club to select from. However, as someone who regularly dives in a trio, with two buddies, i realised this would limit the usability again, so once again opted to leave it open ended.
Hitting Log my Dive redirects the user to the log page, where they can view their dives.

![Dropdown button](assets/images/readme-images/picture10.jpg)

### **logpage.html**


**My log:**
This is a seven field data table that displays the divers own logged dives. The table is placed on a raised card for asthetic purposes, a theme that is used throughout.
The data is outlined below the headings, giving the diver a view of their dives to date, recorded as they please.
Below the log is an option to Log a dive, this button redirects the user to the log page.


### **diving_officer.html**

This page has the same theme as the home page. It is intended for those with staff status only to view. Staff status has to be applied through the admin tool in django for now, this is something that would be changed if i had more time and scope for this projects development.
The diving officer home page gives the diving officer access to the members who are registered on the application and to all of their logs.

**Club Logs:**
This page is very similar to the personal logs page. It displays the dives logged by all divers, their username is present to indicate who logged each dive.

**Members:**
This page has the same card theme as the log page. It contains a list of the users username, first name, last name and email.

![Contact Form](assets/images/readme-images/picture16.jpg)

### **base_generic.html**

This html file contains all of the base features for each page of the application, reducing duplication significantly throughout the code.


### **login/logout/register**

**Login:**
This page contains the same theme as the other pages, complete with the image banner from the home page.
The login form is on a raised card and has fields for username and password. When the user clicks login, it redirects to the home page (index.html)

**Logout:**
When logout is clicked in any of the pages in the application it directs the user to the logout page, which simply indicates that the user is logged out and gives them the option to login again.
Clicking login will redirect to the login page.

**Register:**
This page contains a registration form that the user fills out. The form will return an error if the user inputs the wrong details, ie. spaces where they shouldnt be/wrong characters in passwords/passwords dont match. When the user has correctly filled out the form they are redirected to the home page of the app.


**Further features I would implement:**

If I was to build this application again with the intentions of it being a live application, there are several additional features i would implement;

* Multiple Clubs: As the application is at present, it can cater for one individual club. I would 	like the option for the user to select their club from a dropdown when registering and to be alloted into this club grouping in the admin section. The DO from each club would then have access to only his club members dives.
* Filtering the dive logs: As this is a basic project version of the application i havent input a method to filter the divers by date, year, site, buddy etc. These are things i would like to have if it was a live application.
* Pagination of logs: Similarly, if the log became too full, scrolling through the logs would get a bit tedious and the page would become extremly long (a diver can log 100 or so dives in each year). So i would be implementing pagination after approximately 20 dives, allowing the diver to click through. Having a year and month subheading/seperation of the dives would also help to keep things neater.
* User profile: I would like the option for the user to have a profile where they can see their total dives logged, most frequent buddy, average dive time, most frequent location etc. A general option to change their details, such as diver grade, email etc and to view their stats would greatly enhance the app.
* Map: A map with pins of all of the divers dive locations and number of dives on it would really give a more interractive feel to the application.
* Options to do buddy linking: Similar to the application Strava, i would like if the diver could log a dive and when he selects a certain diver as his buddy, it notifies the buddy that "X has logged a dive with you, add to your log?".
* Diving officer can delete members: I would like the diving officer to have the power to delete a diver from their club members list if they are no longer active etc.

------------------------------------------------------------------


## Technologies Used

<a name="tech"></a>

### **Languages**

The languages used in this project were;

* HTML5
* CSS3
* Python3

### **Frameworks/Libraries/programs:**

* Django 3.2.15: The main framework used for developing the functionality of the application.
* Bootstrap 4: Used for style and fucntion of the application.
* Django Contrib Auth: Used for the login functionality and user registration within the app.
* Django Crispy Forms: Used for customising forms created in the app.
* Whitenoise: Used to serve static image files for the decoration of the application.
* Postgres: Functions as the primary database for this application, to store users data.
* Gunicorn: Used to serve WSGI apps, such as this, especially when there are multiple instances of said app running at one time.
* Font Awesome: Used for icons in the social media bar and the edit/delete functions.
* Google Fonts: Ubuntu was used for the main content of the project, obtained through Google Fonts.
* GitHub: Used to plan, build, preview and edit the application.


### **Other Requirements:**

* asgiref
* backports.zoneinfo
* dj-database-url
* django-allauth
* django-braces
* oauthlib
* psycopg2
* PyJWT
* python3-openid
* pytz
* requests-oauthlib
* sqlparse



------------------------------------------------------------------

## Troubleshooting and testing

<a name="test"></a>

### **Troubleshooting:**
Troubleshooting was quite varied on this project as it involved quite a wide range of different technologies. Initially the biggest issue i ran into was with settign up the authentication and registration system. I spent quite a few weeks trying to get allauth to work before abandoning it in favour of django contrib auth, something that had much more extensive documentation avalible for it and was ultimately much simpler to use.
I opened a new branch to attempt this new authentication system on and when i merged the branches, later on, it took some time to work through the merge conflicts, remove unneeded duplicates, folders and code.
There were countless other small errors solved throughout the development of this application.

**Error Handling and input control:**

### **Testing:**

**Code Validation:**

**Browser Compatibility:**

**Accessibility Testing:**

**Performance Testing:**

**User Story Testing:**

User:

*As a diver I can make a log input of my dive details (depth, time, location) so that I have this recorded in my dive log.*

&#9745; Django.contrib.auth installed which has sign in/ sign up and register functionality.

*As a diver I can edit my logged dives so that I can alter details where needed*

&#9745; An option to edit the dive avalible and a html page that facilitates this avalible. Dive updated and redirects to log.

*As a diver I can delete a dive from my log so that I have full control over what dives i have in my log.*

&#9745; A delete option is avalible for each dive, user can delete their own dives.

*As a Diver I can view my logged dives so that I have access to a log of my dives*

&#9745; Html page for viewing the users own logged dives avalible. Dives in order of most recent for convienience.

*As a user I can create and account so that I can use the app to log and view my dives.*

&#9745; Full login and register functionality avalible with login required for viewing logs and logging dives.

Diving officer:

*As a diving officer I can view all dives logged by members of my club so that i can have a digital log for my club*

&#9745; Diving officer (who has staff status) has access to a means to view all divers logs in order of most recent for convienience.

*As a diving officer I can view a list of my club members on the system so that i know who is contributing and in the event that it is extensive, i can see all of my members.*

&#9745; Diving officer who has staff status can view a list of members, complete with their email and first and last names.

*As a diving officer I can log my own dives within the same profile so that i dont need to have two profiles and i can keep my own log.*

&#9745; The diving officer has access to all of the same functionality as the other users, the diving officer section of the application is for users with staff status only (the diving officer only) and is a seperate section of the application.




**Manual Testing:**

Testing links and forms:

* Navigation links are working and bring the user to the correct page. &#9745;
* The home page Log a Dive” and "View my Log" links are working and take user to the correct pages. &#9745;
* The social media links all work and take users to the correct social media. &#9745;
* The title of the page "My Dive Log" works as a link to return the user to home. &#9745;
* Login and logout functionality works correctly. &#9745;
* The registration form has error handling built in so the user must make the correct inputs.&#9745;
* The forms all redirect appropriately. &#9745;


Testing security elements:

* When the user is not logged in they cannot access log a dive or my dive log. &#9745;
* The user can only view their own logged dives (unless they have staff status). &#9745;
* The user can edit and delete their logged dives. &#9745;
* The user cannot edit or delete anyone elses dives. &#9745;
* The diving officer (who has staff status) can view all users logged dives. &#9745;
* The diving officer (who has staff status) can view all users details. &#9745;

Testing other elements:

* The navigation bar shows which page is active correctly. &#9745;
* Images when used loaded correctly. &#9745;
* Navigation of the application is intuitive. &#9745;
* When the user is logged in their username shows at the top of the screen. &#9745;
* When the user is not logged in the option to login or register shows. &#9745;


------------------------------------------------------------------

## Bugs

<a name="bugs"></a>

### **Bugs Found:**

The login functionality at the top of the screen was appearing twice on the home page, i discovered this was due to a duplicate of the index.html document existing after i merged the branch i was working on to the main. Deleting this extra file fixed the issue.

The delete function was redirecting back to the log but wasnt removing the dive that was supposed to be deleted. This was remedied by taking the delet function out of the delete.html and putting it next to the dive on the log page.

After merging the two branches i spent several hours trying to work out why i wasnt redirected to logged_out.html when i clicked logout but was instead redirected back to the home page. Ultimately i ended up looking through the setting.py from before the merge and found two lines that were now in my settings.py that werent there before i merged the files, when logout was redirecting as desired. The lines were LOGIN = '/' and LOGOUT = '/', these were an override that directed the user back to the home page when login/logout was clicked. After deleting them the app performed as desired.

There was an interesting bug that meant when i filled in a dive log form and clicked log my dive, the form would refresh but the page would not redirect, the dive was logged when i manually navigated to my logged dives. This was solved with some expert help from my mentor.

There are hopefully no bugs present in the application now, if you happen to come across any, please email me at l.butler1993@gmail.com.
------------------------------------------------------------------
## Deployment

<a name="deploy"></a>

Deployment of the program was done via Heroku, the process is below;

* When you have a Heroku account and have signed in there is a white button with purple outline on the top right hand side of the main dashboard labelled new. This button opens a dropdown within which we select 'Create new app'. This will redirect us to a page where we select a name for our app as well as inputting our region. We the click 'Create app'.
* On the page you are redirected to, there is a navigation bar along the top, under the name of the app. Click on the final tab labelled 'Settings'. In this page, scroll down past App information to the section labelled 'Config Vars'. Click on the button to 'Reveal config vars'. Postgres and a secret key will need to be added to this. Once the config vars are saved they should be added to the env.py file, which should be added to the .gitignore file so that the config vars are not publically avalible.
* When you scroll up to the top of the page again, you can select the 'Deploy' tab from the same nav bar we found settings on. On this page select Github as youR deployment method. When you click on Github you will be able to search for the repo you want to use. You can then select to deploy manually or automatically. Selecting automatically will have the app deploy each new update.
* You can then make a push in your Gitpod workspace and your app should deploy.

To manually deploy;

	* Enter 'heroku login -i' in the terminal and enter your own login details.
	* The enter 'heroku apps' in the terminal.
	* Followed by the command: heroku git:remote -a My-Dive-Log.
	* Then push to both the main branch and Heroku using the terminal commands: 'git push origin main' and 'git push heroku main' respectively.
	* The app should now be avalible on Heroku.
------------------------------------------------------------------

## Credits and Acknowledgements

<a name="credits"></a>

### **Credits:**

* Code: Code advice was taken from Stack Overflow (https://stackoverflow.com/).
* It was also take from the Code Institutes walkthrough projcts "Hello Django" and course content.
* Design ideas were taken from Bootstrap (https://getbootstrap.com/) as well as general web searches using Google.


### **Acknowledgements:**
* My program coordinator Kasia for contiuned support and advice throughout.
* My software developer friends (Joshua Butler-senior dev at Overstock Ireland and Glenn Gilmartin- senior dev at Overstock Ireland) for their advice and patience.
* My mentor Tim Nelson for going above and beyond to ensure i was presenting my best work and that i understood each concept we discussed.

------------------------------------------------------------------

## Content and resources

<a name="content"></a>

* All content was written by the developer as part of an academic exercise for the Code Institute.



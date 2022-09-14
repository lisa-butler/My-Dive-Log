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
 2. [Website Features](#features)   
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
The application should be easy to use and require preamble to log a dive quickly after returing from the water.

### **Structural planning**

In order for the web applicationto achieve these goals it was decided to have three pages avalible for the diver; the Home page, Dive log page and Log a dive page. For the diving officer a fourth page labelled Diving officer was avalible, this consisted of two options, to view the club logs and to view the club members.
There was also a login/logout/register functionality at the top of each page and pages such as dive logs and log a dive required login to acess.

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
Hitting log at the bottom of the logging page should take the diver too their logged idves.

**My logs:**
This page should contain the same theme as the other pages.
This page should display all of the divers logged dives specific to them.
Content fileds from their logged dives such as buddy, depth etc should be visible.
The option to edit or delete these dives should exist.

**Diving officer:**
This page should contain the same theme as the other pages.
This page should provide the diving officer with the options to view the club logs or to view the club members.
The club logs hsould contain every dive logged by members of this club with their username visible.
The members section should show all members in the club.

**Wireframes:**
A wireframe was done for each page of the application before progressing into developing it.
The basic plan for the application was to keep it as uncluttered and minimalistic as possible while providing the required functionality. As the mean age of divers is generally older, it was intended that the application be as intuitive as possible.

![Wire frame of home page](assets/images/readme-images/wireframe.jpg)

### **Style**

Background: It was decided to stick with a very basic and modern theme of a white background with content kept neat and centrally placed. This benefitted accessibility as the elderly population in diving who would not be as tech savvy, generally, would have a better chance of navigating the application.

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
The font chosen was;
	-Sans-Serif
The focus of this font being to provide the information in a non-distracting manner that was viable for the visually impaired user or someone trying to use the site on a mobile device.

------------------------------------------------------------------
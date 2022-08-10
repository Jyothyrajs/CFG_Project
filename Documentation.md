
# CFG Project Report
Group members: Jyothyraj Sobhana, Katarzyna Olszynska, Lucianna Tomlin-Paul, Mina Mahdi, Naomi McEntegart

## Introduction
Our project is a productivity program to enhance an individual's productivity. It is a to-do list that also implements a point/reward system for motivation purposes. We were inspired to build this project as we were finding a lot of the current to-do list apps and software available to not quite match what we wanted. Although they helped us to stay organised - they didn’t always keep us motivated. This project incorporates methods to encourage extrinsic motivation through earning points from completing tasks and buying rewards with these points.

## Main Considerations
Although we had many different features we wanted to include in the project, we had to narrow it down to just the key features due to time constraints. These were based on the features that would provide functionality to the software and allow us to solve the problem we presented.

### Key Features
1.	Create a new task
2.	View all tasks
3.	Update the status of task
4.	Each time a new task is completed, an additional point is granted to the user

#### The To-Do List
The basic features of the to-do list (i.e., key features 1-3) were written in Python using Flask. Flask allowed us to connect the backend logic to a database which held the task data.

#### The Reward System
Due to the limited time, the reward system is quite simplistic, the user initially starts with a score of 0 points. Then, every time the delete function is initiated to delete a completed task, an additional point will be added to their total.

## Specifications and Design
![image](https://user-images.githubusercontent.com/104771053/181619110-2e35b1c8-ac53-4d62-887c-e8f689506573.png)
Figure 1. To-do List app basic process flow including basic user requirements
![image](https://user-images.githubusercontent.com/104771053/181619156-88d456f3-8918-445b-a7d1-118b43bae7b8.png)
Figure 2. Another process flow design showing more specific logic

Both figure 1 and 2 show our principal design ideas for our app. Users will be able to set, view and delete tasks. Although we initially looked at using the Tkinter module to design our app, we decided to build an API for the app instead which would use CRUD operations. We firstly used the Flask framework to set up a local web server, and then set up a route. We then utilised our knowledge of MySQL to create a database where our to-do list items would be stored. We then created helper functions which would contain logic to enable us to add, view and delete items in the database. These functions would process the requests by connecting to the database and executing the relevant queries we set up.

## Technical Requirements

### Implementation and Execution
We started the project by having several meetings in which we discussed the list of project requirements. We then narrowed this list down into key requirements needed to create a minimum viable product (MVP) and the additional (desirable) requirements we would like to add if possible, given the time constraints. We also used our list of key requirements to prioritise our tasks. 
Initially we worked together to code the basic requirements in a group coding session over several Zoom sessions. We chose to take this approach at the start rather than diving straight into an agile development style for example due to all of use wanting to be familiar with the initial code and all of us believing it was important for everyone to be happy with what was created. Another important reason for this was the major constraint of using content and tools that were quite new to all of us. This allowed us to easily build on each other’s knowledge and understanding easily and work through the challenges that we faced as we began to bring our program. 
This is how we worked for most of the project before then adopting an agile development style. Although we all worked as a group to discuss the tasks that needed completing, we then assigned a scrum master to implemented and update these tasks using Jira. During the first sprint, we finished the basic code required for the MVP as well as beginning to test our code. The second sprint was dedicated to fixing any problems, making sure we completed all the necessarily requirements of the project and that our code follows SOLID principles. We believe we were quite successful in this regard, although we didn’t get to all the additional requirements, we were able to meet all of our deadlines. 
We continued having regular meetings although these shifted from coding-based to informal sprint planning meetings where we could discuss any issues that were cropping up and keep each other up to date. These meetings also incorporated sprint reviews to discuss what worked/didn’t work. Daily stand-ups were not possible due to time zone differences and our other life commitments, but we communicated very regularly on Slack. 
We used git and GitHub to manage our version control, although did not necessarily utilise branches and merging due to coding together as a group there was generally not an issue with resolving conflicts in the code. 
### Tools used:
•	Zoom: for meetings
•	Slack: for other communication
•	Jira: for keeping track of tasks during our sprints
•	Pycharm: the IDE used
•	MySQL workbench
•	Github
### Libraries and Packages:
•	Flask
•	SQL Connect Python
•	Request

## Testing and Evaluation
### Testing strategy
Unit testing?

We also used more manual methods of testing to test the functionality of our code. We not only used the program ourselves for our day-to-day tasks to check that we didn’t run into any problems while using it, but we also invited a few family members and friends to do the same. This method of testing was quite successful, as we were able to uncover errors in the code as well as some constructive feedback on the program. 

## Project Limitations (‘could haves’ and ‘would haves’)
Front-end: After completing the basic logic of our program, we wanted to implement a GUI to make our To-do list app more appealing. However, with limited experience with front-end languages and not as much time as we would have liked, we were not able to dedicate too much time to this part of the project. One option was to utilise JavaScript libraries but as none of us were too familiar with JavaScript, we then looked at rendering an html page through Flask. 

Reward System: We would have liked to set up a point system that rewarded more points dependant on how long the task would take to complete, but we did not have time to set this up. We were also planning to add a way to spend the points on rewards. We had several ideas for how this could be implemented:
* Using the Pokémon API so users could ‘buy’ a Pokémon with their points, the Pokémon could then be stored in a separate database. This could also work with other APIs available online for people who aren’t interested in Pokémon for example.
* Adding a new function that linked to a separate database that allowed users to add their own rewards and point ‘cost’ that they could use their points to ‘buy’. The intention for this would be real-life rewards, for example 15 mins of watching Netflix. 

## Conclusions
We were able to meet our goal to design and implement a to-do list app that allowed for users to create tasks, update them, and delete/complete them. We were able to successfully code this using Flask and connecting to a database that holds the tasks. This project demonstrates are understanding of both basic coding concepts, such as creating useable functions as well as more specialised concepts such as object-oriented programming and the use of API.

A huge strength of our group was our communication, we not only met very regularly, at least a few times a week, but also continually messaged each other with updates to the code to make sure everyone was up to date. We also wrote a lot of the code together via video calls, allowing everyone to have a say in what was being written and making sure everyone was happy with what was being written. We also successfully took advantage of the groups different skills sets, for example, those who had previous HTML experience were able to start implementing the Front-end of the project.

### Future improvements
The limitations discussed would be our next focus if we had more time to complete this project: working on both improving the front-end user experience of our program as well as adding functionality to the reward system to make the program more user friendly and increase the motivation of the users to complete tasks.

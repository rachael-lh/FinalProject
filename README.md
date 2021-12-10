# ✨Your Goals App✨

Need a place to write and store your daily, monthly or annual goals? This is the app for you! 

The application I made allows you to input your details and your goals with the start and proposed end dates. We all know circumstances change along the way so you are also able to edit and delete them as and when you need to. 

# Project Brief 📑

The application is designed to meet the requirements set out by the QA community project brief. The project is designed to encompass the following:

- To create a multi-tier web application that demonstrates CRUD functionality.
- To utilise containers to host and deploy your application.
- To create a continuous integration (CI)/continuous deployment (CD) pipeline.

Tools used to achieve the requirements are:

* Kanban Board: GitHub Project Board
* Version Control: Git
* CI/CD Server: Jenkins
* Cloud Server: Azure Virtual Machine
* Application configuration: Python
* Containerisation: Docker and Docker Compose
* Reverse Proxy: NGINX

# How I tracked the project 🔎

For project tracking, I used GitHub Project - https://github.com/rachael-lh/FinalProject/projects/1. This is required to plan out what tasks are required to build, amend, test and deploy the application. GitHub Project allows these steps to be presented in a clear and orderly manner via a Kanban Board style. 

The Kanban board is divided into 'to do' tasks, 'in progress' tasks and 'done' tasks. As the project management was detailed in GitHub this allowed me to link the related pull requests to the task noted on the board - allowing for the utmost clarity of whether a task has been successfully actioned. 

<img width="1125" alt="Project Screenshot GH" src="https://user-images.githubusercontent.com/92022019/145603397-dd476567-e9cb-47bf-baab-eb84bc17e119.png">

# Application Structure ⚙️

I created a multi-service web application based on the Flask web framework. The application is a goal tracking application which allows users to input their details and add their goals. The application can *create* users, *read* user data from the MySQL database, *update* user goals and *delete* the user and goals demonstrating CRUD functionality. The user is able to do so by using the 'Add New GOAL!', 'Edit' and 'Delete' buttons on the front page of the web application.

<img width="1329" alt="New goal" src="https://user-images.githubusercontent.com/92022019/145587440-97a5206f-839e-4b8d-92d9-54d97283bd9d.png">

<img width="1429" alt="Edit" src="https://user-images.githubusercontent.com/92022019/145587500-6156c576-3c45-4cea-847f-80ae29d960f6.png">

<img width="1411" alt="Delete" src="https://user-images.githubusercontent.com/92022019/145587557-4d2665e5-8fa9-4831-9bc0-b8fa9b6dc260.png">

<img width="1401" alt="Successful delete" src="https://user-images.githubusercontent.com/92022019/145587790-106045c6-da8d-432d-8a5c-51826c42f915.png">

The flask application connects to the MySQL database (hosted in Docker) via Python using MySQLAlchemy and Flask-SQLAlchemy. Using the routes created within the application, user information and goals are stored, edited and deleted from the database. Should the user not already exist within the database, a new user is created using an "IF" statement.

<img width="420" alt="Application" src="https://user-images.githubusercontent.com/92022019/145571822-53e817b4-c20c-4078-b186-4f7bddc65db8.png">

# Issues - Limitations of Jenkins in Docker 📉

As a macOS user, the recommended course of action was to install Jenkins via Docker. However, when attempting to build the pipeline, it became apparent Jenkins within a container was subject to heavy restrictions, for example, it was unable to run 'sudo' commands to install and upgrade the required dependencies, connect to Github (Webhook). 

Utilising the GitHub branching method, I worked on feature branch to attempt to circumvent these issues. I had to build the Pipeline manually each time without the Github connection. Using the official Jenkins image from Docker, I installed the Linux standard base and docker as seen here (https://github.com/rachael-lh/FinalProject/commit/b3e72956d9a56f5a26156ffb1c88aed6ca694023). This still did not circumvent the abovementioned issues and I was unable to implement a working Pipeline with Jenkins hosted in Docker. 

When I was provided with working access to Microsoft Azure, I was able to create a Linux based Virtual Machine and install Jenkins using the a script file shown in Visual Studio Code (VSC) below:

<img width="848" alt="install-jenkins sh shown in VSC" src="https://user-images.githubusercontent.com/92022019/145577351-bb128a96-42ed-4901-877a-aa020c735134.png">

# CI/CD Pipeline and Technologies used 👩🏻‍💻📊

The diagram below demonstrates the overall structure required from the application development and deployment alongside with the technologies used:

![Pipelines w T](https://user-images.githubusercontent.com/92022019/145613162-75793481-79de-4ccc-acf9-113f97712410.png)

Step 1 - a connection was created between VSC and GitHub, this was done by cloning the GitHub repository using HTTPS to the local working directory. 

Step 2 - the flask application was then made locally and could be connected via http://localhost:port. The MySQL database (created in Docker) and flask application each used a unique port so that traffic could access the port. After the application could perform basic functionality, it was deployed first with Docker and then Docker-compose, and thus the database and flask application was containerised. 

Step 3 - experiencing the limitations of Jenkins in Docker (noted above) caused a delay in producing the Jenkins Pipeline. However, once access was provided to Microsoft Azure, a connection was created between the Microsoft Azure Virtual Machine and VSC using a ssh key. This allowed for basic linux commands to be used enabling the installation of the required dependencies for Jenkins

Step 4 - a basic Jenkins Pipeline is currently running and can be added upon. At the moment, there is a Test stage and a Build & Deploy stage. The Test stage has two unit tests testing that the endpoints have the expected response. The Build & Deploy stage allows for the images and containers to be built allowing the webpage to be accessed on virtual machines' public ip address at port 5000. As the Jenkins Pipeline is connected to Github via a Webhook all pushes trigger a new build. 

<img width="782" alt="Webhook" src="https://user-images.githubusercontent.com/92022019/145593983-3b1b8279-332d-4cdf-a1b1-fb425d5ac533.png">

<img width="807" alt="Github connected" src="https://user-images.githubusercontent.com/92022019/145593996-bd63dec6-aaba-4e4c-9a3b-44ea81de52a3.png">

<img width="578" alt="Screenshot 2021-12-10 at 17 10 31" src="https://user-images.githubusercontent.com/92022019/145613968-12b909af-80c6-4fed-b589-7e21c6867589.png">

# Further Improvements 📈

Although the project achieves the requirements set out in the project brief above, there are further improvements that can be made to optimise how the application is ran. For example, the following changes can be implemented:

* Division of services - separation of the frontend and backend API. 
   - Improves deployability and reliability of the services by isolating each services functions
   - Allows for synchronous development on multiple services
* Creation of a login/sign-up services - email and password syntax has already been placed into the database.
  - Enables users to only see their own goals
  - Creates a cleaner UI for the user
  - Allows for privacy
* Use of Docker Swarm to handle larger scale up usage. 
  - Makes an allowance for large volumes of traffic
* Creation of tests to confirm the reliability of services available.
  - Errors will be highlighted before the build and deploy stage

# Closing Statements 👋🏼

Thank you for taking the time to explore my application and engaging with the read.me for further information. 

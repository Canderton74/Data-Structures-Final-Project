# Data-Structures-Final-Project

## General Roadmap
- Welcome to our Route Risk application
- Route Risk is an application routed in a node.js/react frontend with python HTTP backend server. See the fields below on how to run this application on your local machine.
- Route Risk takes in two use input cities and a choice of type of tree structure. When calculate is pressed on the frontend, the backend creates the designated tree structure from over 246,000 accident reports and then searches for the inputted cities' accidend count. Based on these counts and distance traveled for the journey, the application creates a probability for how likely your journey is to be interrupted by some sort traffic accident.
- The application also outputs the run time that it took to create the designated tree and search for the two cities and output the probability
- Feel free to compare the difference between run time in the B+ tree and the Red Black tree!

## Front end download infrastructure
- Download node.js from https://nodejs.org/en
- Make sure to add 'C:\Program Files\nodejs\' to your PATH environment variables for your computer
- Pycharm should automaticlaly pick up the node.js and npm paths
- If pycharm doesn't you can add this in your files settings

 ## Running the front end
 - To run the frontend, go to the terminal on pycharm and navigate to the "my-app" directory
 - run the command "npm start" and you should be directed to a url that runs the frontend

 ## Updating from Main
 - Whenever you pull from main, make sure to run 'npm install' in the terminal
 - This command will update any dependencies in your package.json files automatically

 ## Running the Backend - new way
 - when you run 'npm start' in the 'my-app' directory, it now automatically runs the backend scripts for you
 - now you only have to do 'npm start' to utilize application
 - there is a connection in 'package.json' that allows the 'npm start' command to run a command to the backend file to start
 
  ## Running the Backend - old way
  - Navigate to the backend directory in the repo
  - In a different terminal than the frontend, run 'python backendServer.py' to start the backend



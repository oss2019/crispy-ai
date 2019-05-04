# Week 1 : Preliminary - Setting Up

In the first week, we are going to set up a working environment and get a basic Django app up and running. If you are still new to django, I would suggest following the video tutorials [here](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p). You will need to know a little python, although, you can easily learn this along the way.

Follow the steps below to get started with the project 

Note:

- We strongly recommend you to use **Ubuntu or a Linux-distro** for development.
- We also recommend you to install [PyCharm Professional Edition](https://www.jetbrains.com/pycharm/) which you can get for free by applying for the [GitHub Student Education Pack](https://education.github.com/pack). PyCharm is an IDE in which we will write python code for the project.


## Step 1 : Installing Python and Django

- Follow Steps 1-4 in this [tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-ubuntu-18-04-quickstart) to install python
- Open a terminal, run `pip3 install django`


##Step 2 : Configuring GitHub for your project

Here is where you get to learn the basics of Git. Currently, you can find the project code [here](https://github.com/oss2019/crispy-ai). You will be able to understand the code structure if you have gone through the videos. Now, before we get this code onto your computer let's first set up git. Open a terminal and execute the commands below

1. `sudo apt update`
2. `sudo apt install git`
3. `git config --global user.name "Your Name"`
4. `git config --global user.email "youremail@domain.com"`

## Step 3 : Cloning the project.
In this step, we will clone the project from GitHub to your computer so that you can edit and run the server locally. It is good practice to fork the repository into your GitHub account and then pull it locally on your machine.

1. First, go to the [repository](https://github.com/oss2019/crispy-ai) and fork it using the `fork` button. You can find it in the top right-corner next to `star` and `watch`.
2. Go to your GitHub profile home - https://github.com/your-username-here . You should be able to see the crispy-ai repository forked from oss2019. If yes, then your good to proceed.
3. Fire up a terminal and navigate to a folder where you wish to download the code to. Execute the following command :
	`git clone https://github.com/your-username-here/crispy-ai`
4. Once it's done, you should be able to see the repo saved locally in the folder in which your terminal was opened. You can verify this by typing `ls` and enter in the terminal.


## Step 4 : Opening the project in PyCharm/SublimeText
- Launch PyCharm or any other editor like sublime text 3. Click Open -> choose the folder 'crispy-ai' where you cloned it in the previous step. (If you get a pycharm name error, rename 'crispy-ai' => 'crispy_ai' and proceed)
- You might get an error asking you to setup a project interpreter. Goto File -> Settings -> Project -> Project Interpreter -> Click the gear icon and add new interpreter -> install the packages mentioned in [requirements.txt](https://github.com/oss2019/crispy-ai/requirements.txt)
- You may also run `pip3 install requirements.txt` instead after setting up a virtual environment. [See this link](https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-18-04)


## Step 5 : Run the Server
- Open the terminal in the project root folder. Execute `python3 manage.py runserver 8000`
- Open a browser and goto `localhost:8000`
- If the site loads without errors, you are ready to start contributing!


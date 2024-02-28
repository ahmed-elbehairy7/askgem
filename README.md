# askgem

### Project for interacting with gemeni from the terminal

## Table of content:

- [ setup](#setup)
  - [OS specific](#os-specific)
    - [Windows](#windows)
    - [linux](#linux)
- [askgem.config](#askgemconfig)
  - [key](#key)
  - [model](#model)
  - [you](#you)
  - [gemeni](#gemeni)
  - [youInFile and gemeniInFile](#youinfile-and-gemeniinfile)
- [arguments](#arguments)
  - [-c, --config-path](#c---config-path-path)
  - [-q, --question [...]](#q---question)
  - [-n, --non-interactive](#n---non-interactive)
  - [-qn, --question-not-interactive](#qn---question-non-interactive)
  - [-s, --save-file](#s---save-file)
  - [-l, --list-models](#l---list-models)

## setup

Just clone the repo by typing this command in your terminal:

    git clone https://github.com/ahmed-elbehairy7/askgem

then you will find a file named askgem.config, you have to put you api key there so you can use the application. You can create a new api key by clicking this link and seeing the documentation: https://makersuite.google.com/app/apikey

    {
        "key" : "Your api key"
    }

Now you need to install the requirements by typing the following command:

    pip install -U -r requirements.txt

> **NOTE:** I had some problems at this step, hope it goes well with you but I did a lot of troubleshooting here because the google generative ai package wasn't enough, sorry that I don't know what happened exactly so I can't document it

### OS specific

#### Windows

first install the pyinstaller python package with the following command

    pip install --upgrade pyinstaller

then run the following command

    pyinstaller main.py -F -n askgem

So basicly this is converting the main.py file to an executable file. the "-F" argument states that the program is just one file, and the "-n" for naming the .exe application. so after running this command you should see two new directories, build and dest, open the dest directory and you will find askgem.exe there, congratulations, it can't find the askgem.config file! [see this](#c---config-path-path)

**access the app from anywhere**

In order to do this you had to add a new environment variable, you can search online for how to do this for more updated info or do the following:
simply press the windows key and start typing environment variables then click it when it appears, after that go environment variables.

Now, you have users variables and system variables. you will find a path named Path, select it and click edit. Now, choose whether you would add a path for only this application or add a path for a directory that will contain any other projects in the future. for me I choose the directory option, then I put all my executables there. So, click new then type the path to the app or the directory whatever you want, this can require a restart I don't know honestly

### Linux

Getting the app to work is literaly as easy as copying a file since what you have to do is just copy the file to the /usr/bin directory

    cp main.py /usr/bin/askgem

## askgem.config

> If your program is not working because it can't find the askgem.config file, [see this](#c---config-path-path)

### key

as obvious, this is the api key for the app, and this is probably the only required one

### model

you can change the model the app uses by changing the model value

### you

this change what the application print to take input from you, for example changing the you to "you: " like this:

    {...

        "you" : "You: "

    ...}

will result of this:

    hostname@uesrname:~$ askgem
    You: Hello

    hello, there!

    You: exit

instead of this:

    hostname@uesrname:~$ askgem
    >>> Hello

    hello, there!

    >>> exit

### gemeni

This is pretty much the same as [you](#you) but for gemeni

### youInFile and gemeniInFile

Sometimes files are unreadable, so this one is for how to save prompts and responses in files. They are pretty much the same as [you](#you) and [gemeni](#gemeni) but for saved files, they're defaulted to >>> for you and <<< for gemeni or the you and gemeni values if they're set.
for saving chat into a file see [save-file](#s---save-file)

## arguments

### -c, --config-path path

specify a path for askgem.config file, the config path is set to ./askgem.config as default see the example below

    python main.py -c D:\new\path\for\askgem.config

### -q, --question [ ...]

This is probably done with the [-n, --not-interactive](#n---not-interactive) argument, or simply -qn for combining them together. And it's job is asking gemeni one question from the command line directly before starting the app.
then gemeni will answer this question before anything. see the example below:

    hostname@uesrname:~$ askgem -q hello gem
    Hello! I'm here to help you with any questions or tasks you may have. Let me know how I can assist you.

    >>> What is your name

    I am a virtual digital voice service, not a person.

    >>> exit

### -n, --non-interactive

This basicly tells the program to not initiate an interactive chat session and close after the first request like the example below:

    hostname@uesrname:~$ askgem -n
    >>> What is your name

    I am a virtual digital voice service, not a person.
    hostname@uesrname:~$

### -qn, --question-non-interactive

This is for times when you just want to ask one simple question. See the exaple below for more understanding:

    hostname@uesrname:~$ askgem -qn What is your name
    I am a virtual digital voice service, not a person.
    hostname@uesrname:~$

### -s, --save-file

save the chat into a file

    askgem -s file.txt

### -l, --list-models

List gemeni models available, this just print the genai.list_models()

    hostname@uesrname:~$ askgem -l
    gemeni-pro
    gemeni-pro-vision
    ...etc.

#### Thanks...

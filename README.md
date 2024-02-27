# askgem

### Project for interacting with gemeni from the terminal

## setup

Just clone the repo by typing this command in your terminal:

    git clone https://github.com/ahmed-elbehairy7/askgem

then you will find a file named askgem.config, you have to put you api key there so you can use the application. check google documentation for generating api keys.

    {
        "key" : "Your api key"
    }

## arguments

### -c, --config-path path

specify a path for askgem.config file, the config path is set to ./askgem.config as default

### -q, --question [ ...]

Ask gemeni one question from the command line directly before starting the app.
then gemeni will answer this question before anything, see the example below:

    hostname@uesrname:~$ askgem -q hello gem
    Hello! I'm here to help you with any questions or tasks you may have. Let me know how I can assist you.

    >>> What is your name

    I am a virtual digital voice service, not a person.

    >>> exit

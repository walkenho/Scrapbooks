## Basics: Moving Around and Basic File Manipulations
If you log on, the first thing you probably want to know is where you are (you will probably be in your homedirectory). You can find this out by printing the name of your current working directory onto the screen
```
# print working directory
pwd
```

You can find out what is in this directory by listing its contents. Many bash commands allow for modifiers to be added, so-called flags. They most commonly consist of a single letter, which is appened to the command by a "-". You can combine multiple flags by just writing them one behind the other. For example the command `ls` lists the contents of a directory. It has a multitude of possible flags. Here are some examples

Print content directories:
```
# list current directory
ls 

# include hidden files
ls -a

# include more details 
ls -l
```

You can find info on a bash command and its modifiers by using the `man` command.

Getting help for a command
```
man command

# for example:
man ls
```

In order to move around, you can use the 



Change directory to directory newdirectory inside the current directory: 
```
cd newdirectory
```

change directory to directory above: 
```
cd ..
```

chaining together:
```
cd ../my_new_directory
```

move file:
```
mv file_old file_new
```

copy file:
```
cp file_old file_new
```

delete file:
```
rm file_to_remove
```

To copy or delete folder, you need to add the -r flag:
```
cp -r folder_old folder_new
rm –r folder_to_remove
```

create (make) directory:
```
mkdir name_of_new_directory
```



find a piece of text inside textfiles:
```
grep textpiece textfile
```

good for looking for stuff in the sas files:
grep installer *.sas
(looks through all files that end with .sas and finds “installer” in them)
Case insensitive version:
grep –i installer *.sas

(If you have a command then the –someletter always gives you options (flags). Alternatively you can use --flag_in_its_long_version (this is a double minus))

Print textfile on the screen:
```
cat textfile
```

dump output of a command into a file:
```
# appends:
mycommand >> mytextfile
# overwrites textfile:
mycommand > mytextfile
```

[Here]([https://devdactic.com/10-basic-bash-commands/) is a link with some basic commands and how they are used:

And this is a small summary of some more commands (more useful, but not as extensively described):
https://www.unr.edu/it/research-resources/research-computing/hpc/the-grid/using-the-grid/bash-commands

And a cheat-sheet for scripting (which you probably won’t need, but I just found because I was looking for sth for you and I thought it was quite neat ;)
https://devhints.io/bash


 ps auxf | grep launch_

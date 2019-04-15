## Basics: Moving Around and Basic File Manipulations
### Moving Around
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

# include hidden files and print more details 
ls -la
```

You can find info on a bash command and its modifiers by using the `man` command.
```
# print manual for mycommand
man mycommand

# for example:
man ls
```

In order to move around, you you the `cd` (change directory) command:

Change directory to directory newdirectory inside the current directory: 
```
# change to directory called mydirectory inside current directory
cd mydirectory

# change to directory above
cd ..

# chaining these together to move into directory which is also inside the directory above (basically into a "parallel" directory)
cd ../mydirectory
```

### Basic Interaction with Files and Folders
You can create a simple text file by 
```
# create a text file called mynewtextfile.txt
touch mynewtextfile.txt
```

This file can then be copied, moved or deleted:
```
# copy file
cp oldfilename newfilename

# move/rename file
mv oldfilename newfilename

# delete file
rm oldfilename
```

In order to create (make) a new directory:
```
mkdir mynewdirectory
```

Directories are copied, moved and deleted like files. However, copying and deleting requires the -r (recursive) flag:
```
# copy directory
cp -r folder_old folder_new

# delete directory
rm –r folder_to_remove

# rename directory (without -r flag)
mv old_folder new_folder
```

## Interacting with files and chaining commands together - slightly less basic
### Interacting with text files
Now that we know how to move files around, we also want to do sth useful with them. 

There are four main options to access the content of a text file. I recommend just trying them out to see what they do and how they behave differently. These are the commands:
```
# print whole text file to screen
cat mytextfile

# print text file to screen one screenful at a time
more mytextfile

# print text file allowing for backwards movement returning to previous screen view after finishing
# note: less does not require the whole text to be read and therefore will start faster on large text files then more or text-editors
less mytextfile

# use a text editor (for example vi)
vi mytextfile
```

You can also show only the first or last n rows of a document
```
# show first 10 rows of a document
head -10 mytextfile

# show last 10 rows of a document
tail -10 mytextfile
```

In order to find pieces of text in a document use `grep`
```
# look for the string python in mytextfile
grep python mytextfile

# search case-insensitive
grep -i python mytextfile

# return line-numbers with the results
grep -n python mytextfile

# search for a filename ("mybadfilename" in the example) (case insensitive) in all files with the ending *.py and return the occurences together with the line number
grep -in mybadfilename *.sas
```

In the last example, we have seen an example of a place holder. \*.sas denotes all files with a .sas ending. 

### Redirecting Output
Some commands print an output to the screen. We might want to re-direct this output to a file. This can be done using `>` and `>>`. `>` creates a new file, `>>` appends to an existing file (or creates a new file if the file does not exist). For example we might want to re-direct the output of the `grep -in mybadfilename *.sas` command into a file: 
```
# creates new file; if file exists, overwrites it
mycommand > mytextfile
# example:
grep -in mybadfilename *.sas > myoutputfile

# appends to file; if myoutputfile does not exists, it creates it
mycommand >> mytextfile
# exammple:
grep -in mybadfilename *.sas >> myoutputfile
```

[Here]([https://devdactic.com/10-basic-bash-commands/) is a link with some basic commands and how they are used:

And this is a small summary of some more commands (more useful, but not as extensively described):
https://www.unr.edu/it/research-resources/research-computing/hpc/the-grid/using-the-grid/bash-commands

And a cheat-sheet for scripting (which you probably won’t need, but I just found because I was looking for sth for you and I thought it was quite neat ;)
https://devhints.io/bash


 ps auxf | grep launch_

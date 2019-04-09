Change directory to directory newdirectory inside the current directory: 
cd newdirectory

change directory to directory above: 
cd ..

chaining together:
cd ../my_new_directory

move files:
mv file_old file_new

delete file:
rm file_to_remove

delete folder (careful!)
rm –r folder_to_remove

make directory:
mkdir name_of_new_directory

list content of current directory:
ls 

list content of directory inside current directory:
ls name_of_directory

find a piece of text inside textfiles:
grep textpiece textfile

good for looking for stuff in the sas files:
grep installer *.sas
(looks through all files that end with .sas and finds “installer” in them)
Case insensitive version:
grep –i installer *.sas

(If you have a command then the –someletter always gives you options (flags). Alternatively you can use --flag_in_its_long_version (this is a double minus))

Print textfile on the screen:
cat textfile

dump output of a command into a file:
appends:
mycommand >> mytextfile

overwrites textfile:
mycommand > mytextfile

This is a link with some basic commands and how they are used:
https://devdactic.com/10-basic-bash-commands/

And this is a small summary of some more commands (more useful, but not as extensively described):
https://www.unr.edu/it/research-resources/research-computing/hpc/the-grid/using-the-grid/bash-commands

And a cheat-sheet for scripting (which you probably won’t need, but I just found because I was looking for sth for you and I thought it was quite neat ;)
https://devhints.io/bash

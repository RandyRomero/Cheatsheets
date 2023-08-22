### Find a file

`find -name *.*`

question id: 7ca7bbcf-beff-4169-aaf5-9d8151e18e8f


### Create a file

`touch file.txt'

question id: f33371fb-d41d-49ef-9a88-e9c383a97913


### Rename file or folder

mv your_file.txt new_file.txt

mv your_folder new_folder

question id: 03caa9e8-801a-4938-9511-69193abcba6a


### How to make a file executable?

make executable
0. chmod +x your_file_name
run
1. ./your_file_name

question id: 1d76c329-cf75-4308-b4bc-29de729c97f1


### How to check/update aliases in bash?

```
nano ~/.bash_aliases
```

question id: a579ff46-e201-4646-8867-2f748ca1845e


### How to unrar .rar archive with password?

```markdown
sudo apt-get install unrar
unrar x filename.rar
```
You will be asked for the password, so type it in and press enter.

question id: 4fe3040a-d845-4ca9-8daa-7049a0131adf


### How to found a command in history?

```markdown
history | grep your_search_word
```

question id: 03df7a9d-8325-48b9-bdb8-5eb3a15782c9


### How to list files and directories as a table with dates and permissions?

```markdown
ls -l
```

question id: f1e696c3-cce3-4d7e-8d2e-920e21a5ae2b


### How to run a command in the background?

```markdown
command &
```

question id: 70e7374d-9670-4422-a739-1dd623be501b



### What does this command mean?

`apt update'

answer:

It updates the database of packages that apt knows about.

question id: bcc6cbf8-f2c3-4cb1-9798-25a8e0059d5e

### What's the root directory in Linux?

answer:

`/'

question id: 9abdaa86-bc6f-404e-8c89-327618a79b49


### What is '/' in Linux?

answer:

It's a root, topmost directory

question id: 5678eff5-e9cf-4bc0-9dd5-7e007ff405db


### What's '/dev' for?

answer:

There are files that are needed to access devices

question id: 7d533901-3d39-4725-b110-8af31e0d50d9


### What's '/etc' for?

answer:

It's probably an acronym for Editable Text Configurations.
There are we have configuration files.

question id: 64b2ea22-bd8d-4f37-8245-bfcdec667ff


### What's '/home' in Linux?

answer:
It's a home directory for the current user.

question id: ccd662a3-a437-4eab-86c3-b8756dd1ed08


### What's '/root' in Linux?

answer:
It's a home directory for the root user. Only root user
can access it.

question id: 61327db9-e333-4a2b-b0dc-c2d2a0b8403e


### How to cd to home directory?

answer:

`cd ~`

question id: 2bf20b82-04af-4ca9-ad4c-a8e53ff8beb


### What's '/proc' in Linux?

answer:
It's a folder for files that represents processes.

question id: 88125f24-90b1-4880-aee0-6b40abee9f45


### What's pwd?

answer:

It stands for 'print working directory' that print the current working
directory where you are.

question id: c97d2c4f-8e03-4373-9fc7-ccb883f2956c


### How to list content of the folder one item per line?

answer:

`ls -1`

question id: 5dd59ef1-4757-4ae6-bc40-8674bfb84053s


### How to remove one command by one from shell?

Let's say you have started your terminal and want to copy a file:
`aleksandr@machine-name:~$ cp some/long/path/file.txt another/long/path`

How to remove one argument by one? Like this
```
aleksandr@machine-name:~$ cp some/long/path/file.txt another/long/path
aleksandr@machine-name:~$ cp some/long/path/file.txt
aleksandr@machine-name:~$ cp
aleksandr@machine-name:~$
```

answer:
By pressing Ctrl+W

question id: 4e3775ca-0470-490f-b626-fd81be9a3bd3


### How to view a text file and be able to scroll it up and down?

answer:

Use 'less your_file.txt` command, than up and down arrows

question id: 6e7ddcd9-3f52-4643-9af3-827aa9337d98


### How to read the first 10 or something lines of a text file?

answer:

`head -n 10 your-file-name.txt`

question id: ccd27173-f001-443f-b3c8-349bc911dcc7


### How to view the last 11 lines of a text file?

answer:

`tail -n 11 your-file.txt`

question id: 24adf89c-8c79-4426-9fe0-bc56df1cb158


### How to concatenate two files into one?

answer:

Using cat, which stands for concatenation.

`cat file.txt file1.txt > combined.txt`

question id: 3d47a46a-a932-4414-af92-477638781fc0


### How to write one line of a text into a new file in the easiest way?

answer:

`echo "My line of text" > my_file.txt`

question id: 7b9c737-d017-40ed-a64f-ac6acf23841b


stdin is usually is a keybord, and stdout is usually a screen


### How to search for a word or a few words in a text file?

answer:

Using grep like this:

```grep -i 'Wie Spaet ist es?' german-expression.txt```

Beware of -i flag to make the search case insensetive

question id: e6459dc6-736a-443b-8ba6-9a82a2d2070c


### How to search a text in two files?

answer

`grep -i "Your text" file1.txt file2.txt`

question id: 5bf9eb5e-0879-41ef-a1c5-bd892da176b2


### How to search a text in all files that match a pattern?

answer:

`grep -i "Your Text" filename*`

question id: e9a8fffa-a5f8-49cf-88d1-81217ae31905


### How to search for a text in each file in a specific directory?

answer:

`grep -ir "Your text" .`

-i stands for case insensitive
-r stands for resucrsive (for looking through directories)

question id: e9a8fffa-a5f8-49cf-88d1-81217ae31905



### How to get a list of all files and directories recursively?

From the current working directory down

answer:

`find .`

or

`find your-directory`

question id: e180098f-4ffb-41e0-9add-03c82fc719eb


### How to get a list of files resursively? Excluding directories

From current working directory down

answer:

`find . -type f`

Looks recursively in the current directory and further down

or

`find some-path -type f`

question id: f0aac8cb-8aca-445d-ba46-78dd5379e4b9


### How to find all files with .txt extension in the current directory recursively?

answer:

`find . -type f -name *.txt`

question id: d35e6393-2f2e-4428-99c3-be56a0c19fce


### How to specify several commands on one line to execute one after another? Regardless of hether any commands were executed successully or not

answer:

Example:
`mkdir test; cd test; echo done`

These commands will be executed one after another, even if any of them fails

question id: 4864920b-25a4-4f3b-93fc-716cc0ec73fc


### How to specify several commands on one line to execute one after another, but only if every command is succesful?

answer:

mkdir test && cd test && echo done

question id: 76aadb57-aa98-428d-9016-1edfb40348cc


### How to run a command only if the previos one fails?

answer:

mkdir test || "directory exists"

question id: 504ea78d-bcab-4bd7-9852-2e85b0a62e43


### How to get a list of all enviromental variables?

answer:

`printenv`

question id: 21a3bb69-739d-4c0b-8e43-34d9908daafc


### How to set an environmental variable?

answer:

`export MYVAR=whatever`

question id: 50427857-1758-4093-a561-9c95c9f09d8c


### How to get a value of an enviromental variable?

answer:

`printenv ENV_NAME`

question id: a6c948fd-2e77-4b24-b301-707cbd5b1438


### How to remove exported environmental variable?

answer:

`unset YOUR_VARIABLE`

question id: 944f9f84-caeb-4b4f-959f-96249517ee24


### How to edit list of permanently defined environmental variables?

answer:

`nano ~/.bashrc`

question id: 22ee2de7-12d7-45dc-b45b-3c38af3b0587


### How to add a new permanent environmental variable?

answer:

`echo MYVAR=whatever >> ~/.bashrc`

two greater than signs means appending to the end of the file instead of rewriting it

question id: 02874e92-4b5b-4b8e-add5-a322afa32bf3


### How to reload .bashrc?

answer:

`source ~/.bashrc`

question id: 92e82dc7-ec00-432c-bb46-dda62114bdd1


### How to get a list of running processes?

answer:

`ps`

question id: c2f4c8a3-6e82-4c47-a966-3eb95e55a097


### How to kill a process by its pid?

answer:

`kill %pid%`

question id: 061ae04b-eb0a-4799-bcbb-af6f70fc3cf8


### Can you descirbe what this permission set means?

drwxr-xr-x

answer:

It's a directory (otherwise it will be -rwxr-xr-x)

The first group represents permissions of a user who owns this file.
He can read (r), write (w) and execute(x) this file.

The second group represents permissions of the group that owns
this file.

The third one is everyone else.

question id: 7268000e-f7d0-4e21-a632-f7d68c4331f9


### How to understand whether your are root user or just a regular user?

answer:

`$` means you are regular user, `#` means you are root

question id: eb64dbdb-18ae-45b1-95bf-37bf2092f625


### What does `#` in terminal mean?

answer

That you ARE currently A ROOT user

question id: f8bf5044-aaa2-4c4e-84d8-db009c89ed22


### What does `$` in terminal mean?

answer

That you are currently NOT A ROOT user

question id: 0fc844ab-24b3-4eb2-a736-cca4fca96b02
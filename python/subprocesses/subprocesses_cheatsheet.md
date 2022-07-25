https://levelup.gitconnected.com/how-to-execute-shell-commands-properly-in-python-5b90c1a9213f

### What is subprocess.run()?

It is a function to run a shell command from inside Python script and wait for it to finish.

question id: 3450fd8f-fe5b-4bf9-9046-ff831b5c1df2


### Is subprocess.run() blocking function?

Yes, it will block Python sript until the shell command finishes.

question id: d3863c99-c56c-4e4c-b690-fa0d302d6794


### What is subprocess.Popen()?

It is a function to run a shell command from inside Python and not wait for it to finish.

question id: 5dd6e0fc-d044-4aae-9af1-87eb12a92af6


### Is subprocess.Popen() blocking function?

No, it is not. Python scirpt will not wait for the shell command to finish.

question id: 8d0095ab-b651-4762-912e-5d3e4360d7a4


### What is `check` flag in subprocess.run()?

answer:
From:
https://docs.python.org/3/library/subprocess.html

"If `check` is true, and the process exits with a non-zero exit code, 
a CalledProcessError exception will be raised. Attributes of that exception 
hold the arguments, the exit code, and stdout and stderr if they were captured."

question id: 84a6a26f-64a3-4b80-9ba7-ca6a29fc5f47


### How to make sure that the process started with subprocess.run() finished without errors?

answer:

user `check` flag like `subprocess.run(check=True)`

question id: e30c3105-e3f5-4cd0-9f78-65761f946d07
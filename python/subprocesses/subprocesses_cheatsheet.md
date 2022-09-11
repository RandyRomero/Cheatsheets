https://levelup.gitconnected.com/how-to-execute-shell-commands-properly-in-python-5b90c1a9213f


### How to start a shell command from Python and get its result back? In synchronous Python

answer:
```python
import subprocess

result = subprocess.run("some command", check=True, capture_output=True)
```

question id: 5bd05406-1643-4de3-b3dc-1d3e58078215


### How to start a shell command from Python and get its result back? In async Python

```python
import asyncio
from asyncio.subprocess import PIPE

async def run_shell_command(cmd: str) -> str:
    process = await asyncio.create_subprocess_shell(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = await process.communicate()
    if process.returncode and process.returncode != 0:
        raise subprocess.CalledProcessError(process.returncode, cmd, stderr=stderr.decode())
    return stdout.decode()
```

question id: 8747c63c-1c5f-4db7-b62f-6aee71ace461


### How to run asynchronously a shell command from Python and do not wait for it to finish?

```python
import asyncio

async def run_shell_command(cmd):
    await asyncio.create_subprocess_shell(cmd)
```

question id: b2f9eccc-7c23-4f2d-9eac-cada6493aa44


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
### What does compiling mean?

In the simple model of the world, “compile” means to convert a program in a high-level 
language into a binary executable full of machine code (CPU instructions).

question id: 28921820-40b1-4653-8117-2cf2968b4e44


### How is source code in compiled languages executed and how does source code in Python executed?

- In compiled languages compiler compiles your source code to machine code all at once (instructions in binary file), 
than CPU executes instructions from you binary file.

- In Python your code gets copliled to binary code (not machine code, so CPU still won't understand it).
Then this binary code is translated to machine code line by line by Python Interpreter a.k.a Python Virtual Machine, 
giving the CPU instructions to run.

question id: d994602f-0fea-4859-bcd9-fa0a72fd2f0c


### What does mean "compiled" or "interpreted" language?

Actually, language itself cannot be either compiled or interpreted. 
We can, for example, compile Python source code to machine code or write interpreter for C code.

question id: e237da59-8977-45af-9376-a21926e3fe32


### What are benifits of using interpreter?

- source code gets compiled to binary code much faster than to machine code
- code in interpreted languages is platform-independent

question id: 9b344abf-b73b-4429-b52a-0e5f20c6ef92


### What is interpreter/virtual machine? 

The Virtual Machine just a big loop that iterates through your byte code instructions, 
one by one, to carry out their operations. The Virtual Machine is the runtime engine of
Python and it is always present as part of the Python system, and is the component that 
truly runs the Python scripts. Technically, it’s just the last step of what is called 
the Python interpreter.

question id: 8e120050-a418-4c9f-8e8a-79d00906ba1c

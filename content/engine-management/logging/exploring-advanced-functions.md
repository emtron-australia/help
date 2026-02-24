---
title: "Exploring Advanced Functions"
weight: 110
---

# Exploring Advanced Functions

Advanced Math Functions can be added by the user themselves.  

![Image](</img/NewItem790.png>)

Clicking Explore Advanced Functions allows the user to import new .dll files as new Math Functions

## Creating New Functions

To create a new function, firstly - Download the **c compiler**: [*https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.0/LLVM-10.0.0-win32.exe*](<https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.0/LLVM-10.0.0-win32.exe>)

** When installing, ensure you check the box saying 'add to path' or else Emtune will not be able to find the compiler.

To add a new function, you need to create a source file for the function. **The file extension must be .c and not contain any spaces.**

There is an example file in the source directory for the users to use as a template: 

Example: testfunction.c

The new file should look like this (don't worry too much about the icon):

![Image](</img/NewItem791.png>)

Open the file in a text editor compatible with .c files such as -  Notepad++ [*https://notepad-plus-plus.org/downloads/*](<https://notepad-plus-plus.org/downloads/>)

To get started you can paste the following into your new math function as a starting point:

#include "math_function.h"

char *name(void) { return "derivative"; }

char *description(void)

{

    return "Calculates the derivative of the provided parameter.\\n\\n"

           "Input Parameters:\\n"

           "Required=1\\n"

           "Optional=0\\n"

           "Required Parameter 1: The parameter to differentiate\\n\\n"

           "Input Values:\\n"

           "Required=1\\n"

           "Optional=0\\n"

           "Required Input 1: Derivative gain. A scaler applied to the output. Set to 1 if "

           "unused.\\n"

           "";

}

typedef struct {

    int channelCount;

    float gain;

    float previousValue;

} Impl;

int initialise(int argc, float argv[], void *memory)

{

    if (argc != 2) {

        return -1;

    }

    Impl *impl = (Impl *)memory;

    impl->channelCount = argv[0];

    impl->gain = argv[1];

    impl->previousValue = 0;

    return 0;

}

int nextValue(float inputValues[], float timeDeltaSeconds, float *outputValue, void *memory)

{

    Impl *impl = (Impl *)memory;

    float difference = inputValues[0] - impl->previousValue;

    if (timeDeltaSeconds != 0) {

        *outputValue = impl->gain * (difference / timeDeltaSeconds);

    } else {

        *outputValue = 0;

    }

    impl->previousValue = inputValues[0];

    return 0;

}

** The file in the source folder called math_function.h contains more technical information about how the math functions work.

This is the source for the derivative function shipped with Emtune.

Once pasted in, at the very least, the function name must be renamed.

Changed the line:

char *name(void) { return "derivative"; }

to

char *name(void) { return "testfunction"; }

This is the name that will appear in Emtune in the dropdown list.

Save the file.

Back in emtune, click the button 'Recompile' which is left of the highlighted button in the first screen shot.

The function will now be available to select from the dropdown list. \


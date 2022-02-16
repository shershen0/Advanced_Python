16.02.22

##Easy
Write a function to generate tables. A double list is received at the input, and a string with a formatted valid latech is output. You can check that the latech is valid, for example, in Overleaf.

The string needs to be saved in a .tex file and it will be an artifact for this task.

##Medium
Write a function to generate images in latech.

Use the picture from the first homework as a picture, BUT:
You need to compile the code from the first DZ into the library using setuptools/conda-build, put it in the repository
If the first DZ is not done, then assemble any package that generates an image
Install the library, generate an image

After that, generate a PDF with a table from the easy task and a picture based on the received latech. PDF is the first artifact of the task, the link to the repository in PyPI/Anaconda is the second.
You can generate pdf using pdflatex. But in order for it to work, you need the distribution of the tech itself. There are many different ones

##Hard

Most likely, for the Medium task, you have installed some binary latech dependencies with your hands. If another developer wants to reuse your code, then he will have to do the same. To avoid this, Docker is usually used.

The task is to write a Dockerfile and generate a pdf using docker.

The artifact will be the Dockerfile itself, it can be left in the hw02 folder

You can use docker compose
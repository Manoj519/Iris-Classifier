# Iris-Classifier
Classify the iris flowers dataset by length and width.

## There are some steps to set-up the project.

### 1.) Folder Making
Make a folder in any drive(eg. F:\Iris_Data).

### 2.) Download Project
Download project in "Iris_Data" folder.

### 3.) Create Virtual Environment
###### Install Virtual Environment
```Pip install virtualenv```<br/>
This command type in command prompt at specific location(eg. F:\Iris_Data).<br/>

###### Folder Creation
```Virtualenv myenv```<br/>
This Command create virtual environment with myenv folder automatically.<br/>
Now here 4 folder and 7 files are present : <br/>
A.) .idea (folder)<br/>
B.) .ipynb_checkpoints (folder)<br/>
C.) iris_project (Project)<br/>
D.) myenv (Virtual Environment)<br/>
E.) Iris data.html (html file for visualization of code.)<br/>
F.) Iris data.ipynb (A python notebook file.)<br/>
G.) requirement.txt (text file with all packages.)<br/>
H.) model.pkl<br/>
I.) frocfile<br/>
J.) .gitignore<br/>
K.) README.md <br/>

###### Enter Into Virtual Environment
```F:\Iris_Data>myenv\scripts\activate```<br/>
Now activate the virtual environment by above command. And it will change<br/>
```(myenv) F:\Iris_Data>myenv>```

###### Install Django and Other Packages<br/>
```pip install -r requirements.txt```<br/>
Using this command django and other libraries install automatically.<br/>

### 4.) Open Project
Open Pycharm and tab on open and select the "iris_project" folder as project.

### 5.) Makemigrations
Now back to command prompt and type <br/>
```Python manage.py makemigrations```<br/>
(eg. (myenv) F:\Iris_Data>myenv>Python manage.py makemigrations).

### 6.) Migrate
```Python manage.py migrate```<br/>
(eg. (myenv) F:\Iris_Data>myenv>Python manage.py migrate).

### 7.) Run Server
```Python manage.py runserver```<br/>
(eg. (myenv) F:\Iris_Data>myenv>Python manage.py runserver).<br/>
This will run the server and give the localhost path in it.(eg. http://127.0.0.1:8000/)<br/>
Copy the url from your command prompt and paste on browser and enjoy the project.

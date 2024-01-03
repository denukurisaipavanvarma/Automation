# Steps to take this code in your machine
### Clone this project using in your local machine:
git clone https://github.com/denukurisaipavanvarma/Automation.git

Note:Git needs to be installed in your local machine

# Prerequisite for this project
Python3.+ version needs to be installed
IDE-Pycharm 

# Required libraries installation:
Once code cloning is done, we need to navigate "/Automation" folder in your local machine

### Perform this command:
pip3 install -r requirements.txt

### Then check the below libraries are installed are not by entering the bellow command:
pip3 list

-----
behave
requests
-----

# Scenario execution:
### To run all the scenarios: behave <feature_file>.feature
Example: ~/Automation/features behave users_api.feature

### To run the individual scenarios by using tags: behave --tags=@<tag_name>
Example: ~/Automation/features behave --tags @smoke

### To run the scenario by passing the input from behave command:
~/Automation/features behave pass_input_from_commandline.feature -D url="https://reqres.in/api/users" 


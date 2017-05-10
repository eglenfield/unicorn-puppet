# Puppet Run Analyser

If you would like to install the application locally and run the data gathering bash script yourself, you will need to be on a Linux/Unix machine, where you will run the following command:

`git clone https://gitlab.eeecs.qub.ac.uk/40101382/puppetrunanalyser.git`

You will also need permission to access the EEECS Gitlab domain. When the repository has been downloaded successfully, make sure you have the following software installed to utilise all application functionality:

-	Vagrant
-	VirtualBox
-	Python >= 3.5.2
-	Pip (a Python package manager); with Pip installed you will need to install
-	Django
-	Heroku (if you have homebrew installed Heroku with it)

Django can be installed with pip, and Heroku can be installed with brew using the following command:

`brew install heroku`

Once you have the required software installed, to run the data gathering bash script, simply enter the following into the terminal:

`./data.sh`

The script then runs through various conditions to first determine if it is running on a Darwin operating system, and if it is not to run the Vagrant command ‘vagrant up’. The Vagrant command gathers the relevant boxes, and provisions each box using the vagrant_script.sh file to gathering data regarding each machine. After the execution of the scripts, an inventory_files will be generated with four files inside it, one for each node.

Once the inventory files have been added to the inventory files directory (check to confirm), you can now run the application to migrate the data to the database. Using the command line from the main directory, type the following command:

`python3 manage.py runserver`

# Puppet Run Analyser

To run the analyser you will need to have the following software installed:

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


# unicorn-puppet
An analyser of puppet managed systems. Using bash, Python and R to gather data from a puppet run and display the similarities between their packages, users and groups - colourful and magic filled, hence unicorn-puppet!

## What you'll need to have installed
To run the analyser you'll need to have:
* Vagrant
* (by extent) Virtualbox or VMWare Fusion
* Python 2.7.10 (and above)
* Text editor of choice (I used vim for convenience) 

## Run
First run `vagrant up`. Once that completes, you will have two directories created, **files** and **inventory_files**. **inventory_files** will contain the data structure output from running `puppet inventory` on the vagrant machines. Next run the python parser from the top level dir by running `python python_parser.py`.

## Vagrant
On `vagrant up` the Vagrant file creates and provisions (running the bash script vagrant_script.sh) a Debian, Ubuntu and Centos machine. The boxes for each machine are all puppetlabs boxes, so all have puppet preinstalled.

## Bash script
The script is run when vagrant is provisioning the machines, where it checks the operating system (and distro) to install a puppet module ([puppetlabs-inventoy](https://github.com/puppetlabs/puppetlabs-inventory)) and output the data structure describing properties of the system on which it's run. This is then used by the python parser and separated into packages, versions, users and volumes.



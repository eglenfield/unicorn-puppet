# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.synced_folder "inventory_files/", "/tmp/inventory"
  config.vm.provision "shell", path: "vagrant_script.sh"
  config.vm.synced_folder ".", "/vagrant", type: "rsync" # or "rsync"

  config.vm.define "debian" do |debian|
    debian.vm.box = "puppetlabs/debian-7.8-64-puppet"
  end

  config.vm.define "ubuntu" do |ubuntu|
    ubuntu.vm.box = "puppetlabs/ubuntu-16.04-32-puppet"
  end

  config.vm.define "centos" do |centos|
    centos.vm.box = "puppetlabs/centos-7.2-64-puppet"
  end

end

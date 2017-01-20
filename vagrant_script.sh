#!/bin/bash
# Check if OS is Unix or Linux based
if [ "$(uname)" == "Darwin" ]; then
  # Is puppet installed?
  if ps ax | grep -v grep | grep puppet > /dev/null
    then
      puppet module install puppetlabs-inventory
    else
      # Install puppet if it isn't
      curl -O https://downloads.puppetlabs.com/mac/10.11/PC1/x86_64/puppet-agent-1.8.0-1.osx10.11.dmg
      sudo hdiutil mount puppet-agent-1.8.0-1.osx10.11.dmg
      sudo installer -pkg /Volumes/puppet-agent-1.8.0-1.osx10.11/puppet-agent-1.8.0-1-installer.pkg -target /
      sudo hdiutil unmount /Volumes/puppet-agent-1.8.0-1.osx10.11
      rm -rf puppet-agent-1.8.0-1.osx10.11.dmg
    fi
  # Outputs puppet run into inventory file
  puppet inventory > inventory_files/inventory.json
# For all Linux distros
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
  # Checks if puppet is installed first instead of a check for each distro
  if ps ax | grep -v grep | grep puppet > /dev/null; then
    echo "Puppet is running"
      # The package lsb_release is found on Debian and Ubuntu machines
      # So this narrows those down
      if [ -f /etc/lsb-release ] && echo "lsb_release package installed" || echo "lsb_release package not installed"; then
        if lsb_release -is | grep -q "Debian"; then
          echo "Debian machine"
          puppet module install --force puppetlabs-inventory
          mkdir -p /etc/puppet/modules
          puppet module install --force puppetlabs-inventory
          cd /tmp/inventory
          puppet inventory --verbose
          puppet inventory > inventory-debian.json
        elif lsb_release -is | grep -q "Ubuntu"; then
          echo "Ubuntu machine"
          sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 7F438280EF8D349F
          puppet module install puppetlabs-inventory
          cd /tmp/inventory
          puppet inventory
          puppet inventory > inventory-ubuntu.json
          set +x
        fi
      elif [ cat /etc/redhat-release | grep -q "Centos" ]; then
        echo "Centos machine"
        puppet module install puppetlabs-inventory
        cd /tmp/inventory
        puppet inventory
        puppet inventory > inventory-centos.json
      fi
    else
      # For some machines after puppet is installed the service isn't running automatically
      echo "Puppet was not running"
      puppet resource service puppet ensure=running enable=true
      if [ -f /etc/lsb-release ]; then
        if lsb_release -is | grep -q "Debian"; then
          echo "Debian machine"
          puppet module install --force puppetlabs-inventory
          cd /tmp/inventory
          mkdir -p /etc/puppet/modules
          puppet module install --force puppetlabs-inventory
          puppet inventory
          puppet inventory > inventory-debian.json
        elif lsb_release -is | grep -q "Ubuntu"; then
          echo "Ubuntu machine"
          set -x
          sudo puppet module install puppetlabs-inventory
          cd /tmp/inventory
          puppet inventory
          puppet inventory > inventory-ubuntu.json
          set +x
        fi
      # Strangely Debian and Ubuntu both have puppet running but Centos does not
      # It also doesn't work if you include the last bracket  
      elif [ -f /etc/redhat-release ] && echo "Redhat machine" || echo "Not Redhat Machine"; then
        echo "Centos machine"
        puppet module install puppetlabs-inventory
        cd /tmp/inventory
        puppet inventory --verbose
        puppet inventory > inventory-centos.json
      fi
    fi
fi

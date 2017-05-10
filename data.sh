mkdir -p inventory_files
mkdir -p files

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
  puppet inventory > inventory_files/inventory-mac.json
fi
vagrant up

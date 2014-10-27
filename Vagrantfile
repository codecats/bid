# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "bid"
  config.vm.box_url = "https://dl.dropboxusercontent.com/u/197673519/debian-7.2.0.box"
  # config.vm.network "forwarded_port", guest: 80, host: 8080
  # using a specific IP.
  config.vm.network "private_network", ip: "192.168.50.4"
  config.vm.synced_folder "src/", "/bid"
  #Some errors may be resolved in graphical mode
  #config.vm.provider :virtualbox do |vb|
  #  vb.gui = true
  #end
end

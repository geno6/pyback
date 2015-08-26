# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # Set memory and cpu size
  config.vm.provider "virtualbox" do |v|
    v.customize ["modifyvm", :id, "--memory", "2048"]
    v.customize ["modifyvm", :id, "--cpus", "2"]
  end

  # Vagrant box
  config.vm.box = "ubuntu/trusty64"

  # Network
  config.vm.network :forwarded_port, guest: 80, host: 8000, auto_correct: true
  config.vm.network "private_network", ip: "192.168.10.10"

  # Shared
  config.vm.synced_folder ".", "/var/www", :nfs => true

  # Configure virtual host name
  config.vm.hostname = "pyback"
end
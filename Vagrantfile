# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # Vagrant box
  config.vm.box = "ubuntu/trusty64"

  # Network
  config.vm.network "private_network", ip: "192.168.10.10"
  config.vm.network :forwarded_port, host: 8000, guest: 80

  # Shared
  config.vm.synced_folder ".", "/var/www", type: 'nfs'

  # Provisioning
  config.vm.provision :puppet, :module_path => "puppet/modules" do |puppet|
    puppet.manifests_path = "puppet/manifests"
    puppet.manifest_file = "default.pp"
    puppet.options = "--hiera_config /vagrant/puppet/manifests/hiera.yaml"
  end
end
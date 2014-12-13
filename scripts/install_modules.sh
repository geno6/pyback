#!/bin/sh

if [ $1 != "" ]; then

	# Install modules
    puppet module install puppetlabs-mysql
    puppet module install stankevich-python
    puppet module install jfryman-nginx
    puppet module install puppetlabs-mongodb
    puppet module install ajcrowe-supervisord
    #configure modules

    sudo puppet apply puppet/manifests/local.pp
else
	echo "Please provide environment name"
fi
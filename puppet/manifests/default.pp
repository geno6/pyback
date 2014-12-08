#-----------------------------------------------------------------------------------------------------------------------
# Ensure that Puppet is installed
#-----------------------------------------------------------------------------------------------------------------------

group { "puppet":
	ensure => present,
}

#-----------------------------------------------------------------------------------------------------------------------
# APT Update
#-----------------------------------------------------------------------------------------------------------------------

exec { "apt-get update":
    command => "/usr/bin/apt-get update",
}

#-----------------------------------------------------------------------------------------------------------------------
# Check for required packages
#-----------------------------------------------------------------------------------------------------------------------

package { "vim":
    ensure => present,
}

#-----------------------------------------------------------------------------------------------------------------------
# Check for directories
#-----------------------------------------------------------------------------------------------------------------------

file { "/var/www/":
    ensure => "directory",
}

#-----------------------------------------------------------------------------------------------------------------------
# Python
#-----------------------------------------------------------------------------------------------------------------------

#class { "python" :
#
#    version => "3.4",
#    pip => true,
#    dev => true,
#    virtualenv => true,
#    gunicorn => true,
#}
#
#include python

#-----------------------------------------------------------------------------------------------------------------------
# MySQL
#-----------------------------------------------------------------------------------------------------------------------

class mysql {

    # root mysql password
    $mysqlpw = "root"

    # install mysql server
    package { "mysql-server":
        ensure => present,
        require => Exec["apt-get update"]
    }

    #start mysql service
    service { "mysql":
        ensure => running,
        require => Package["mysql-server"],
    }

    # set mysql password
    exec { "set-mysql-password":
        unless => "mysqladmin -uroot -p$mysqlpw status",
        command => "mysqladmin -uroot password $mysqlpw",
        require => Service["mysql"],
    }
}

#-----------------------------------------------------------------------------------------------------------------------
# NGINX
#-----------------------------------------------------------------------------------------------------------------------

class nginx {

    package { "nginx":
        ensure => "present",
        require => Exec["apt-get update"],
    }

    service { "nginx":
        ensure  => "running",
        require => Package["nginx"],
    }
}

#-----------------------------------------------------------------------------------------------------------------------
# Includes
#-----------------------------------------------------------------------------------------------------------------------
include mysql::server::secure
include nginx
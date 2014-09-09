# Docker usage inside crouton on a chromebook

## Requirements

- A chromebook installed with Ubuntu 14.04
- Properly installed Virtualbox. see: https://github.com/dnschneid/crouton/wiki/Build-kernel-headers-and-install-Virtualbox-(x86) for details
- Enabled VT_X for virtualbox. see: https://github.com/dnschneid/crouton/wiki/Repack-kernel-to-Enable-VT_x-for-Virtualbox for details
- Installed vagrant. https://www.vagrantup.com/
- Installed ansible. www.ansible.com/


## Steps
- clone this repository  
- change directory to it
- start vagrant;
     
     vagrant up

- Vagrant will provision a virtual machine installed with ubuntu 14.04 and also install docker among a few other packages. see the file provisioning/start.yml
- Once vagrant finishes provisioning, ssh into the virtual machine(VM)
     
     vagrant ssh

- Once in the VM, change directory to the

## Docker usage inside crouton on a chromebook

`we will run a small django app using docker in ubuntu in a chromebook.`

## Requirements

- A chromebook installed with Ubuntu 14.04
- Properly installed Virtualbox. see: https://github.com/dnschneid/crouton/wiki/Build-kernel-headers-and-install-Virtualbox-(x86) for details
- Enabled VT_X for virtualbox. see: https://github.com/dnschneid/crouton/wiki/Repack-kernel-to-Enable-VT_x-for-Virtualbox for details
- Installed vagrant. https://www.vagrantup.com/
- Installed ansible. www.ansible.com/


## Steps
- clone this repository into /home/docker_chromebook
    its important you clone it to that directory since it will be used by the ansible provisioning script. But you can clone it to any directory so long as you change the ansible task(copy app dir) found in provisioning/start.yml to point to your new directory.     
- change directory to it
    `cd /home/docker_chromebook`
- start vagrant;
     `vagrant up`

- Vagrant will provision a virtual machine installed with ubuntu 14.04 and also install docker among a few other packages. see the file provisioning/start.yml
- Once vagrant finishes provisioning, ssh into the virtual machine(VM)
     `vagrant ssh`

- Once in the VM, change directory to /home/appdir/docker_chromebook (or wherever you asked ansible to copy the project directory to)
- Build a docker image using the Dockerfile in this project
     `sudo docker build -t test_img .`

- This will create an image called test_img
- Now lets create an app/container based of this image
     `sudo docker run --name test_app -v /home/appdir/docker_chromebook:/home/appdir/docker_chromebook -p 7000:7000 -i -t test_img make run`

- This creates a container named test_app and we are using the -v option to 'attach' the application directory to the container and we are also exposing the port 7000
- We are also 'executing' the make run command. If you open the Makefile, you'll see that this just installs the application requirements, syncdb and then runserver.

- Go to; `http://localhost:7000/` in your host machine and your app will be running there.

- NB: 
That in the Dockerfile we exposed port 7000. If you look inside the Vagrantfile, this is the same port we forwaded.       
The app is running in a container inside a VM inside Ubuntu in a chromebook. Thats many levels of 'virtualization'       
Its important that you expose the same port in your Dockerfile as is forwarded in your Vagrantfile.


# Enjoy
- Questions can be addressed to: 
      `komuw05 [at] gmail [dot] com`


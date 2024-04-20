+++
title = "Libvirt networking libraries"
slug = "libvirt-networking-libraries"
date = 2015-01-14T21:06:57+03:00
tags = ['networking', 'linux', 'virtualization', 'infrastructure']

+++

Fedora 21 workstation seems to come with a lot of virtualization
features and most of the `libvirt` libraries installed. I only had to
add the `KVM virtual-manager` which is the KVM application I am more
familiar with. However, the new version of the `libvirt*` libraries have
networking features that are great for the data centre environment, but
maybe not the best option for a particular workstation, so I added the
following packages in order to set up an easier network configuration
for my local virtual machines.

``` bash
sudo dnf install virt-install libvirt-daemon-config-network
```

In order to reflect the changes and start using the new features, we
need to restart its service:

``` bash
systemctl restart libvirtd.service
```

After that, when creating a new virtual machine, the NAT option is
enabled, and the virtual manager with handle the NAT or bridging
configuration automatically, which allows me to deploy new machines
faster.

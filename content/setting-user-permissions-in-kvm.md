+++
title = "Setting user permissions in KVM"
slug = "setting-user-permissions-in-kvm"
date = 2015-06-20T20:46:58+03:00
[taxonomies]
tags = ['linux', 'virtualization', 'infrastructure']
+++

In a [previous article](link://slug/libvirt-networking-libraries) I
mentioned how to install a library in Fedora, in order to make
`KVM virtualization` easier, managing the `NAT` network configuration
between the guest virtual machine and the host, by means of `libvirt`.

Besides that, while using `KVM` locally for development, I use
`virt-manager`, a helpful application that manages the different virtual
machines. This application, as well as the rest of the commands that
interact with `libvirt` (`virsh` for example), require super user
privileges, so it will prompt for the `sudo` password every time.

This can be avoided by including the user into the following groups:
`kvm`, and `libvirt`.

Therefore, just by running the following command we can skip the
password prompt every time.

``` bash
sudo usermod -a -G kvm,libvirt mariano
```

This is an option I would use only for local development on my machine.
Productive environments must have an strict permissions management.

# simultaneous_user_test
Multiple users created by Vagrant and automated with Ansible to set all up the test environment. To better balance the traffic we have used two hardware devices:

- Lanner NCA-1510 (8CPUs, 16GB RAM, 1TB) capacity for 20 Vagrant VMs.
- Lanner NCA-1516 (16CPUs, 64GB, 1TB) capacity for 30 Vagrant VMs.

  
This is the folder structure for both devices running Ubuntu 22.04 LTS. 
```
playbook/
├── server01/
│   ├── Vagrantfile
│   ├── ansible.cfg
│   ├── inventory/
│   │   └── hosts.ini
│   └── vms_02.yml
└── server02/
    ├── Vagrantfile
    ├── ansible.cfg
    ├── inventory/
    │   └── hosts.ini
    └── vms_02.yml
```
**Note:**
  Server01 ==> Lanner NCA-1510
  Server02 ==> Lanner NCA-1516

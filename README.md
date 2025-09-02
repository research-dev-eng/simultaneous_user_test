# Simultaneous User Test
This project creates multiple users with **Vagrant** and automates the setup of the test environment using **Ansible**.  
To better balance traffic, we used two hardware devices:

- **Lanner NCA-1510** – 8 CPUs, 16GB RAM, 1TB (capacity for 20 Vagrant VMs)  
- **Lanner NCA-1516** – 16 CPUs, 64GB RAM, 1TB (capacity for 30 Vagrant VMs)  

---

## 📂 Project Structure

This is the folder structure for both devices running **Ubuntu 22.04 LTS**:
```text
playbook/
├── server01/
│   ├── Vagrantfile
│   ├── ansible.cfg
│   ├── inventory/
│   │   └── hosts.ini
│   └── vms_01.yml
└── server02/
    ├── Vagrantfile
    ├── ansible.cfg
    ├── inventory/
    │   └── hosts.ini
    └── vms_02.yml

**Note:**
- Server01 ==> Lanner NCA-1510
- Server02 ==> Lanner NCA-1516

ec2ctl
======

Control EC2 instances script


## Users

- EC2 users who Start and Stop EC2 Instances on demand.
- Individual EC2 users. Only you can access your EC2 instances.


## Installation

- Install boto
- Set credentials to ~/.boto
- Get ec2ctl.py from git
- Edit user variables in ec2ctl.py


## Command lines

### Power on EC2 Instance
Power on EC2 Instance.

```
$ python ec2ctl.py start
```

### Shutdown EC2 Instance
Shutdown EC2 Instance.

```
$ python ec2ctl.py stop
```

### Show EC2 Instance status

```
$ python ec2ctl.py status
```








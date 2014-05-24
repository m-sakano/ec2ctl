ec2ctl
======

Control EC2 instances script


## Users

- EC2 users who Start and Stop EC2 Instances on demand.
- Individual EC2 users. Only you can access your EC2 instances.


## Command Functions

- Control existing EC2 instances power (Start|Stop|Status).
- Set AWS Security Group acceessible from only your IP.
- Set AWS Security Group acceessible from no any IP.
- Show AWS Security Group if acceessible from any IP.


## Command lines

### Power on EC2 Instance

```
$ ec2ctl <Instance ID> start
```

### Shutdown EC2 Instance

```
$ ec2ctl <Instance ID> stop
```

### Show EC2 Instance status

```
$ ec2ctl <Instance ID> status
```

### Set AWS Security Group acceessible from only your IP

```
$ ec2ctl <Group ID> set
```

### Set AWS Security Group acceessible from not any IP

```
$ ec2ctl <Group ID> unset
```

### Show AWS Security Group status if acceessible

```
$ ec2ctl <Group ID> status
```


## User Scripts

### myEC2Start.sh

### myEC2Stop.sh







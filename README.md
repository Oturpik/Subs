# To Do: Data Storage Dilemma

Problem Statement:

You're tasked with creating data storage solutions using Amazon EBS and EFS for different use cases.

# Guidelines/Goals:

1. Amazon EBS Setup:

Create an Amazon EBS volume and attach it to an EC2 instance.

Format and mount the volume to a specific directory.

2. Use EBS for Application Data:

Create a simple text file on the EBS volume.

Ensure the data persists even if the instance is stopped and started.

3. Amazon EFS Setup:

Create an Amazon EFS file system.

Mount the file system on multiple EC2 instances.

4. Use EFS for Shared Data:

Create a file on one instance and verify its presence on another.

Observe how changes to the file on one instance are reflected on the other.


# Solution

1. Amazon EBS Setup:
* Launch an Amazon EC2 instance.
* In the AWS Management Console, go to "Elastic Block Store" (EBS).
* Click on "Create Volume" and configure the EBS volume with the desired size, type, and availability zone. Use the same AZ as the instance.
* Once the EBS volume is created, note the volume ID.
* Attach the EBS volume to your EC2 instance by selecting the EC2 instance and choosing "Actions" > "Attach Volume." Choose the instance created above.
* Connect to the EC2 instance.
* Format the EBS volume.

sudo mkfs -t ext4 /dev/xvdf

* Create a directory where you want to mount the EBS volume:

sudo mkdir /data

* Mount the EBS volume to the directory:

sudo mount /dev/xvdf /data

* Add an entry to `/etc/fstab` to ensure the volume is mounted at boot:

echo '/dev/xvdf /data ext4 defaults 0 0' | sudo tee -a /etc/fstab

2. Use EBS for Application Data:

* Create a simple text file on the mounted EBS volume:

Curl <file link here> >sampledoc.pdf

* The data will persist on the EBS volume even if the EC2 instance is stopped and started.

3. Amazon EFS Setup:

* In the AWS Management Console, go to "Elastic File System" (EFS).
* Click on "Create file system" and configure it.
* After creating the EFS file system, note the file system ID.
* In your EC2 instances, install the NFS client package if not already installed:

sudo yum install nfs-utils

* Mount the EFS file system on your EC2 instances:

sudo mount -t nfs -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 < my-EFS-DNS-Name>:/ /mnt/efs

* Add an entry to `/etc/fstab` to mount the EFS file system at boot.

If you get the error message "mount point /mnt/efs does not exist" it suggests that the specified mount point directory (/mnt/efs) does not exist on your EC2 instance.

To resolve this issue, you should create the mount point directory before attempting to mount the EFS file system:

1. SSH into your EC2 instance.
2. Create the mount point directory (/mnt/efs) if it doesn't exist:

sudo mkdir -p /mnt/efs

3. Now, attempt to mount the EFS file system to this directory:

sudo mount -t nfs -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 <my-EFS-DNS-Name>:/ /mnt/efs

Creating the mount point directory should let you successfully mount the EFS file system without encountering the "mount point /mnt/efs does not exist" error.

4. Use EFS for Shared Data:
* Mount the EFS system on multiple EC2 instances following the process above.
* Create and modify files in the shared directory (`/mnt/efs`) from any of the instances. Changes made to a file on one instance will be reflected on all other instances that have the EFS file system mounted.


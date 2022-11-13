# Linux Command Line

## Seeing files
1. ls

### Seeing all files
1. ls -a
2. ls -al

### Seeing non-hidden files
1. ls -A
2. ls -l
3. ls -lrt

## Linux commands
1. man
    * man wget - Guide and descriptions how to use commands 
2. wget
    * wget "file", wget is used to download files from a url or over the network
3. sudo
    * sudo apt update
    * sudo apt install "package"
4. apt install
5. apt update
6. cd
7. cat
8. clear
9. history
10. touch
11. mkdir
12. rm
  * rm ...
  * rm ...?
13. pwd
14. nano 
15. cp
  * cp file* directory/
16. rmdir
17. grep - Filter out lines that contain text
18. ">>" put content into a newfile
  * can use one >, but that overwrites existing data
19. cut
20. sort
21. tar
22. lsmod - List modules
23. modprobe - Load a module
24. wc - word count
25. locate
26. updatedb
27. systemd
28. chmod

## Kernel
Most files are in the lib/modules/version/kernel directory <br>
Receive version: 
```
uname -r
```

## Network
1. ip route show or route
2. dhclient
3. ip addr or ifconfig
4. netstat -i or netstat -l
5. ss -i

## DNS
1. host "website"
2. ping 8.8.8.8
3. scp

IPv4, NAT, IPv6

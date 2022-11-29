# Checking Bash System

proc directory shows many stats to look at, such as cpu, memory, drivers and much more <br> 
<br>
Use commands to uncover certain details:
```
top
```

```
less ....
```

```
... info
```
Where "..." is a variable to inspect

```
free
```
or 
```
free -h
```

```
df command volume_to_inspect
```

```
ps
```
Shows the following information:
1. PID
2. TTY
3. TIME
4. CMD

```
kill
```
Use kill command to delete a PID or use killall Which deletes everything. Not recommended
```
killall yes
```

Enable and Disable a program:
```
systemctl enable ....
```

```
systemctl disable ....
```

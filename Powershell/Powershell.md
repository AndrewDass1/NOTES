# Powershell

## Execution Policy
1. Restricted - Can't run powershell script
2. RemoteSigned - Runnable, does not run downloaded scripts from internet. Digital Cert issues. <br>
  Use the command below to run a script in RemoteSigned setting from the internet ``` "unblock-file" ... ```
3. AllSigned - Scripts has been signed, run it. Otherwise no.
  Use the command below to change the setting
```
Set-ExecutionPolicy allsigned -Force
```
4. Unrestricted - Good for testing, not for finalized apps
5. ByPass - 

## Set the Execution Policy
```
Set-ExecutionPolicy ...
```

```
Get-ExecutionPolicy
```

## Script Extensions



## Make a file
```
New-Item driveletter:\fulldirectory...\...\file
```
Edit the file
```
Set-Content driveletter:\fulldirectory...\...\file 'Write anything here'
```
Read the file
```
get-Content .....
```


## Run a Script
Use the full path name <br>
Example: .\...\...\file.extension <br>
or in the same directory as file: <br>
.\filename.extension


## Open a Directory
invoke-item .

# How to Write Powershell Scripts

## Writing Scripts Basics

### If and Else Statements
$variable="value"
```
if($variable)
{
  Write-Output "The $variable ...."
}

elseif($variable)
{
  Write-Output "....."
}

else
{
  Write-Output "The $variable ...."
}
```

## Scopes
1. MachinePolicy
2. UserPolicy
3. Process
4. CurrentUser
5. LocalMachine

## Policies

1. All Signed
2. Bypass
3. Remote Signed
4. Restricted
5. Unrestricted

```
Get-ExecutionPolicy -List
```

Change the Policy
```
Set-Execution Policy ....
```

Specific Change the Policy
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
```

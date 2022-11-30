# How to Write Powershell Scripts

## Arithmetic Operations
"+" : add <br>
"-" : subtract <br>
"/" : divide <br>
"*" : multiply <br>

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

## Two Comparisons
if(($var1 -eq $var2) -and ($var1 -eq $var3))
* Can use -or

## Operations
1. -eq : equal
2. -gt : greater
3. -like : Is value1 like value2
4. -match : Do two values match each other
5. -contains : Does a variable contain a value 
6. -in : Is a value in another variable

```
if ($var1 ... $var2)
```

## Alternative to if and else, using ? marks
($var1 -eq $var2) ? $true : $false

## Make an Array
```
1..20
```
This example shows an array was created holding the numbers from 1 to 20 <br>
Can use -contains and -in to look at arrays


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

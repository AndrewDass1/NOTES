# More Powershell Scripting Techniques

## Casting 
$string1="3" <br>
<br>
[int]$string1 or $string1 -as [Int]

## Ways to make an Array
Method 1
```
$Empty = @()

$var1 = @(1, 2, 3)
```

Method 2
```
$var1 = '1', '2', '3'

```

Method 3
```
$var1 = Write-Output 1 2 3
```

## Getting Array Values
$var1[0] <br>
$var1[0,1,2] (multiple values)

## Make a Function
```
function Invoke-Message() { Write-Host "Some Text" }
```

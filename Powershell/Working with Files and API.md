# Read Files

Open a file
```
Invoke-Item "filepath\file"
```

Retrieve Data
```
Get-Process a*
```

```
Get-Content filepath\file
```

Save files
```
$var.Save(give_filepath_to_where_it_is_saved)
```

## JSON
1. ConvertFrom-Json
2. ConvertTo-Json

```
command | select * | ConvertTo-Json -AsArray
```

## XML

Import Commands: <br>
1. Export-CliXml
2. Import-CliXml
3. ConvertTo-Xml

Export to file in directory
```
filename | Export-Clixml -Path "filepath\file"
```

# APIs
1. Invoke-WebRequest
2. Invoke-RestMethod

# How to make an API in Powershell

## Four Rules 
1. POST
2. GET
3. PUT
4. DELETE

## Receive information from a Website
```
Invoke-RestMethod -Uri "URL"
```
or defined variable in place of "-Uri URL", and Add "-WebSession" to remember variable at the end

```
ConvertTo-...
```
Refer to documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/?view=powershell-7.3

## Retrieve from REST API
```
$declare_var = @{
  Uri = "Url"
  Credentials or Token = example
  Authentication = example2
  WebSession = example3  including WebSession is optional
}
```

Use an OAuth Token
```
$token = "" | ConvertTo-SecureString -AsPlainText -Force
```

## Four Rules
### Post
```
$declare_var = @{
  Method = "POST"
  json_url = ""
  variable = $...
  url_and_variable_copied_to_file = "name_of_file"
}
```
Variable has to be converted to JSON

### Get
```
$declare_var = @{
  Method = "GET "
  ...
  ...
}

```


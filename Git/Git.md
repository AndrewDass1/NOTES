# Git Commands

## How to Upload Git Files to a Repository
```
git version
```
Check the Version

```
man git
```
Shows manual or documentation how to use Git and Git commands

```
git init
```
Initialize directory on computer to upload files onto Git or Github from

```
git config --global user.name ""
```
Add username from associated Github account to eventually upload files to a repoistory owned by that account

```
git config --global user.email ""
```
Add email from associated Github account to eventually upload files to a repoistory owned by that account


```
git config --list
```
List all the settings Git has

```
git add .
```
Add every file before pushing

```
git commit -m "first commit"
```
Shows the changes before making official changes to the repository

```
git remote add origin "github repo"
```
Specifies the Github repository that will be updated

```
git status
```
Shows the branch that new code or changes will be applied to

```
git push -u origin "branchname"
```
Push files to the specified branch name in to a repository

```
git commit -a -m "message"
```
Confirm the changes when new code or files was uploaded to the repository

```
git branch ""
```
Create a new branch in a repository 

```
git checkout main
```
Change to a different branch in a repository

## File Stages
1. Commit
2. Modify
3. Stage

## Staging commands
```
git status
```

```
git diff --staged
```
Compare stage commands to last ones

## Other Commands
```
git pull origin main
```

```
git pull origin main -- allow unrelated-histories
```

```
git push origin main
```

```
git config --global remote.origin.url "Github Repo"
```

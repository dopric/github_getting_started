# GitHub: Getting Started

<table>
    <tr>
        <th colspan="2">Pluralsight Training</th>
    </tr>
    <tr>
        <td>Author</td>
        <td>Gill Cleeren</td>
    </tr>
    <tr>
        <td>Duration</td>
        <td>4 hours</td>
    </tr>
</table>

## Working with SSH

# check if ssh exists
```
ls -al ~/.ssh
```

create ssh
ssh.keygen -t rsa -b 4096 -C "yourEmail@gmail.com"

Add to SSH Agent
```
eval $(ssh-agent -s) - check if agent is running

ssh-add ~/.ssh/id_rsa
```

Add to GitHub
Open directory users\myuser\.ssh and copy content of pub file and add to your git provider

Verify with
```
ssh -T git@github.com (commit with YES)
```

## Add remote origin
git remote add origin https://github.com/dopric/gh_getting_started.git
## verify
git remote -v
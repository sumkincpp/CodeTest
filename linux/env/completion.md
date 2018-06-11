
Installing bash-completion libraries

```bash
sudo yum install bash-completion
```

```bash
sudo apt-get install -y git-core bash-completion
```

# Git #

```
curl https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash -o ~/.git-completion.bash
```

```bash
if [ -f ~/.git-completion.bash ]; then
  . ~/.git-completion.bash
fi
```

# Kubectl #

```bash
source <(kubectl completion bash) 
```

# Git

```bash
--system/--global/--local
system-wide/user-wide/project-wide
#------------------------------------------------------------------------
- staging 
- most recent commit
- working directory
#------------------------------------------------------------------------

git config --list

git config --global user.name "<your_full_name>"
git config --global user.email "<your_email>"
git config --global core.editor "atom --wait"

# "auto carriage return line feed".
git config --global core.autocrlf
# Windows - true
# Mac/Linux - input

# Default pushing for current branch
git config --global push.default simple.

#------------------------------------------------------------------------
# available branches
git branch
# all remote branches
git branch -a
# new branch
git branch <new_branchname>
git checkout <new_branchname>
# OR
git checkout -b <new_branchname>
# Pushing local branch remotely ( at first!)
git push -u origin <branch_name>

# List local branches
git branch --merged
# Delete specific branch
git branch -d <branchname>
#------------------------------------------------------------------------
# work dir vs staged
git diff
# staged vs most committed ( staging vs history)
git diff --staged
# w&s compares with HEAD ( work& stage vs HEAD, history ) 
git diff HEAD
# word by word comparison
git diff --color-words
#------------------------------------------------------------------------
git log
git log --oneline --graph --decorate --all
git log --oneline --graph
git log --stat
git log --patch

$ git log --oneline --graph --decorate --all
*   0b5f8e4 (HEAD -> master, origin/master, origin/HEAD) Merge branch 'sumkincpp-branch'
|\
| * 95d8766 (origin/sumkincpp-branch) Update sumkincpp-branch
| * 7eccb13 new data from new local branch
| * 66f5d75 (origin/sumkincpp-more-bio) even more changes
| * e2e6d13 more bio
* | 31b03fb even more changes
* | 9ef17a2 more bio
|/
*   35feb78 Merge pull request #6 from sumkincpp/FedorSumkin
|\
| * 1ee14fd (origin/FedorSumkin) added fav color
| * 3fe5091 Create FedorSumkin.txt
* | 117b379 Create FedorSumkin.md
|/
| * 3142390 (origin/add-gitignore) Add gitignore file to ignore log
|/
* 8173a64 Update README.md
* c569ac5 change repo specific links
* ec0b89b initialize template repo
* 321618c Initial commit

$ git log --oneline --graph
*   0b5f8e4 Merge branch 'sumkincpp-branch'
|\
| * 95d8766 Update sumkincpp-branch
| * 7eccb13 new data from new local branch
| * 66f5d75 even more changes
| * e2e6d13 more bio
* | 31b03fb even more changes
* | 9ef17a2 more bio
|/
*   35feb78 Merge pull request #6 from sumkincpp/FedorSumkin
|\
| * 1ee14fd added fav color
| * 3fe5091 Create FedorSumkin.txt
* | 117b379 Create FedorSumkin.md
|/
* 8173a64 Update README.md
* c569ac5 change repo specific links
* ec0b89b initialize template repo
* 321618c Initial commit

#------------------------------------------------------------------------
# Modifying previous commit
# new files -> add to stage
git add file_that_we_forgot
# --ammend, i.e. modify previous commit, editor will open
git commit --ammend

#------------------------------------------------------------------------
# reverting file contents
git revert <file>
# unstaging file
git reset HEAD file.md

# Move my branch to point to commit, 
# working dir and staging are untouched( same state )
git reset --soft <my-branch> <other-commit>

# <my-branch> and the staging area look like the <other-commit> snapshot
# default mode, usefull for partial staging
git reset --mixed <my-branch> <other-commit>

# deletes LOCAL changes(all uncommittted)
git reset --hard <my-branch> <other-commit>

# When u need to reset initial commit, move HEAD before 1 commit(???)
# after that there is force available
git update-ref -d HEAD

#------------------------------------------------------------------------
# overwriting file with PREVIOUSLY committed version
git checkout -- HELLOW
#------------------------------------------------------------------------
# git aliases
git config --global alias.lol "log --oneline --graph --decorate --all"
# git lol
git config --global alias.co "commit -m"
# git co "message"

git config --global --unset alias.lol
#------------------------------------------------------------------------

# clone with one commit depth
git clone --depth=1 <blablabla>

# diff file on -2 revision
git diff HEAD~2 spin_glass_counter.hpp

# show file on -2 revision
git show HEAD~2:./spin_glass_counter.hpp

## Other useful commadns ##
git log --oneline

# show what files are changed
git log --name-only

# Changes in your branch that are on top of master
git log master.. --oneline
```

# working tree status with all files

```
git status -uall
```

# Git patches archive (from commit to HEAD)

```
git diff --name-only -z --diff-filter=ACMRT fa3de33a4 | xargs -0 git archive -o update.tar.gz HEAD --
```

# Git patches archive (from commit to HEAD)

```
git diff --name-only -z --diff-filter=ACMRT fa3de33a4 | xargs -0 git archive -o update.tar.gz HEAD --
```

# Git rebase

```
git rebase -i KEKEK --exec 'git commit --amend --author="NOPE <email@address.com>" --no-edit'
```

```
git rebase -i origin/main --exec 'GIT_COMMITTER_DATE="$(date)" git commit --amend --no-edit --date="$(date)"'
```


--system/--global/--local
system-wide/user-wide/project-wide

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

# clone with one commit depth
git clone --depth=1 <blablabla>

# diff file on -2 revision
git diff HEAD~2 spin_glass_counter.hpp

# show file on -2 revision
git show HEAD~2:./spin_glass_counter.hpp

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

# clone with one commit depth
git clone --depth=1 <blablabla>

# diff file on -2 revision
git diff HEAD~2 spin_glass_counter.hpp

# show file on -2 revision
git show HEAD~2:./spin_glass_counter.hpp

--system/--global/--local
system-wide/user-wide/project-wide

git config --list

# clone with one commit depth
git clone --depth=1 <blablabla>

# diff file on -2 revision
git diff HEAD~2 spin_glass_counter.hpp

# show file on -2 revision
git show HEAD~2:./spin_glass_counter.hpp

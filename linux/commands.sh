# Archiving
zip -r backup.zip data

tar -cf backup.tar data

tar -czf backup.tar.gz data

# unpacking to data folder
mkdir data
tar -cf backup.tar -C data

# Code coloring with enscript
enscript -2rG --line-numbers -p - --word-wrap --highlight=javascript --color=0 untitled.js | pstopdf -i -o ~/out.pdf && open ~/out.pdf

enscript -1rG --line-numbers -p - --highlight=javascript --color=0 -c untitled.js | pstopdf -i -o ~/out.pdf && open ~/out.pdf

# Show PATH entries, one entry per line
echo $PATH | tr : '\n'


ssh-keygen -t rsa -C "blablabla@localhost"

# Generate key fingerprint
ssh-keygen -lf ~/.ssh/id_rsa.pub

# Checking connection to repo
ssh -vT git@github.com
ssh -vT git@bitbucket.org

mount -o loop disk.iso /mnt/disk
umount /mnt/disk

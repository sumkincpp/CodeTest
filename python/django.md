
```bash
python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py startapp someapp
python3 manage.py dumpdata -o data.json blog.Comment blog.Tag blog.Post auth.User
python3 manage.py loaddata data.json
```

```
pip3 install django-registration
```

```
python manage.py shell

from django.contrib.auth.models import User
user = User.objects.get(username='your username')
user.set_password('raw password')
user.save()

python manage.py changepassword <user>
```

Generate new secret

```
from django.core.management.utils import get_random_secret_key  
get_random_secret_key()
```

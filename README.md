#ONE DAY ONE STORY
=================
####Powered by python 3 and django 1.10

`Python3`,`Django`,`JavaScript`,`Blog`

## Usage:
create a virtualenv
```
$ virtualenv venv
```
Windows environment:
```
$ .\venv\Scripts\active
```
Linux environment:
```
$ source venv/bin/activate
```
Install the requirements
```
(venv)$ pip install -r requirements.txt

```
migrate database
```
(venv)$ python manage.py shell
>>>python manage.py makemigrations
>>>python manage.py migrate
....
>>>exit()
```
Create Account
```
(venv)$ python manage.py createsuperuser
```
Run
```
(venv)$ python manage.py runserver
```
Enter http://127.0.0.1:8000/blog/ to see homepage.

**Preview:**
`homepage`
![homepage](https://ws4.sinaimg.cn/large/647dc635jw1f8020dam4gj21h40p1jvs.jpg)

`article`
![article](https://ws4.sinaimg.cn/large/647dc635jw1f8020m73xrj21gu0ozaiw.jpg)

`tags`
![tags](https://ws1.sinaimg.cn/large/647dc635jw1f80215w76yj21hb0irq3t.jpg)


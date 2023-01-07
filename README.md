# [Django Berry PRO](https://appseed.us/product/berry-dashboard-pro/django/)

**Django** starter styled with **[Berry Dashboard PRO](https://appseed.us/product/berry-dashboard-pro/django/)**, a premium `Bootstrap 5` design from [CodedThemes](https://codedthemes.com/?ref=appseed)
The product is designed to deliver the best possible user experience with highly customizable feature-rich pages. 

> **NOTE**: This product `requires a License` in order to access the theme. During the purchase, a `GitHub Access TOKEN` is provided. 

- 🛒 [Django Berry PRO](https://appseed.us/product/berry-dashboard-pro/django/) - `Product page` (contains payment links)
- 👉 [Django Berry PRO](https://django-berry-pro.onrender.com) - `LIVE Demo`
- 🚀 [Support](https://appseed.us/support/) via `Email` & `Discord`

<br />

## Features: 

- ✅ `Up-to-date Dependencies`
- ✅ `Design`: [Django Theme Berry](https://github.com/app-generator/django-admin-berry-pro) - `PRO Version`
- ✅ `Sections` covered by the design:
  - ✅ **Admin section** (reserved for superusers)
  - ✅ **Authentication**: `Django.contrib.AUTH`, Registration
  - ✅ **All Pages** available in for ordinary users 
- ✅ `Docker`
- 🚀 `Deployment` 
  - `CI/CD` flow via `Render`

<br />

![Berry Bootstrap 5 PRO - Premium Template Django Template.](https://user-images.githubusercontent.com/51070104/210833058-be0b3e87-4f2b-4765-b84d-3795ba03c6a1.jpg)

<br />

## Manual Build 

> 👉 Download the code  

```bash
$ git clone https://github.com/app-generator/django-berry-dashboard-pro.git
$ cd django-berry-dashboard-pro
```

<br />

> Export `GITHUB_TOKEN` in the environment. The value is `provided by AppSeed during purchase`. 

This is required because the project has a private REPO dependency: `github.com/app-generator/priv-django-admin-berry-pro`

```bash
$ export GITHUB_TOKEN='TOKEN_HERE'  # for Linux, Mac
$ set GITHUB_TOKEN='TOKEN_HERE'     # Windows CMD
$ $env:GITHUB_TOKEN = 'TOKEN_HERE'  # Windows powerShell 
```

<br />

> 👉 Install modules via `VENV`.


```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> 👉 Edit the `.env` using the template `.env.sample`. 

```env

# True for development, False for production
DEBUG=True

```

<br />

> 👉 Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> 👉 Create the Superuser

```bash
$ python manage.py createsuperuser
```

<br />

> 👉 Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

## Screenshots

![Berry Pro - Premium full-stack starter crafted by AppSeed.](https://user-images.githubusercontent.com/51070104/210833261-af09bc29-0894-4d21-84ad-8e8853f8cbe1.jpg)

<br />

> **Django Berry PRO** - `Kanban Board`

![Berry Pro, Kanban Board - Premium full-stack starter crafted by AppSeed](https://user-images.githubusercontent.com/51070104/210833567-e26f67e1-53c8-430a-8add-e4d6c874266a.jpg)

<br />

> **Django Berry PRO** - `Kanban Board`

![Berry Pro, Widgets page - Premium full-stack starter crafted by AppSeed](https://user-images.githubusercontent.com/51070104/210833737-76643967-02f6-4342-9545-1ffaba68343f.jpg)

<br />

> **Django Berry PRO** - `eCommerce`

![Berry Pro, eCommerce page - Premium full-stack starter crafted by AppSeed](https://user-images.githubusercontent.com/51070104/210834456-344fbcb5-4a32-45ed-964e-b808dbc53356.jpg)

<br />

---
[Django Berry PRO](https://appseed.us/product/berry-dashboard-pro/django/) `Starter` - Minimal **Django** starter provided by **[AppSeed](https://appseed.us/)**

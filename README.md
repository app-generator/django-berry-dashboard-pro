# [Django Berry PRO](https://appseed.us/product/berry-dashboard-pro/django/)

**Django** starter styled with **[Berry Dashboard PRO](https://appseed.us/product/berry-dashboard-pro/django/)**, a premium `Bootstrap 5` design from [CodedThemes](https://codedthemes.com/?ref=appseed).
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

![Berry Bootstrap 5 PRO - Premium Template Django Template.](https://user-images.githubusercontent.com/51070104/215728155-9b9cfe26-96e8-49c3-8a08-131d96f4f2eb.png)

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

## Codebase structure

The project is coded using a simple and intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- core/                            
   |    |-- settings.py                  # Project Configuration  
   |    |-- urls.py                      # Project Routing
   |
   |-- home/
   |    |-- views.py                     # APP Views 
   |    |-- urls.py                      # APP Routing
   |    |-- models.py                    # APP Models 
   |    |-- tests.py                     # Tests  
   |    |-- templates/                   # Theme Customisation 
   |         |-- includes                # 
   |              |-- custom-footer.py   # Custom Footer      
   |     
   |-- requirements.txt                  # Project Dependencies
   |
   |-- env.sample                        # ENV Configuration (default values)
   |-- manage.py                         # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

## How to Customize 

When a template file is loaded in the controller, `Django` scans all template directories starting from the ones defined by the user, and returns the first match or an error in case the template is not found. 
The theme used to style this starter provides the following files: 

```bash
# This exists in ENV: LIB/admin_berry_pro
< UI_LIBRARY_ROOT >                      
   |
   |-- templates/                     # Root Templates Folder 
   |    |          
   |    |-- accounts/       
   |    |    |-- login-v1.html        # Sign IN Page
   |    |    |-- register-v1.html     # Sign UP Page
   |    |
   |    |-- includes/       
   |    |    |-- footer.html          # Footer component
   |    |    |-- sidebar.html         # Sidebar component
   |    |    |-- navigation.html      # Navigation Bar
   |    |    |-- scripts.html         # Scripts Component
   |    |
   |    |-- layouts/       
   |    |    |-- base.html            # Masterpage
   |    |    |-- base-fullscreen.html # Masterpage for Auth Pages
   |    |
   |    |-- pages/       
   |         |-- index.html           # INDEX page
   |         |-- dashboard/index.html # Main dashboard page
   |         |-- widgets/data.html    # Widgets page
   |         |-- *.html               # All other pages
   |    
   |-- ************************************************************************
```

When the project requires customization, we need to copy the original file that needs an update (from the virtual environment) and place it in the template folder using the same path. 

> For instance, if we want to **customize the footer.html** these are the steps:

- ✅ `Step 1`: create the `templates` DIRECTORY inside the `home` app
- ✅ `Step 2`: configure the project to use this new template directory
  - `core/settings.py` TEMPLATES section
- ✅ `Step 3`: copy the `footer.html` from the original location (inside your ENV) and save it to the `home/templates` DIR
  - Source PATH: `<YOUR_ENV>/LIB/admin_berry_pro/includes/footer.html`
  - Destination PATH: `<PROJECT_ROOT>home/templates/includes/footer.html`

> To speed up all these steps, the **codebase is already configured** (`Steps 1, and 2`) and a `custom footer` can be found at this location:

`home/templates/includes/custom-footer.html` 

By default, this file is unused because the `theme` expects `footer.html` (without the `custom-` prefix). 

In order to use it, simply rename it to `footer.html`. Like this, the default version shipped in the library is ignored by Django. 

In a similar way, all other files and components can be customized easily.

<br />

## Deploy on [Render](https://render.com/)

- Create a Blueprint instance
  - Go to https://dashboard.render.com/blueprints this link.
- Click `New Blueprint Instance` button.
- Connect your `repo` which you want to deploy.
- Fill the `Service Group Name` and click on `Update Existing Resources` button.
- After that your deployment will start automatically.

At this point, the product should be LIVE.

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

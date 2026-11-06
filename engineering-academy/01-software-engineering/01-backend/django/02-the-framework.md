# 02. The Framework

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Django gives you a structure, an object-relational mapper (ORM), an admin site and a way of doing common jobs. Django
REST Framework (DRF) adds the tools for building APIs. This stage covers how a request travels through Django 6 and
where your code fits. Back to the [roadmap](./README.md).

## Projects and apps

A Django project holds the settings and the top-level URLs. Apps hold the code for one area each, such as articles
or profiles.

**What to learn:**

- Creating a project and apps with `django-admin` and `manage.py`, and what each generated file does
- Splitting the RealWorld API into apps, such as users, profiles and articles
- Django's supported releases, and the long-term support release that client projects often use

**Resources:**

- [Writing your first Django app](https://docs.djangoproject.com/en/6.1/intro/tutorial01/), Django documentation
- [Download and supported versions](https://www.djangoproject.com/download/), Django website

**Level:** Practitioner · Core

## URLs and views

The URL configuration maps each path to a view: a function or class that takes a request and returns a response.

**What to learn:**

- `path()` patterns, path converters such as `<slug:slug>`, and including one app's URLs in the project's
- Function views and class-based views
- Pattern order: Django uses the first pattern that matches, so `articles/feed` must come before `articles/<slug>`

**Resources:**
[URL dispatcher](https://docs.djangoproject.com/en/6.1/topics/http/urls/) and
[writing views](https://docs.djangoproject.com/en/6.1/topics/http/views/), Django documentation

**Level:** Practitioner · Core

## Django REST Framework basics

DRF adds API views that parse JSON, check authentication and permissions, and return JSON responses.

**What to learn:**

- `APIView` and the `@api_view` decorator, `Request` and `Response`
- Setting DRF's defaults in the `REST_FRAMEWORK` setting
- How DRF chooses the response format, and why the browsable API is turned off in production

**Resources:** [DRF quickstart](https://www.django-rest-framework.org/tutorial/quickstart/), DRF documentation

**Level:** Practitioner · Core

## Middleware and the request cycle

A request passes through each middleware in order, then reaches the view. The response passes back through them in
reverse.

**What to learn:**

- The `MIDDLEWARE` setting, and what Django's default middleware does
- Writing middleware, such as one that adds a request ID to every response and log line
- Where DRF's authentication and permission checks run, compared with middleware

**Resources:** [Middleware](https://docs.djangoproject.com/en/6.1/topics/http/middleware/), Django documentation

**Level:** Practitioner · Core

## Settings and environments

Settings that change between your machine, staging and production come from environment variables, never from code.

**What to learn:**

- Reading settings from the environment, for example with `django-environ`, and failing at start-up when one is
  missing
- Why `SECRET_KEY` and passwords are never committed, and what goes in `.env.example`
- `DEBUG`, `ALLOWED_HOSTS`, and why debug mode must be off in production

**Resources:** [Settings](https://docs.djangoproject.com/en/6.1/topics/settings/), Django documentation

**Level:** Practitioner · Core

## The admin site

Django's admin site gives staff a ready-made interface to manage data. Many client projects use it for back-office
work.

**What to learn:**

- Registering models, and customising list pages and forms
- Protecting the admin site in production, with staff-only accounts and a non-default URL

**Resources:** [The Django admin site](https://docs.djangoproject.com/en/6.1/ref/contrib/admin/), Django documentation

**Level:** Practitioner · Optional

## Project: Start the API

**Brief:** Create a Django project with DRF for your RealWorld API, and add the first endpoint, `GET /api/tags`,
returning `{"tags": []}` for now.

**Size:** 1–2 days

**Verification**, checked by a reviewer:

- [ ] The project runs on a supported Django release with Python 3.12 or later, with API URLs under `/api` and no
  trailing slashes
- [ ] `GET /api/tags` returns status 200 and `{"tags": []}`
- [ ] With `DEBUG = False`, an unknown path under `/api` returns a JSON 404 through a `handler404` view, not an
  HTML page
- [ ] A middleware adds a request ID to every response header and log line, and has a test
- [ ] Settings come from environment variables, `.env` is not committed, and `.env.example` lists every setting
- [ ] Ruff and mypy run with no errors
- [ ] The README explains how to install, run and test the project

Previous: [01. Language Fundamentals](./01-language-fundamentals.md) · Next:
[03. HTTP and REST APIs](./03-http-and-rest-apis.md)

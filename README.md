# django-blog
Blog making base on Bootstrap and Django

### Project Purpose
- This project is made for me to understand and remind my [django-polls: tutorial](https://github.com/be-garam/django-poll) 
- So it will be just written by django(4.1) and bootstrap

### Refer
- I get help for writing this project by below sites
    - [django tutorial](https://docs.djangoproject.com/en/5.0/)
    - [djangogirls tutorial](https://jeffkit.gitbooks.io/django-girls-tutorial/content/ko/index.html)

### Updating BootStrap
- css file is in ./mysite/blog/static/css
    - downloaded from [`Complied CSS and JS`](https://getbootstrap.com/docs/5.3/getting-started/download/)
- for JS I've use CDN(Contents delivery network) instead of using `bootstrap.min.js`
    ``` HTML
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js" integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy" crossorigin="anonymous"></script>
    ```
    - It allow user to download file from the nearest server

### TO-DO
- [x] show post data - 🛸 2024.04.03 
- [x] add detail page - 🛸 2024.04.03 
- [x] add comment function - 🛸 2024.04.03 
- [ ] refactoring code
- [ ] apply bootstrap(make new branch)
- [ ] redesign by my self

### Thanks 💪
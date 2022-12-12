<div align="center">
  <img src="./website/static/website/logo.png">
  <h2>Free and Open Source Link Sharing</h2>
</div>

Linksharin' is currently (temporarily) live at [Python Anywhere](https://adamtherookie.pythonanywhere.com). Soon deploying to [linkshar.in](https://linkshar.in).

## What is linksharin'?
Linksharin' is a link sharer (surprise!). It gives you a unique link which you can then post on your social media profiles which then contains all the other links you would like your audience to see: personal websites, stores, content...

## Running locally
If you want to host an instance of Linkr on your own server, or test it locally, you can clone the git repo
`git clone https://github.com/adamtherookie/linksharin`.
Then you must set up the sqlite3 database: `python manage.py makemigrations && python manage.py migrate`.
After that you can run the server: `python manage.py runserver`

Requires sqlite3, python and the Django, Beautiful Soup, and markdown modules.

## Contributing
Any contributions fixing issues or adding new features are greatly appreciated. A good place to start would be adding colorschemes and effects.

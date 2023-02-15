<div align="center">
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
  <img src="./website/static/website/logo.png">
  <h2>Free and Open Source Link Sharing</h2>
  <a href="https://www.linkshar.in">Website</a> | <a href="https://discord.gg/g6ZSJdt8">Discord</a>
</div>

## What is linksharin'?
Linksharin' is a link sharer (surprise!). It gives you a unique link which you can then post on your social media profiles which then contains all the other links you would like your audience to see: personal websites, stores, content.... It also has a feature where you can generate custom private startpages with all your quicklinks and more!

## Running locally
If you want to host an instance of Linksharin' on your own server, or test it locally, you can clone the git repo

`git clone https://github.com/adamtherookie/linksharin`.

Then you must set up the sqlite3 database: `python manage.py makemigrations && python manage.py migrate`.

After that you can run the server: `python manage.py runserver`

Requires sqlite3, python and the Django, Beautiful Soup, and markdown modules.

## Contributing
Any contributions fixing issues or adding new features are greatly appreciated. A good place to start would to look at the goals below.

## Features + Goals
- [x] 100% FOSS
- [x] Custom CSS
- [ ] Drag and Drop mechanism for adding links
- [ ] Separate startpage CSS from page CSS
- [ ] Enable users to publish their custom themes (a theme marketplace or something of that sort)
- [ ] Detailed analytics with time-to-click, geographic distribution, referring sites, etc
- [ ] Portfolio generator

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://linktr.ee/rishav.raj"><img src="https://avatars.githubusercontent.com/u/97666287?v=4?s=100" width="100px;" alt="Rishav Raj"/><br /><sub><b>Rishav Raj</b></sub></a><br /><a href="#design-Rishav1707" title="Design">🎨</a> <a href="https://github.com/adamtherookie/linksharin/commits?author=Rishav1707" title="Code">💻</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
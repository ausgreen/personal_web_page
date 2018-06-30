# README.md

How to build/host this webpage

1. Make some useful changes to the website
2. Tell pelican you want to build the files
    
    $ make build
    
3. Push updates to git
4. Log in to webserver
5. Navigate to web root (directory named in nginx.conf)
6. Pull changes from git
7. Reload nginx
    $ sudo nginx -s reload


###### Useful links
building webpage with pelican
• https://www.fullstackpython.com/blog/generating-static-websites-pelican-jinja2-markdown.html

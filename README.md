# GibranGodoy

# Project 2

Web Programming with Python and JavaScript

## Flack - 2020

A Flask application where users enter giving a name, and then create channels or go into one of the already existing.

In the channels, the users can type and send messages which only exists into that channel and other users receive those messages and they can respond.

**Application.py**

Here is were the app resides. In this file, there are routes like `/`, `/allChannels`, `/channels/<channel>`, `/signin` and `/logout`.
- On the route `/` is render the file `index.html`.
- `/allChannels` loads `allChannels.html` file.
- `/channels/<channel>` is when I want to get the channel and it render `channel.html`.
- `/signin` is the route for the user sign in.
- `/logout` is called when the user log out from the session.

Also, there are `socketio` from flask, that communicate js files to the app.

**Static**

Here is store the Logo image. Also the custom CSS stylesheet and the javascript *ch.js*. The js file manage the data provided.
> The Logo I used is one that I made for one course.

**Templates**

Here is the interface the user can interact with in the browser. Here are the html files. I used boostrapCDN repository.

**Personal Touch**

I add in the `channel.html` file the option to upload a file from the computer to the page.

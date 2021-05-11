#!/usr/bin/env python3

from guizero import App, Text

app     = App ( title="Hello World" )
message = Text( app, text="Welcome to the app" )

app.display()
#!/usr/bin/env python3

# Imports --------------------
from guizero import App, Text, PushButton
from random  import choice

# Functions ------------------
def choose_name():
    # print("Button was pressed")
    first_names = [
        "Barbara"       ,
        "Woody"         ,
        "Tiberius"      ,
        "Smokey"        ,
        "Jennifer"      ,
        "Ruby"
        ]

    last_names = [
        "Spindleshanks" ,
        "Mysterioso"    ,
        "Dungeon"       ,
        "Cateye"        ,
        "Darkmeyer"     ,
        "Flamingobreath"
        ]

    spy_name = choice( first_names ) + " " + choice( last_names )
    print( spy_name )

# App ------------------------
app = App( "TOP SECRET" )

# Widgets --------------------
title  = Text      ( app, "Push the red button to find out your spy name" )
button = PushButton( app, choose_name, text="Tell me!" )

# Display --------------------
app.display()
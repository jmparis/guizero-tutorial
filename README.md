# guizero
simple examples with the [guizero](https://lawsie.github.io/guizero/) library.

----

### Installation

Open a shell, ensure [`Python 3`](https://www.python.org/) is already installed on your system, then install the [`guizero`](https://lawsie.github.io/guizero/) library with:

``` Shell
> pip install guizero
> git clone https://github.com/jmparis/guizero-tutorial.git
```

----

### 01\_simple\_window.py

In this first example, we just open a titled window with:

``` Python
#!/usr/bin/env python3

from guizero import App

app = App(title="Hello World")
app.display()
```

The first line is the [shebang](https://stackoverflow.com/questions/6908143/should-i-put-shebang-in-python-scripts-and-what-form-should-it-take) used to run the python program without typing the python3 command.

Every guizero application must end with a call to the [display()](https://lawsie.github.io/guizero/app/#app) function.

----

### 02\_simple\_text.py

``` Python
#!/usr/bin/env python3

from guizero import App, Text

app     = App ( title="Hello World" )
message = Text( app, text="Welcome to the app" )

app.display()
```

Simply create a `message` variable, and link this object to the previously created `app` object.

----

### 03\_wanted.py

In this example, we change the background color of the window, for a light yellow `#FBFBD0`.

We also change the font (`Impact`)and the size (`50`) of the text.

The `text` and `picture` objects are linked to the main `app`.

``` Python
#!/usr/bin/env python3

from guizero import App, Text, Picture

app = App( "Wanted!" )
app.bg = "#FBFBD0"

wanted_text = Text( app, "WANTED!" )
wanted_text.text_size = 50
wanted_text.font = "Impact"

cat = Picture( app, image="tabitha.png" )

app.display()
```

----

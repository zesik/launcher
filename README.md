# Launcher

Launcher is a simple zsh completion for choosing and running commands.
I created Launcher for listing servers based on partial name,
so that I can choose and connect to one of them.
Launcher is designed to be able to run arbitrary commands.

![](http://i.imgur.com/23veptt.gif)

## Prerequisites

Launcher is written in Python 3.

## Installation

1. Copy `launcher` directory and its content to `$HOME`.

2. Create a new directory `$HOME/.zsh-functions` and copy `_s` there.

3. Create a new directory `$HOME/bin` and create a soft link `s` to `$HOME/launcher/launcher.py`.
  Add executable permission to the link.

4. Modify `.zprofile` and add the following content.
    ```
    fpath=(
      $HOME/.zsh-functions
      $fpath
    )
    path=(
      $HOME/bin
      $path
    )
    ```

5. Copy `$HOME/launcher/launcher.conf.sample` to `$HOME/launcher/launcher.conf` and customize as you need.

## License

(The MIT License)

Copyright (c) 2015-2016 Yang Liu &lt;hi@zesik.com&gt;

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

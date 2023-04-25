# Python Installation Guide

## __Windows__
#### __Step 1: Download Python__ 
1) visit https://www.python.org/downloads/windows/
2) Find a stable Python 3 release. We reccomend Python 3.11.3.
3) Click the appropriate link for your system to download the executable file: Windows installer (64-bit) or Windows installer (32-bit). You should have a 64-bit system so you need the first one.
#### __Step 2: Install Python__
1) After the installer is downloaded, double-click the .exe file, for example python-3.11.4-amd64.exe, to run the Python installer.
2) Select the Install launcher for all users checkbox, which enables all users of the computer to access the Python launcher application.
3) Select the Add python.exe to PATH checkbox, which enables users to launch Python from the command line.
4) Click on the "Customize installation". Select all point. Click next. Select the first 4 points.
5) Click "Install". After installation you should see a "Setup successfull" message.
6) Verify the Python-installation:
   ```shell
   python --version
   ```
   should output:
   ```shell
   Python 3.11.3
   ```

## MacOS
The installation process on MacOSx is simple using homebrew.
If you haven't installed homebrew yet open a terminal and run 
```zsh
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```
Aftert this set Homebrew on the top of your path variable. Therefore open a terminal and run:
```zsh
nano ~/.profile
```
Insert the following line and save it:
```zsh
export PATH="/usr/local/opt/python/libexec/bin:$PATH"
```
Now install Python via brew, therefore type in:
```zsh
brew install python
```
Verify that you have a current Python Version by running:
```zsh
python --version
// Output should be:
Python 3.11.3
```

## __Linux__
The Linux install is very easy, if you are using a latest version of Ubuntu (but also anything else works) just run the following commands in a terminal:
```zsh
$ sudo apt-get install software-properties-common
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt-get update
$ sudo apt-get install python3.11.3
``` 
Verify that you have a current Python Version by running:
```zsh
python --version
// Output should be:
Python 3.11.3
```

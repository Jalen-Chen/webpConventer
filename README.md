# Introduction 
Converter could convert `webp` file under your selected directory into `png` file.
# Environment 
You need Python3 installed to run this script. To check your Python verision, run code below:
```shell 
python --version
```
if you are currently using Python2, error will occur since it is not compatible with this code.

## Install pip
pip is a tool to manage python packages, you could use command below to check wheither you have pip installed in your machine.
```shell
pip3 --version 
```
if you want to install pip, you can do so by enter command below:
```shell
 $ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
 $ sudo python get-pip.py 
 ```
 ## Using pip install OpenCV 
 Please check your pip version before installation:
 ```shell
 pip -V
 ```
 To upgrade your pip version, you can enter command as below:
 ```shell 
 pip install --upgrade pip
 ```
 Then install Opencv. Opencv is supported by Windows, macOS, most Linux, GNU.
 ```
 pip install opencv-python
 ```
 # Usage 
 1. Run converter script via Terminal or CMD
 ```shell 
 python converter.py
 ```
 2. Enter your folder directory 
 > You can use absolute directory or relative directory
 > your directory may contains Chinese charactors, but this is highly deprecated.
 > The script will check whether your directory is vaild.
 3. Press Enter, Then use `Y` or `N` to select whether to backup.
 > If you wish to backup before converting, the script will create a `.bk` file each time when across a `.webp` file. 
 > Eg: ![image](https://user-images.githubusercontent.com/57817787/123756011-140b4b80-d8ef-11eb-9960-bda8e502266b.png)
Then the script will then run and convert every `.webp` file to `.png`.
>Note that this script will justify a file type using `byte Steam Detection`, since some file's extension is named as `.png` but is actually coded with `webp` format and have `webp` file's hex signature. 

# Maintainer 
Jay Chen - `jalen_chen@outlook.com`
Please feel free to drop me an e-mail is any error occur when using. 

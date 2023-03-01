# Simple Defanging Python Script Documentation

The purpose of this tool is to quickly and easily defang malicious URLs and IP addresses from a simple command line interface. This is a process that is repeated quite often in a security operations center when writing reports for customers and needing to provide documentation of the malicous links and IP addresses visited by their network. However it is critical in this documentation to defang the IP addresses / URLs in order to prevent them from accidently being clicked/visted.

## Setup
---
#### Install the latest version of Python and install pyperclip

Visit https://www.python.org/downloads/ and install the latest version of Python. As of writing, this is Python 3.11.2 
![download-installer](https://github.com/jaredbergenthal/Simple-Defang-Tool/images/download-installer.png)

Once the executable is downloaded, run the installer selecting the express “Install Now” option.


![install-python](https://github.com/jaredbergenthal/Simple-Defang-Tool/images/install-python.png)

After the setup is complete, you’ll need to ensure that pyperclip, a module that handles plain text copy and paste functions, is installed. On a windows machine, input windows + r to open the “run” prompt, and input “cmd” and hit okay.


![run-cmd](https://github.com/jaredbergenthal/Simple-Defang-Tool/images/run-cmd.png)


This will open your windows command prompt. From here, input 
`pip install pyperclip`
and hit enter to install the pyperclip.


![install-pyperclip](https://github.com/jaredbergenthal/Simple-Defang-Tool/images/install-pyperclip.png)


Install the defanging tool

Go to https://github.com/jaredbergenthal/Simple-Defang-Tool, and from here select the green “Code” button, select download zip, download, and extract the tool. After the file is extracted, simply double click the file entitled “main.py” to run it.

![main-prompt](https://github.com/jaredbergenthal/Simple-Defang-Tool/images/main-prompt.png)
From here, input the URL/ip you wish to defang. If you would like to include another URL/ip, simply click enter once then type the next one. When finished, click enter twice to run the program.

```sh
<ip> [Enter]
```
(Additional as needed:
```sh
<ip> [Enter]
```
)
```sh
[Enter]
```




![defanged-example](https://github.com/jaredbergenthal/Simple-Defang-Tool/images/defanged-example.png)

The new, defanged url is now copied to your clipboard and ready for you to analyze. 

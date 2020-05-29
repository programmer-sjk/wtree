# wtree
tree command for Windows

## purpose
* Windows tree command only support /F or /A option.
* I Wanna use tree command with -d(only directory) or -L(level of sub items) options 

## Requirement
* Python 3.x
* pip is installed

## tech stack
* python

# Getting Started
1. git clone https://github.com/programmer-sjk/wtree.git
2. cd wtree
3. I give two option to execute init.sh
* If you wanna execute <b>python script</b>, you can command <b>bash init.sh</b> <br>
you will command like this. ex) python wtree.py [path] [option]
 
* If you wanna execute <b>binary exe</b>, you can command <b>bash init.sh -b</b> <br>
If you will add directory path to windows environment path, you can use wtree everywhere.<br><br>

After you command <b> bash init.sh -b </b>, you can see dist directory like below<br>
<img width="500px" src="https://user-images.githubusercontent.com/52809501/83218688-68527200-a1a9-11ea-90ba-d4677edc7fe0.png"><br>

wtree.exe will be placed dist\wtree\ path.<br>
<img width="500px" src="https://user-images.githubusercontent.com/52809501/83218782-a64f9600-a1a9-11ea-80f2-8f9884936246.png"><br>

You need to add wtree.exe path to Windows environment path.<br>
<img width="500px" src="https://user-images.githubusercontent.com/52809501/83218817-bb2c2980-a1a9-11ea-9f28-9af4ab81d5cf.png"><br>

Finally, you can use wtree every place.

# example
* cmder example 
<img width="500px" src="https://user-images.githubusercontent.com/52809501/83120742-64bcdd80-a10c-11ea-9cbb-7ea3376516e8.PNG">

* cmd example
<img width="500px" src="https://user-images.githubusercontent.com/52809501/83120748-68506480-a10c-11ea-95db-a176647abb81.PNG">


<h1 align="center">Everything You Need to know about Python3</h1>
<p align="center">
  <img src="https://th.bing.com/th/id/OIP.vfW3CHC6irCGHk3DEPjlnwHaEK?w=282&h=180&c=7&r=0&o=5&pid=1.7" alt='Python Logo' />
</p>

<p align="left">
This repo is all about educational purpose. It contains everything that you need to know about python3 with some docs and code which is constantly updating with either 
  some concepts or projects. There is no pre-requisite for refering this repo, any one can start learning this as concepts are documented from scratch.
</p>

## To Get a Copy
- You can directly download the zip file by using the following link :
<a href="https://github.com/venkateshtantravahi/Python-0-to-hero-/archive/refs/heads/main.zip" target="_blank">Python.zip</a>
- You can directly clone the repo using https or ssh or github cli thorugh thier prompts 
``` 
command: git clone https://github.com/venkateshtantravahi/Python-0-to-hero-.git
```

# To Work with Code 
### Setup of python 

- For windows gui's guided installation file will be available on following websites as python can be installed directly as a package or you can install with anaconda distribution

```
Python: https://www.python.org/downloads/
Anaconda: https://docs.anaconda.com/anaconda/install/windows/
```

- For Ubuntu distributions you need to install packages from the terminal as no guided gui will be available there

```
Python: sudo apt install python
Anaconda : https://docs.anaconda.com/anaconda/install/linux/
```

### Creating Environments
Once the installations is done you can create seperate envs to work standalone with this repo, which means that's like a private space where you install packages specific 
to this repo which doesn't effect the global packages, you can create env's in wo different ways 
- Creating env using pipenv
  ```
  pip--install: pip install virtualenv
  create env : virtualenv <name>
  ```
- Activation and deactivation
 ```
 acivation(Wndows) : mypthon\Scripts\activate
 activation(Ubuntu) : Source mypython/bin/activate
 deactivation : deactivate
 ```
- Creating using conda
```
creation : conda create -n <env_name> <python_version>
activation : conda activate <env_name>
deactivation : conda deactivate
```

### Running scripts
- For windows open the shell at desired folder 
   - for python file 
      ```C:\devspace> hello.py```
      
- For Ubuntu open the terminal 
  - for python file \
    ```xyz-PC:-$ python filename.py```
    
 ### Packages Installation
 - For some modules to work with in the repo there might be usage of external modules which may lead to error when you directly run these files prior installation 
 - to install these modules you can directly refer to pip[python package installer] or conda repo based on the installer on your machine
- If python is installed as standalone package in ubuntu or windows installer then pip should already be part of it, if not first install pip using following command:

``` python get-pip.py```
- or upgrade the current version using 

``` python -m pip install --upgrade pip```
- If you have installed anaconda you would already been configured with conda base env so you can refer the below repo's as requirement

<a href="https://pypi.org/project/pip/" target="_blank">Pip Repo</a>
<a href="https://anaconda.org/anaconda/conda" target = "_blank">Conda Repo</a>

The only thing you have to do is go to that repo and search for package you wana install and it will give you the reuired information about it.

### Liked Content 

Please hit a star 🌟 and follow me on github for more like this. 


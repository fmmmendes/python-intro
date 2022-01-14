# Intro to Python

## Requirements

* VS Code
* Python 3
* Windows

## Topics

### Virtual Environments

Why create a virtual environemnt? Allow to create an isolate environemnt to work 

Create a virtual env
```cmd
virtualenv venv-intro
```

Activate the virtual env
```cmd
 .\venv-intro\Scripts\activate
```

Intall pandas package 

```cmd
pip install pandas
```
Intall several packages using requirements.txt

```cmd
pip install -r requirements.txt
```

Deactivate the virtual env

```cmd
deactivate
```

### Jupyter and Pandas

Jupyter is...


Start jupyter service or execute from VS Code

```cmd
jupyter lab
```

Save a notebook output as html file

```cmd
jupyter nbconvert --execute --to html notebook.ipynb
```


## References

https://dev.to/idrisrampurawala/setting-up-python-workspace-in-visual-studio-code-vscode-149p   
https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html  
https://coincodex.com/crypto/bitcoin/historical-data/  
https://towardsdatascience.com/python-environment-101-1d68bda3094d  
https://flask.palletsprojects.com/en/2.0.x/  
https://docs.pytest.org/en/6.2.x/  
https://towardsdatascience.com/write-clean-python-code-using-pipes-1239a0f3abf5  
https://towardsdatascience.com/timestamp-parsing-with-python-ec185536bcfc  
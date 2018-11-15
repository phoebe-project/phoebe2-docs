### [phoebe](phoebe.md).logger (function)


```py

def logger(*args, **kwargs)

```



Return a basic logger via a log file and/or terminal.

Example 1: log only to the console, accepting levels "INFO" and above
```py
logger = logger()
```

Example 2: log only to the console, accepting levels "DEBUG" and above
```py
logger(clevel='DEBUG')
```

Example 3: log only to a file, accepting levels "DEBUG" and above
```py
logger(clevel=None,filename='mylog.log')
```

Example 4: log only to a file, accepting levels "INFO" and above
```py
logger(clevel=None,flevel='INFO',filename='mylog.log')
```

Example 5: log to the terminal (INFO and above) and file (DEBUG and above)
```py
logger(filename='mylog.log')
```

Arguments
----------
* `clevel` (string, optional): level to be logged to the console.
    One of: "ERROR", "WARNING", "INFO", "DEBUG".
* `flevel` (string, optional): level to be logged to the file.
    Must also provide `filename`.  One of: "ERROR", "WARNING", "INFO", "DEBUG".
* `filename` (string, optional): path to the file to log at the `flevel` level.
* `style` (string, optional, default='default'): style to use for logging.
    One of: "default", "minimal", "grandpa".


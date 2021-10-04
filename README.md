## Code Checking with Pylint

Use [pylint][pylint] to find coding and style problems in `person.py`.  
```
pylint person.py
```
Fix the problems and rerun pylint until you get a score of 10.

Push the corrected code to Github.

### Installing Pylint

pylint may already be installed on your computer. 
If not, install it using:
```
pip install pylint
``` 
On some systems, "pip" may be named "pip3".

[pylint]: https://pylint.org


### Use Flake8 and Flake8-docstrings to check `contacts.py`

Flake8 is another code checker that detects coding style and logic errors.
Flake8-docstrings is an extension that uses Pydocstyle to check docstring
comments.

Flake8 with Flake8-docstrings to check your `contacts.py` from the midterm.  Copy `contacts.py` to this repository before editing it.  Correct the file until there are no messages from flake8.

```
pip install flake8 flake8-docstrings
```

As usual, you can also use `pip install --upgrade package ...` to upgrade existing packages.



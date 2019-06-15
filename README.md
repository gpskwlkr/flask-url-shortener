# Flask based super-duper-simple URL shortener

# For usage 

```python
python main.py
```

And that's it, everything is already set up for you !

# How it works

1. You enter the URL that you want to shorten
2. Script searches for that URL in the database, and if it's there already just returns you an ID that belongs to that URL.
3. If it's not in the database, script generates a random 5 character URL for you and saves it to database.
4. Once you enter the shortened URL script looks for your ID in the database and redirects you to the corresponding URL.
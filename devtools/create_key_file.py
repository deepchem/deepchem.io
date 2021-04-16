import os

print(len(os.environ["AWS_ACCESS_KEY_ID"]))
print(len(os.environ["AWS_SECRET_ACCESS_KEY"]))

with open('keys.crt', 'w') as f:
  f.write('''[default]
access_key = {AWS_ACCESS_KEY_ID}
secret_key = {AWS_SECRET_ACCESS_KEY}
guess_mime_type = True
no_mime_magic = True
'''.format(**os.environ))
  f.flush()

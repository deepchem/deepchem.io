import os
import pip
import tempfile
import subprocess
import delegator

BUCKET_NAME = 'deepchem.io'
if pip.__version__ >= "10.0.0":
    from pip._internal.utils.misc import get_installed_distributions
else:
    from pip import get_installed_distributions

if not any(d.project_name == 's3cmd'
           for d in get_installed_distributions()):
  raise ImportError('The s3cmd package is required. try $ pip install s3cmd')

template = "s3cmd -M -H --config {config} sync website/ s3://{bucket}/"
cmd = template.format(config='keys.crt', bucket=BUCKET_NAME)
c = delegator.run(cmd)
c.block()
print(c.out)

template = "s3cmd --recursive modify --add-header='content-type':'text/css' --include '.css' --config {config} s3://{bucket}/"
cmd = template.format(config='keys.crt', bucket=BUCKET_NAME)
print(cmd)
c = delegator.run(cmd)
c.block()
print(c.out)

template = "s3cmd --recursive modify --add-header='content-type':'application/javascript' --include '.js' --config {config} s3://{bucket}/"
cmd = template.format(config='keys.crt', bucket=BUCKET_NAME)
c = delegator.run(cmd)
print(c.out)

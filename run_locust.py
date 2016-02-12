#!/anaconda/bin/python
import sys
import os
import os.path

# Map OS environment variables to locust options
vars_to_check = {'LOCUST_PW': '--locust-pw=', 'LOCUST_NUM_REQUESTS': '--num-request=',
                 'LOCUST_HOST': '--host='} # , 'LOCUST_CLASS': ''}
vars_to_pass = []
print "checking environment variables"
for k, v in vars_to_check.items():
    if os.environ.has_key(k):
        print k + " is set"
        vars_to_pass.append(vars_to_check[k] + os.environ[k])
    else:
        print k + " env variable is NOT set"

workdir = os.getenv('LOCUST_WORKDIR')
if workdir == None:
    workdir = os.environ['PWD']

os.chdir(workdir)
sys.path.append(workdir)
target_script = workdir + "/locust/main.py"
locust_file =  workdir + "/locustfile.py"
sys.argv = [target_script,
            '--locustfile=' + locust_file,
            '--no-web',
            '--clients=1',
            '--hatch-rate=1',]
# include and OS variables
sys.argv.extend(vars_to_pass)
execfile(target_script)

import subprocess
import sys

result = subprocess.Popen(['git', 'ls-files'], stdout=subprocess.PIPE)
files = result.stdout.read().decode('utf-8').strip().split('\n')

print(files)

scp = subprocess.Popen(['gcloud compute scp ' + ' '.join(files) + ' ishan@blog:~/mysite/ --recurse'], shell=True)
scp.wait()

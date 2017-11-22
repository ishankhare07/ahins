import subprocess
import sys

result = subprocess.Popen(['git', 'archive', 'master', '-o', 'deployment.tar.gz'], stdout=subprocess.PIPE)

scp = subprocess.Popen(['gcloud compute scp ' + 'deployment.tar.gz' + ' ishan@blog:~/ahins_deploy'], shell=True)
scp.wait()

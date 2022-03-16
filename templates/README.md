**COMPONENTS**
1. Runner
I installed a runner on my server to listen to the github actions happening in this repository. Because the two are connected 
my updated page automatically got written and executed on the server. 
2. SSH
An SSH-key is a more secure way of authentication, using both a private and public key. Since both aren't stored in the same
place, the chance of someone being able to steal a password is much smaller. I used a SSH-key to log into the server.
3. sh-files
This assignment is the first time I used .sh-files. They are basically a pre-written list of bash-command you can execute at any time.

**PROBLEMS**
1. Service-file. The main problem I had was with my .service file, which didn't function as it should, even though I copied it from the assignment. Luckily I found that the 'sudo systemd-analyze verify yourname.service' command could check the service-file, after which I was able to find and solve the problem.
2. Bash. During the entire front and backend course I always used powershell. Therefore using bash now was new and unfamiliar to me, since I had to use ls instead of dir and so on.
3. Github actions. At first, I had problemns with my github action not resolving. It took me some time to work out that I had to start gunicorn in a different way.

**OTHER NOTES**
Honestly, I wish the deployment-part of the course would be larger. I think it would be great If we could build an app here with a front and backend, authentication, databases and so in. It would really connect the dots.
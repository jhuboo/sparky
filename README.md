# SpotMicroAI runtime source code

This repo contains a basic os that let you move SpotMicroAI with a remote controller and a RaspberryPi

If you are looking for simulation, please check the simulation repositories here: https://gitlab.com/custom\_robots/spotmicroai

## Start

Refer to the instructions here to install the software: https://gitlab.com/custom\_robots/spotmicroai/basic

# Steps to setup the Repo:
1) git clone https://github.com/jhuboo/sparky spotmicroai
2) cd spotmicroai/
3) find . -type f -iname "\*.sh" -exec chmod +x {} \\;
4) cd utilities/
5) ./activate.sh
6) cd integration\_test/
7) ./test\_motion.sh

# SpotMicroAI Community

Visit the project website for more
* Website: https://spotmicroai.readthedocs.io/en/latest/
* Slack: https://spotmicroai-inviter.herokuapp.com/
* Forum http://spotmicroai.org/
* Repositories: https://gitlab.com/custom_robots/spotmicro
* Some videos: https://www.youtube.com/watch?v=kHBcVlqpvZ8&list=PLp5v7U2tXHs3BYfe93GZwuUZLGsisapic&


###### TODO
On boot, if someone press a button before press start, show the error properly in the log and screen of spotmicro

## Other peoples builds!

* User Mike R from the slack community, build the more advanced software: https://github.com/mike4192/spotMicro -> https://www.youtube.com/watch?v=S-uzWG9Z-5E. He has the moves!

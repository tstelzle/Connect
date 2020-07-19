# Connect

## About
The game is for two players. Alternating every player puts a block on the field.
A player wins by reaching one of these three conditions:
1. 5 blocks in a row (vertical, horizontal and diagonal)
2. A square of four blocks
3. Having blocks in all *adjacent* fields of the same color

## Running

### Docker
There is a docker container available, which can be build with the Makefile.
As this is a front end application, you need to enable 'xhost +'. If you do not like the security concerns, please use the local installation guide below.
1. make build-image
2. make container
3. make run

These commands should start you the game, if you have docker installed and are able to use it without sudo permissions.

### Local
Alternatively you can install python3 and the needed modules 'tk-tools' and 'Pillow' locally on your machine.
Then you are able to run 'python connect.py' in the directory, which should also start the game.
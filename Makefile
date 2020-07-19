# MAKEFILE https://github.com/tstelzle/Connect
# AUTHORS: Tarek Stelzle

IMAGE-NAME := python-env-connect
CONTAINER-NAME := connect
MOUNT-DIR := $(PWD)
RUN := docker exec -it -w /usr/src $(CONTAINER-NAME) python connect.py

default:
	@echo "Possible Targets:"

build-image:
	docker build -t $(IMAGE-NAME) .

container:
	docker run -d -t --rm -v $(MOUNT-DIR):/usr/src -e DISPLAY=${DISPLAY} -v /tmp/.X11-unix:/tmp/.X11-unix --device /dev/dri/ --name $(CONTAINER-NAME) $(IMAGE-NAME)

run:
	$(RUN)

run-master:
	git stash --include-untracked $(IGNORE-OUTPUT)
	git checkout master $(IGNORE-OUTPUT)
	$(RUN)
	git checkout $(BRANCH) $(IGNORE-OUTPUT)
	git stash pop $(IGNORE-OUTPUT)
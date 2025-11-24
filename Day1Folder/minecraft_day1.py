# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
################# Function Section #############################
def Teleport():
    agent.teleport_to_player()
# move commands

def move_forward(steps):
    agent.move(FORWARD, steps)

def move_back(steps):
    agent.move(BACK, steps)

def move_up(steps):
    agent.move(UP, steps)

def move_down(steps):
    agent.move(DOWN, steps)

#turn commands
def turn_left():
    agent.turn(LEFT)

def turn_right():
    agent.turn(RIGHT)

#obby1
def obby1():
    agent.move(FORWARD, 4)
    agent.turn(LEFT)
    agent.move(FORWARD, 4)
    agent.turn(RIGHT)
    agent.move(FORWARD, 3)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 3)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)

################## On Chat Commands Section #####################
player.on_chat("come", Teleport)
player.on_chat("mf", move_forward)
player.on_chat("mb", move_back)
player.on_chat("mu", move_up)
player.on_chat("md", move_down)
player.on_chat("tl", turn_left)
player.on_chat("tr", turn_right)
player.on_chat("obby1", obby1)
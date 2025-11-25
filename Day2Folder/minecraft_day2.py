# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
def choptree(height):
    for i in range(height):
        agent.destroy(FORWARD)
        agent.move(UP,1)
    agent.move(DOWN, height)
    agent.collect_all()

def choptree_whole(height):
    for i in range(height):
        agent.destroy(FORWARD)
        agent.move(UP,1)
    agent.move(DOWN, height)
    agent.move(FORWARD, 1)
    agent.collect_all()

def mineore(blocks):
    for i in range(blocks):
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.destroy(DOWN,)
        agent.destroy(UP)
        agent.collect_all()
        agent.move(FORWARD, 1)

def go_down():
            agent.destroy(DOWN)
            agent.move(DOWN, 1)
            agent.turn_left()
            agent.turn_left()

player.on_chat("chop", choptree)
player.on_chat("choptree_whole", choptree_whole)
player.on_chat("mineore", mineore)
player.on_chat("go_down", go_down)
# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
def build_wall(stone):
    for i in range(stone):
        agent.place(FORWARD)
        agent.move(BACK, 1)

def build_walls(stones):
    for i in range(stones):
        agent.place(FORWARD)
        agent.move(UP, 1)

player.on_chat("build_wall_down", build_wall)
player.on_chat("build_wall_up", build_walls)
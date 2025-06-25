# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER

def on_chat():
    agent.teleport_to_player()
player.on_chat("come", on_chat)


def on_chat2():
    agent.turn(LEFT)
player.on_chat("tl", on_chat2)


def on_chat3():
    agent.turn(RIGHT)
player.on_chat("tr", on_chat3)


def on_chat4(steps):
    agent.move(FORWARD, steps)
player.on_chat("FW", on_chat4)


def on_chat5(steps):
    agent.move(BACK, steps)
player.on_chat("B", on_chat5)


def on_chat6(steps):
    agent.move(UP, steps)
player.on_chat("U", on_chat6)


def on_chat7(steps):
    agent.move(DOWN, steps)
player.on_chat("D", on_chat7)



def on_chat8(obby1):
    agent.move(FORWARD, 4)
    agent.move(LEFT, 4)
    agent.move(FORWARD, 3)
player.on_chat("obby1", on_chat8)


def on_chat9(obby2):
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
player.on_chat("obby2", on_chat9)


def on_chat10(chop):
    agent.destroy(FORWARD)
    agent.collect_all()
    agent.move(UP, 1)
player.on_chat("chop", on_chat10)

def on_chat11(height):
    for i in range(height):
        agent.destroy(FORWARD)
        agent.move(UP, 1)
    agent.move(DOWN, height)
    agent.collect_all()

player.on_chat("chp", on_chat11)


def on_chat12(lenght):
    for i in range(lenght):
        agent.destroy(FORWARD)
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.destroy(DOWN)
        agent.collect_all()
        agent.move(FORWARD, lenght)
player.on_chat("mine", on_chat12)









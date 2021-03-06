import game

Flappy = game.Game()

def run_controlled():
    for j in range(20):
        Flappy.reset()
        done = False
        i = 0
        while not done:
            if i % 13 == 0:
                rew, done = Flappy.step(1)
            else:
                rew, done = Flappy.step(0)
            i += 1
        print("rewared: ", rew)

def run_user():
    Flappy.reset()
    done = False
    i = 0
    while not done:
        rew, done = Flappy.step(0)

run_controlled()
# run_user()

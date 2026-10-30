# SPACE SHOOTER

A 2D endless space-survival game built with Python and Pygame. Pilot a spaceship, select incoming objects, type their words to fire lasers, and survive for as long as possible. The longer you stay alive, the faster and more frequently enemies arrive.

## Features

* Spaceship movement using arrow keys.
* Two-frame spaceship animation.
* Incoming space objects with words displayed above them.
* Automatic target selection for nearby enemies.
* Press `TAB` to switch between targets.
* Typing the next correct letter fires a laser at the selected target.
* Enemy health is based on the length of its word.
* Each laser hit removes one health point.
* Score and destroyed-enemy counter.
* Survival timer that counts upwards.
* Increasing difficulty as survival time increases.
* Enemy spawn frequency and movement speed increase over time.
* Collision with an enemy ends the run.
* Game Over screen with final score, enemies destroyed, survival time, and high score.
* Local high-score saving.
* Replay support.

## Controls

| Key                     | Action                                 |
| ----------------------- | -------------------------------------- |
| `↑` `↓` `←` `→`         | Move the spaceship                     |
| `TAB`                   | Switch to the next nearby target       |
| Letter keys             | Type the selected enemy's word to fire |
| `R` / `ENTER` / `SPACE` | Replay after Game Over                 |
| `ESC`                   | Quit the game                          |

You can also click the **PLAY AGAIN** button on the Game Over screen.



## Gameplay

1. Move your spaceship around the screen.
2. Incoming space objects appear with words above them.
3. Select a nearby target automatically or press `TAB` to switch targets.
4. Type the displayed word one letter at a time.
5. Each correct letter fires a laser towards your selected target.
6. Destroy enemies to earn points.
7. Avoid collisions and survive for as long as possible.
8. Try to beat your previous high score!

## Notes

* High scores are stored locally. There is currently no online leaderboard.
* The game uses an endless survival mode rather than a fixed-level progression system.
* Required sprite and font assets must be present in their respective folders before running the game.

---

**Built with Python and Pygame.** 🚀

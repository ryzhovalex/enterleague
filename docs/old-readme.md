### Glossary

*TODO: write terminology*

### Background

This is "learn" project, so main goal of this is to research different technologies during development, discover advantages and disadvantages of various decisions, obtain experience of serious-like software development separated by stages and sprints. Finally, to try to build proper architecture, development process and operations which are welcome in modern software building.

Despite of said above, contributing and participating are welcomed, because working in team or just single collaborating is highly appreciated.

### Product requirements in the form of user stories

- As a visitor, i want to see massive living simulation, so i can watch after my favourite club/player and enjoy it/his results.
- As a visitor, i want to see good overview of the simulation, so i can stay tuned and don't miss simulation actions, like matches and important actions.
- As a visitor, i want to see wide statistics of every aspect of the simulation, so i can be informed why certain event happened or why it possible can happen.
- As a visitor, i want to see logical and realistic simulation, so i can enjoy it and don't be disfocused because of strange and non-realistic moments.
- As an user, i want to have an access to the player of my choice, so i can manipulate matches, where this player participates, configure his parameters.
- As an user, i want to make decisions for my player, so i can accept or decline transfers to another clubs and perform other actions related to player's career.
- As an user, i want to have convenient panel with actions and overview of my player, so i can have control over him without issues and watch after him.
- As an admin, i want to have multi-functional panel for controlling over all actions of the simulation, so i can recover simulation state if something went wrong or fix unfair and not-realistic matches results.
- As an admin/user/visitor, i want to have my own account with corresponding rights.

### Technical requirements

- Core app should be builded on Flask framework.
- Main languages - Python, JavaScript. Other languages are welcomed but only for future extra features.
- Architecture pattern - MVC (Model, View, Controller) with realization on Flask framework.
- No virtual environments - only requirements and manual files (in future it can be changed, but now it's should be considered "as it").
- PostgreSQL as a main database.
- Database models implementation - flask-sqlalchemy models.

### Out of Scope
- Compatibility to every browser in the world (really, only Chrome, only hardcore)
- Highly rpm oriented (not important for this project)

### Future Goals

- mooooreee functions and statistics of clubs, players, ... etc.
- other sport types (tennis, motosport)

### Assumptions

Resources:
- virtual server with access for creating sub-servers (nginx, app, db)
- developer time =)

Conditions:
- delicious coffee

---

## Design

### Data Models

#### Player

Basic element of the system. Participates in matches, chained to the certain Club. Has parameters and skills which affecting to match result. Parameters and skills change through time and depend on Player's statistic and actions.

#### Club

Contains Players. Participates in matches with another clubs in terms of Championship. Has budget and rating. According to rating can participate in different Championships.

#### Championship

Contains Clubs-participants. May be play-off or table type. Winner and prizers will get a trophie according to Championship.

#### Season

Contains Championships, which will be played during this Season. In real time may be only one Season. Seasons changes each other and are significant moments of the Simulation where parameters of all instances of lower levels are being changed.

#### Simulation

Contains sequental set of Seasons. It is the main element of the program. Simulation defines global parameters of everything, which happens across Seasons.

---
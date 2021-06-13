EnterLeague
===

EnterLeague project has designed with goal of building living championship simulation with access from third-view user to watch after all actions within it.
"Living championship simulation" - this is complex set of championships, clubs and players and matches between them. All this are united in season, which define simulation progression. Main goal for this stage is to build this simulation based on football game.
Special feature is possibility to have an access to own player and control his parameters with functions of changing. All matches, where controlled player has a partition also can be configured and controlled.


## Roadmap

Working process separated into Sprints (1 week), each with certain end-goal and purpose.

*Keys:*     
🔶 - main purpose of a sprint   
🏁 - sprint has finished     
⭐ - current sprint      
✅ - task done   
⚠️ - task has done, but some planned functions have been discarded   
🏃️ - work on task is in progress   
⏲️ - task has been moved to next sprint because of deadline breaking      
❌ - task has been rejected because of changed conditions   


### 🏁 Sprint 1 - Base (2021.05.31 - 2021.06.06)

&nbsp;&nbsp;&nbsp;&nbsp;*🔶 Organize basic platform for future development*

- ✅ Define instances and their dependencies
- ✅ Create structure (build UML schema with core instances)
- ✅ Organize work environment (repository, directories, tools, etc.)
- ✅ Build basic Flask app with database connection and skeleton instances

### ⭐ Sprint 2 - Generation (2021.06.07 - 2021.06.13)

&nbsp;&nbsp;&nbsp;&nbsp;*🔶 Make first steps in data collection and generation*

- ✅ Build models of general instances
- ✅ Collect raw data for further migrations
- 🏃 Implement general generation engine (players, clubs, etc. generators)

---

## References

1. Flask App template with migrations extension: [helloflask](https://github.com/ryzhovalex/helloflask)
1. Overview structure reference: [stackoverflow blog](https://stackoverflow.blog/2020/04/06/a-practical-guide-to-writing-technical-specs/)
1. How to start with big project (RU): [youtube video](https://www.youtube.com/watch?v=F3STHxfABf4)

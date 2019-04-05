# What is Continuous Integration? [DRAFT]

> It's all about **TESTING**, and applied in the scenario of **DAILY MULTIPLE MERGES TO MASTER BRANCH**.

[Refer to: Continuous Integration - What's the point? - Continuous Integration P1 - Fun Fun Function](https://www.youtube.com/watch?v=ymPOI4gWQFY)

`CI` sounds like a buzz word, a magic word, which in my opinion it's just to confuse the beginners.
**In an essense, a `CI` is just a `server program` that helps you to run your test scripts automatically when you do `git push`.**

What does "integration" mean?
It simple means `git merge` from a feature-branch to a master-branch.

What does "continuous" mean?
It's just saying after you developed a new thing to the application, the code can be `git merge`ed **WITHOUT WAITING** for the `Ops guy` to manually check stuff before he merge the code. It means to say, without the "blocker", without the waiting, the development process then become "continuous".



## Common development process

Start from the beginning, as the team's `branching strategy`, what we do is to **develop all feature or fix** at a `feature branch` out of the master branch.
When the development is finished, we run the unit tests and functional tests at the feature branch by a simple command like `pytest /path/to/project/tests` to make sure all tests are passed.
Then seems it's ready to be merged to master branch.
What does it mean by `merge to master`? It means that the code is ready to RELEASE to the public, to show to the customers, which is critical and can be risky. We want it to be as less risky as possible.

Before diving deeper, I'd like to show the common development process on a new feature:
- Create a feature branch from the master: `git checkout -b new-feature-01`
- Develop on this feature without worrying, and commit anything you like: `git commit`
- Run unit tests on this branch: `pytest /path/to/project/unit-test`
- Run functional tests on this branch: `pytest /path/to/project/functional-test`
- Push the feature branch to remove: `git push origin new-feature-01`
- The remote server is triggered to run the tests on the feature branch, which is called `doing a CI`
- The remote server shows you a webpage that if the `CI` tests are passed or not.
- If the CI passed, means that you're ready to be merged to the master.
- Or you want to deploy the feature branch to a `Test Environment` computer, which has some test dataset in the database or the production database (read-only).
- When everything runs well with the feature branch, you've gained enough confidence, means it's ready to merge to the master
- Create a Pull Request & merge the feature branch to the master branch, meaning the master branch is updated with your new code
- Run tests on the master branch with `real production server` on "real data"
- If it passed, the master branch is ready to RELEASE to the public!
- Then **deploy** the master branch to the `production server`
- DONE! Now every user can see the new feature


## How the CI is triggered

In the pro-language, we call it a `hook` when something will be automatically triggered.
At Github, it's called a `webhook` on a repo which will trigger some scripts or programs when you do some change to the repo, like `git push`.

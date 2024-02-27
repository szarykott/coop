# Cooperative task

This repository contains files that form a skeleton of an application. Currently the application does nothing. Your task is to make this application do something, but so that code is merged to this repository in GitHub.

To do so you'll need to learn the process of forking, branching and merge (pull) requests. It would be best if you did at least two pull requests, in order to practice.

Me as an owner of this repository will comment on your code and request improvements as a reviewer in a normal workplace would do, so that you can get the feeling of this.

# Task 1 - Parse command line args

In file `cliargs.py` there is a blueprint of a method to parse cli arguments. Let's imagine we want our application to cook dishes.

```bash
app.py COMMAND OPTION1 OPTION2 ...

COMMAND:
bake - bakes using owen
cook - cooks using pots

OPTIONS (all optional)
--speed - accepts values in set : {'not-in-a-hurry', 'late-for-work', 'late-for-plane'}
--ingredients - accepts a list of ingredients in a format 'ingredientA ingredientB' (space delimited list)
--quantity - accepts values in set : {'a-little', 'a-lot', 'for-an-army'}
```

Application needs to be able to parse correct input and inform user about their mistakes.

# Task 2 - Cook

Given the input, application needs to write (or paint or draw if you feel adventurous) how the process of preparation looks like, taking into account bake/cook and other parameters.

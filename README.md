# learning_systems

Module generate decision tree

#To run 
```python

python3 main.py

```

Tree for zoo.data.txt

----- column 0
      |
----- when is outlook then class
----- when is overcast then Play
----- sunny is divided by 
---------- column 2
            |
---------- when is normalna then Play
---------- when is wysoka then Don'tPlay
----- rain is divided by 
--------------- column 3
                  |
--------------- when is false then Play
--------------- when is true then Don'tPlay

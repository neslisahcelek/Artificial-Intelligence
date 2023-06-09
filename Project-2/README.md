# CSE358/CSE5058 Artificial Intelligence Project 2

## Project Definition

In this project, you are required to color the map of the South America continent using a backtracking search
algorithm. When coloring the map, two neighboring countries should not have the same color. Furthermore, you
can use at most 4 different colors (blue, green, red, and yellow).

Table 1 presents the border neighborhoods of the countries in South America. You need to embed this information
into your application in a way of your own choice (e.g., reading a CSV file, setting as program variables etc.).

*Table 1. Countries on the continent of South America and their border neighbors*
![image](https://github.com/neslisahcelek/Artificial-Intelligence/assets/70594682/8d15c50e-84cc-4c30-8bc8-c167b6e265ad)

## To-Do

You are going to develop a Python application, which employs backtracking to color the countries in South America.
Once the algorithm finds a possible solution, you should plot a choropleth map by calling “plot_choropleth“, which
takes a dictionary as an argument. This dictionary should contain country names as keys and colors as values. 

# Graph Cheat Sheet

#### Import Libraries

The following code snippet imports the library used for graphing and sets up
the "style" of the graph. There are many different styles you can use that you
can find by searching online.

```python
import matplotlib.pyplot as plots
plots.style.use("fivethirtyeight")
```

#### Create a figure

The following code snippet creates a 6x6 window that is then filled with your
desired graph.

```python
plots.figure(figsize=(6, 6))
```

#### Fill Bar Graph with Data

The following code snippet creates a bar graph with two bars. The first bar is
given the name "bar1" with a height of `10`. The second bar is given the name
"bar2" with a height of `15`.

```python
plots.bar(x=["bar1", "bar2"], height=[10, 15])
```

#### Fill Scatter Plot with Data

The following code snippet creates two purple dots on a scatter plot. The first
dot is at `(80, 10)` and the second dot is at `(81, 9.5)`.

```python
plots.scatter([80, 81], [10, 9.5], color="purple", label="Purple Data")
```

#### Fill Line Graph with Data

The following code snippet creates a graph with a red line that goes from `(0, 10)`
to `(1, 11)` to `(2, 14)`.

```python
plots.plot([0, 1, 2], [10, 11, 14], color="red", label="thing")
```

#### Set Graph Options

- Add a title: `plots.title("Title of Graph")`
- Add a ylabel: `plots.ylabel("Y Axis Text")`
- Add a xlabel: `plots.xlabel("X Axis Text")`
- Add a legend: `plots.legend()`
- Add y "ticks": `plots.yticks([0, 100])`
- Turn on/off grid on graph: `plots.grid(True)` | `plots.grid(False)`

#### Full Example Scatter Plot

The following code snippet creates a scatter plot with two sets of colored points:
one set of points is red and the other is orange. The points for red scatter plot
are at `(2.5, 10)`, `(3, 9.5)`, `(2, 9)`, and `(1, 10)`.

```python
#!/usr/bin/python3
import matplotlib.pyplot as plots

plots.style.use("fivethirtyeight")


if __name__ == "__main__":
    plots.figure(figsize=(6, 6))

    plots.scatter([2.5, 3, 2, 1], [10, 9.5, 9, 10], color="red", label="In")
    plots.scatter([14, 4.5, 3.5, 1], [1, 0, 0, 0.5], color="orange", label="Out")

    plots.title("Made up data")
    plots.ylabel("This is the y axis")
    plots.xlabel("This is the x axis")
    plots.legend()
    plots.grid(True)
    plots.yticks([0, 5, 10, 15])

    plots.show()
```

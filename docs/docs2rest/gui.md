## GUI definition

`docs2rest` offers a basic support for defining GUIs in Markdown.
The idea is that data should be shown in two different modes:

- as a grid of cells, where each cell is a single value
- in an editor that should allow user to create and modifiy existing elements.

The GUI definition section must follow some rules, we could say that the definition is *position based*.

the first line for a new GUI definition is the *header* with this syntax:

```markdown
  ### GUI: `(gui name)` [something I don't remember] [size of column 1, size of column 2, ...]
```

So the first part `### GUI: ` specify the beginning of a new GUI definition to the parser. The name of the GUI must be enclosed in backticks ``` ` ```.

If the editor will have more than one column, you can specify the size in unit of 12th (as in Bootstrap or Material design) so that every line is created by 12 elements.

For example, if you want a column be as twice as big than the other, specify a ratio of 8:4 (the first column is 8, the second is 4, so the sum is 12 and first column is twice as big as the second).
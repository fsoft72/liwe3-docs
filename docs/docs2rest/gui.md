# GUI definition

`docs2rest` offers a basic support for defining GUIs in Markdown.
The idea is that data should be shown in two different modes:

- as a grid of cells, where each cell is a single value
- in an editor that should allow user to create and modifiy existing elements.

The GUI definition section must follow some rules, we could say that the definition is *position based*.

## Defining the *header*

the first line for a new GUI definition is the *header* with this syntax:

```markdown
  ### GUI: `(gui name)` [collection name[/filter]] [size of column 1, size of column 2, ...]
```

So the first part `### GUI: ` specify the beginning of a new GUI definition to the parser. The name of the GUI must be enclosed in backticks ``` ` ```.

Then inside the square brackets you have to insert the **collection name** and optionally the **filter**, separated by the slash `/`.

If the editor will have more than one column to show the inputs and widgets, you can specify the size in unit of 12th (as in Bootstrap or Material design) so that every line is created by 12 elements.

For example, if you want a column be as twice as big than the other, specify a ratio of 8:4 (the first column is 8, the second is 4, so the sum is 12 and first column is twice as big as the second).

Here there is a complete example of a GUI definition for a `Post` field editor, with two columns:

```markdown
  ### GUI: `Post` [posts/posts] [8,4]
```

## Defining the *fields*

After that, you can specify the fields that will be shown in the grid, and the fields that will be shown in the editor.
Every field must be defined with the following syntax:

```markdown
[position in grid][colum][size of field] field_name field type 'Field Title'
```

for example:

```markdown
[1][1][12] title		str,req				'Title'
```

this is the `title` field, which will be shown in the grid, and in the editor as a text field. It is required.
It will be at the first position in the grid, and in the first column in the editor, and will be 12 units wide.

If a field should appear in the editor, but not in the grid, you can specify the column position to be empty:

```markdown
[ ][1][12] sub_title		str				'Sub Title'
```

In a similar way, if a field should appear in the grid, but not in the editor, you can specify the editor position to be empty:

```markdown
[1][ ][12] title		str,req				'Title'
```
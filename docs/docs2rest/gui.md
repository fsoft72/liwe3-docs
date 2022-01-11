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

this is the `title` field, which will be shown in the grid, and in the editor as a text field. It is a required field that means that the user must fill it in the editor before being able to save the item.
In grid, it will be at the first position, and in the first column in the editor, and will be 12 units wide.

If a field should appear in the editor, but not in the grid, you can specify the column position to be empty:

```markdown
[ ][1][12] sub_title		str				'Sub Title'
```

In a similar way, if a field should appear in the grid, but not in the editor, you can specify the editor position to be empty:

```markdown
[1][ ][12] title		str,req				'Title'
```

## The accordion container

In the *editor* mode, sometimes it is useful to group elements together both for logical reasons and to make the editor more compact.

The **GUI** definition can contain an **accordion container**, which will be shown in the editor as a group of elements (if the translator plugin supports this feature).
At the moment, only the *nextjs* plugin support the feature, but you will have the information in the AST tree anyway.

To start an accordion container, you can use the following syntax:
```markdown
[ ][2][12] acc accordion 'Accordion Title'
```

Since the first square brackets are empty, the element will not be shown in the grid, but will be shown in the editor as a group of elements.
In the example, the second square brackets specify the column position in the editor (2) and the size of the group (12 / all the available row space in the editor).

With this line, you have defined an *accordion start* and everything that follows will be shown in the editor as a group of elements if you put the '*' character as the value of the second brackets.

Let's see a complete example:

```markdown
[ ][2][12] acc			accordion		'Price'
[ ][*][ 6] price_net		num			'Price net'
[ ][*][ 6] price_vat		num			'Price vat'
[ ][*][ 4] discount		num			'Discount'
[ ][2][12] email		email			'Client email'
```

In this example, we're defining an accordion with the *Price* title. Inside the accordion, we have the *price_net*, *price_vat*, *discount* fields, while the *email* field will be shown in the editor outside the accordion.
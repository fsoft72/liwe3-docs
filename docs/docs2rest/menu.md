# Menu creation

`docs2rest` offers an option to create the markdown code for the menu of a module.

Usually, you should provide a menu that references the collection endopoints and structures of the module, but when the module becose bigger and bigger, you may start to forget to create the new menu entries.

So, `docs2rest` offers an option to create the menu automatically. It is a small utilty inside the `docs2rest` package that will create the menu for you.

## Usage

The usage is quite simple, let's see an example:

```bash
$ docs2rest.py -t null -o /null -m ~/dev/snippets/docs/post.md
```

**PLEASE NOTE**: the `docs2rest` menu creation, always dumps the output on console. The two options `-t` and `-o` are not used, but you have to provide them anyway, since they are mandatory by the `docs2rest` software.
#!/usr/bin/env python3

"""
This script takes a ts file and scan it for /** ... */ comments, and converts the JSDoc comments to markdown.
It also reads the line below the comment and uses it as the title of the markdown section.
"""

import argparse


class DocNode:
    def __init__(self, modname):
        self.title = ""
        self.subtitle = ""
        self.comment = []
        self.params = []
        self.returns = ""

        self.modname = modname

    def add_line(self, line):
        # removes the leading "*"
        line = line.strip()
        if line.startswith("*"):
            line = line[1:].strip()

        if "@param" in line:
            self.add_param(line)
        elif "@returns" in line:
            self.returns = line.replace("@returns", "").strip()
        else:
            self._add_comment(line)

    def _add_comment(self, line):
        self.comment.append(
            line.replace("/**", "").replace("*/", "").replace("*", "").strip()
        )

    def add_param(self, param):
        # Param can be:
        # @param {string} name - description
        # or @param name - description

        param = param.replace("@param", "").strip()

        if "{" in param:
            _type = param.split("{")[1].split("}")[0]
            param = param.replace(f"{{{_type}}}", "").strip()
            pname = param.split("-")[0].strip()
            desc = param.split("-")[1].strip()
        else:
            _type = "any"
            if "-" in param:
                pname = param.split("-")[0].strip()
                desc = param.split("-")[1].strip()
            else:
                pname = param.split(" ")[0].strip()
                try:
                    desc = param.split(" ")[1].strip()
                except:
                    desc = ""

        self.params.append([pname, _type, desc])

    def add_title(self, line):
        line = line.replace("export const", "", 1)
        self.title = line.replace("=>", "").replace("{", "").strip()

        self.main_title = self.title.split("=")[0].strip()

    def slugify(self, txt):
        txt = txt.lower().strip()

        # removes all after "("
        if "(" in txt:
            txt = txt.split("(")[0]

        replaces = [
            ["export const", ""],
            [" ", "-"],
            ["=", ""],
            [".", ""],
            ["_", "-"],
        ]

        for r in replaces:
            txt = txt.replace(r[0], r[1])

        # Removes all the '-' at the beginning and end of the string
        while txt.startswith("-"):
            txt = txt[1:]
        while txt.endswith("-"):
            txt = txt[:-1]

        return txt

    def dump(self):
        print('<a id="%s-%s"></a>' % (self.modname, self.slugify(self.main_title)))
        print("## `%s`" % self.main_title)
        print("\n")
        print("```ts")
        print(self.title)
        print("```")
        print("\n")
        print("\n".join(self.comment))
        print("\n")
        if self.params:
            print("**Parameters**")
            print("")
            print("| Name | Type | Description |")
            print("| ---- | ---- | ----------- |")
            for p in self.params:
                print(f"| `{p[0]}` | {p[1]} | {p[2]} |")

        print("\n\n")
        print("**Returns**: `%s`" % self.returns)
        print("\n-----------------\n")


parser = argparse.ArgumentParser(description="Convert JSDoc comments to markdown")
parser.add_argument("file", type=str, help="The file to convert")
args = parser.parse_args()

modname = args.file.split("/")[-1]
modname = modname.split(".")[0]

with open(args.file, "r") as f:
    lines = f.readlines()

in_comment = False
needs_title = False
completed = False

node = DocNode(modname)

for line in lines:
    if in_comment:
        if line.strip() == "*/":
            in_comment = False
            needs_title = True
        else:
            node.add_line(line)

    elif needs_title:
        node.add_title(line)
        needs_title = False
        completed = True

    elif line.strip() == "/**":
        in_comment = True
        needs_title = True
        completed = False

    elif completed:
        node.dump()
        node = DocNode(modname)
        completed = False

    else:
        pass

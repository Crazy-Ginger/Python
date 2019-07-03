#!/usr/bin/env python3
def insert_in_middle(target, substitute):
    target_len, sub_len = len(target), len(substitute)
    if sub_len > target_len:
        return substitute
    diff = target_len - sub_len
    start = diff // 2
    end = target_len - (start if diff % 2 == 0 else start + 1)
    return target[:start] + substitute + target[end:]


class BinaryTree(list):
    def __init__(self, val, children=[]):
        self.val = val
        if len(children) == 2:
            if all(isinstance(child, BinaryTree) for child in children):
                super().__init__(children)
            else:
                raise TypeError("Non-BinaryTree type in children")
        else:
            super().__init__()

    @property
    def is_leaf(self):
        return len(self) == 0

    @property
    def val_str(self):
        return str(self.val) if "\n" not in str(self.val) else str(type(self.val))

    @property
    def get_strings(self):
        # Base case
        if self.is_leaf:
            return [str(self.val)]

        # Get multiline strings of children
        strings = [child.get_strings for child in self] + [self.val_str]

        # Get the maximum line length of each child's string and use that as spacing
        spacings = [
            " " * (max([len(part) for part in string]) // 2)
            for string in strings
        ]
        # Get the (divide-corrected) length of this node's value string
        val_len = len(strings[-1]) + 2
        spacings.append(" " * (val_len if val_len % 2 != 0 else val_len + 1))

        total_spacing = len("".join(spacings))

        # If our child strings have different numbers of lines,
        # add more appropriately-sized lines to the smaller one
        if len(strings[0]) != len(strings[1]):
            smaller = int(not len(strings[0]) < len(strings[1]))
            strings[smaller].extend([
                " " * spacings[smaller] for i in range(
                    len(strings[int(not smaller)]) - len(strings[smaller])
                )
            ])

        # Generate the header
        header = [
            (
                spacings[0]
                + "+" + ("-" * total_spacing) + "+"
                + spacings[1]
            ),
            spacings[0] + "v" + (" " * total_spacing) + "v" + spacings[1],
        ]
        # Insert our value halfway along
        header[0] = insert_in_middle(header[0], strings[-1])

        # Generate the content (ie formatted lines w/padding)
        content = [
            line[0] + spacings[-1] + line[1]
            for line in zip(strings[0], strings[1])
        ]
        return header + content

    def __repr__(self):
        if self.is_leaf:
            return self.val_str
        return "\n".join(self.get_strings)


print(BinaryTree(
    1, (
        BinaryTree(
            "Hey", (
                BinaryTree(1),
                BinaryTree(2),
            )),
        BinaryTree(
            "Hi, I'm Laura!", (
                BinaryTree("Hey"),
                BinaryTree("Yo"),
            )
        )
    )
))

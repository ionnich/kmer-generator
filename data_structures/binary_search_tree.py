# %%
class node:
    # constructor
    def __init__(self) -> None:
        self.left = None
        self.right = None
        self.value = None
        self.counter = 0

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s : %s' % (self.counter, self.value)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()  # type: ignore
            s = '%s : %s' % (self.counter, self.value)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s : %s' % (self.counter, self.value)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s : %s' % (self.counter, self.value)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


# %%
def add_node(root, value):

    # if root is null, this node must be the root
    if root is None:
        root = node()
        if value is not None:
            root.value = value
            root.counter += 1
        return root

    if root.value is None and value is not None:
        root.value = value
        root.counter += 1
        return root

    # if value is less than root.value go to left nodes
    if value < root.value:
        root.left = add_node(root.left, value)
        # if the left node does not exist
        # if root.left is None:
        #     root.left = node()
        #     root.left.value = value
        #     if value is not None:
        #         root.left.counter += 1
        # else:
        #     root.left = add_node(root.left, value)

    if value > root.value:
        root.right = add_node(root.right, value)
        # if root.right is None:
        #     root.right = node()
        #     root.right.value = value
        #     if value is not None:
        #         root.right.counter += 1
        # else:
        #     root.right = add_node(root.right, value)

    if value == root.value and value is not None:
        root.counter += 1

    return root

# %%


def search_value(root, value):

    if value == root.value:
        return root.counter

    if root is None:
        return 0

    if value < root.value:
        return search_value(root.left, value)

    if value > root.value:
        return search_value(root.right, value)

    # if we are at the bottom of the tree and the value has still not been found, the value must not be within the tree

# %%


def destroy_tree(root):

    # if a left node exists
    if root.left is not None:
        # recursively destroy the left node
        destroy_tree(root.left)

    # if a right node exists
    if root.right is not None:
        # recursively destroy the right node
        destroy_tree(root.right)

    # delete the root node
    del root

# %%


def create_tree():
    return add_node(None, None)

# %%


def show_tree(root):

    if (root is None):
        return

    lines, *_ = root._display_aux()
    for line in lines:
        print(line)

# %%

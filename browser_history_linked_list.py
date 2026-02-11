"""
Browser History using a Doubly Linked List.

Each visited page is a node:
 prev pointer (back)
 next pointer (forward)

Rules:
visit(url): clears forward history and adds a new node
back(steps): move to prev nodes
forward(steps): move to next nodes
"""


class Node:
    def __init__(self, url: str):
        self.url = url
        self.prev = None
        self.next = None


class BrowserHistory:
    def __init__(self, homepage: str):
        self.current = Node(homepage)

    def visit(self, url: str):
        new_node = Node(url)

        # remove forward history
        self.current.next = None

        # link current <-> new_node
        new_node.prev = self.current
        self.current.next = new_node

        # move current to the new page
        self.current = new_node

    def back(self, steps: int):
        while steps > 0 and self.current.prev is not None:
            self.current = self.current.prev
            steps -= 1
        return self.current.url

    def forward(self, steps: int):
        while steps > 0 and self.current.next is not None:
            self.current = self.current.next
            steps -= 1
        return self.current.url

    def get_current_page(self):
        return self.current.url


if __name__ == "__main__":
    bh = BrowserHistory("google.com")
    bh.visit("youtube.com")
    bh.visit("github.com")
    print("Current:", bh.get_current_page())  # github.com

    print("Back 1:", bh.back(1))              # youtube.com
    print("Back 1:", bh.back(1))              # google.com
    print("Forward 1:", bh.forward(1))        # youtube.com

    bh.visit("stackoverflow.com")
    print("Current:", bh.get_current_page())  # stackoverflow.com
    print("Forward 2:", bh.forward(2))        # still stackoverflow.com

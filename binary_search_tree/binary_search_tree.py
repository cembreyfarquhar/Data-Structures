class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value == self.value:
      return "Value found"
    if value < self.value:
      if self.left is None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    elif value > self.value:
      if self.right is None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)
    else:
      self.value = value

  def contains(self, target):
    if self.value == target:
      return True
    else:
      if target < self.value:
        self.left = BinarySearchTree(self.left)
        self.left.contains(target)
      else:
        self.right = BinarySearchTree(self.right)
        self.right.contains(target)

  def get_max(self):
    if self.right is None:
      return self.value
    else:
      self.right = BinarySearchTree(self.right)
      self.right.get_max()

  def for_each(self, cb):
    pass
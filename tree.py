import turtle
import time

start_time = time.time()

MINIMUM_BRANCH_LENGTH = 5

def build_tree(t, branch_length, shorten_by, angle):
  if branch_length > MINIMUM_BRANCH_LENGTH:
    t.forward(branch_length)
    new_length = branch_length - shorten_by
    t.left(angle)
    build_tree(t, new_length, shorten_by, angle)
    t.right(angle * 2)
    build_tree(t, new_length, shorten_by, angle)
    t.left(angle)
    t.backward(branch_length)

tree = turtle.Turtle()
tree.hideturtle()
tree.speed(0)
tree.setheading(90)
tree.color('green')
build_tree(tree, 50, 5, 40)
print("--- %s seconds ---" % (time.time() - start_time))  
turtle.mainloop()
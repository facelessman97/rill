from rill import *
from rill.fn import synced


@component
@inport('IN1')
@inport('IN2')
@outport('OUT')
def Add(IN1, IN2, OUT):
    for x, y in synced(IN1, IN2).iter_contents():
        OUT.send(x + y)

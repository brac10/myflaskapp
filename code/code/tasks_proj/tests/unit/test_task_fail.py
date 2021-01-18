"""Use the Task type to show test failures."""
from tasks import Task

def test_task_equality():
    """Different tasks should not be equal."""
    t1 = Task('Login in', 'bob')
    t2 = Task('Enter IP address', 'Zack')
    assert t1 == t2


def test_dict_equality():
    """Different tasks compared as dicts should not be equal."""
    t1_dict = Task('Set Network Mask', 'April')._asdict()
    t2_dict = Task('Set Gateway Address', 'Bob')._asdict()
    assert t1_dict == t2_dict

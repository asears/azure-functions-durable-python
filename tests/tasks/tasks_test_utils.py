def assert_tasks_equal(task1, task2):
    assert task1.is_completed == task2.is_completed
    assert task1.is_faulted == task2.is_faulted
    assert task1.result == task2.result
    assert task1.timestamp == task2.timestamp
    assert task1.id == task2.id
    assert task1.action == task2.action

def assert_taskset_equal(taskset1, taskset2):
    assert taskset1.is_completed == taskset2.is_completed
    assert taskset1.is_faulted == taskset2.is_faulted
    assert taskset1.result == taskset2.result
    assert taskset1.exception == taskset2.exception
    assert taskset1.actions == taskset2.actions

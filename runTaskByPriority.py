import random
import pprint
from string import ascii_letters


def generateTaskList(itemNum=6,
                     commandTextCount=4,
                     priorityRange=(0, 10)):
    """ Generate a list of mock tasks for the purpose of testing.

    :param itemNum: number of tasks that are going to be generated
    :type itemNum: int

    :param commandTextCount: number of the characters the random command
    :type commandTextCount: int

    :param priorityRange: the range of the priority
    :type priorityRange: tuple of integers

    :return: a list of dictionaries containing 2 keys 'priority' and 'command'
            Example:
            [
            {'priority': 7, 'command': 'UviP_0'},
            {'priority': 8, 'command': 'swTE_1'},
            {'priority': 1, 'command': 'AXUe_2'},
            {'priority': 6, 'command': 'rukr_3'},
            {'priority': 5, 'command': 'bxdJ_4'},
            {'priority': 5, 'command': 'onKy_5'},
            ]

    :rtype: list of dictionary
    """
    taskList = list()
    for index in range(itemNum):
        randomString = ''.join(random.choice(ascii_letters) for count in range(commandTextCount))
        command = '_'.join([randomString, str(index)])
        taskList.append(
            {'command': command,
             'priority':random.randint(priorityRange[0], priorityRange[1])
            }
        )

    return taskList



def sortTaskByPriority(taskList, largeToSmall=True):
    """ Sort a list of tasks by their priority numbers.

    :param taskList: list of tasks
                     Each task is a dictionary containing 2 keys 'priority' and 'command'
    :type taskList: list of dictionaries

    :param largeToSmall: if sorting the list by larger priority numbers to smaller priority numbers.
    :type largeToSmall: bool

    :return: a list of sorted tasks
    :rtype: list
    """
    return sorted(taskList, key=lambda task: task.get('priority'), reverse=largeToSmall)


def runTasks(tasks):
    """ A mock of running the command of the task.

    :param tasks: list of tasks
                  Each task is a dictionary containing 2 keys 'priority' and 'command'
    :type tasks: list

    :return:
    """
    for task in tasks:
        print('run command: {}, task priority: {}'.format(task.get('command'),
                                                          task.get('priority')))



def execute(priorityLagerToSmall=True):
    """

    :return:
    """
    taskList = generateTaskList(itemNum=10, commandTextCount=4)
    sortedTaskList = sortTaskByPriority(taskList, largeToSmall=priorityLagerToSmall)

    print('Tasks generated:')
    pprint.pprint(taskList)
    print('\n[Run tasks]', '-' * 20)

    runTasks(sortedTaskList)


if __name__ == '__main__':
    execute()


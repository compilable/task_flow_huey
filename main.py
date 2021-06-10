from config import huey, Record
# import any tasks / decorated functions
from task import checkInternalStatus, checkExternalStatus

'''
Manually run the task for testing.
'''

if __name__ == '__main__':

    # single record
    result = checkInternalStatus(Record('US001', 1, 'NEW'))
    newPerson = result.get(blocking=True)
    print('checkInternalStatus = %s' % str(newPerson.count))

    # multiple records
    '''pipe = (checkInternalStatus.s(Record('US001',1,'NEW'))
        .then(checkExternalStatus)
        .then(checkInternalStatus))
    result_group = huey.enqueue(pipe)
    print(result_group.get(blocking=True))'''

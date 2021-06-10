from config import huey, Record
from huey import crontab
from time import sleep


def checkForRecords():
    # sleep(50)

    # load from the DB.
    recordList = [Record('US001', 1, 'NEW'), Record(
        'US002', 5, 'EXISTING'), Record('US003', 10, 'NEW')]

    print('checkForRecords record count = %s' % str(len(recordList)))

    recordResponse = []

    for record in recordList:
        print('record = %s' % str(record.userId))

        pipe = (checkInternalStatus.s(record)
                .then(checkExternalStatus))
        recordResponse.append(huey.enqueue(pipe))

    return recordResponse


@huey.task()
def checkInternalStatus(record):
    record.status = 'INTERNAL'
    record.count = record.count+1
    print('checkInternalStatus called id = %s , status = %s , count = %d' %
          (str(record.userId), str(record.status), record.count))
    return record


@huey.task()
def checkExternalStatus(record):
    record.status = 'EXTERNAL'
    record.count = record.count+1
    print('checkExternalStatus called id = %s , status = %s , count = %d' %
          (str(record.userId), str(record.status), record.count))
    return record


@huey.periodic_task(crontab(minute='*/1'))
def scheduler():
    print('Runs every minute')
    # looks for db and find records
    # call that task to start the workflow

    checkForRecords()
    # print(result.get(blocking=True))

    return True


@huey.on_shutdown()
def on_shutdown(task, task_value, exc):
    print('exiting, clear the redis cache')

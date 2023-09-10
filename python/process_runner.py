import logging
import multiprocessing
import signal
import time

logger = logging.getLogger(__name__)

# Configure the logging module
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def task1():
    time.sleep(10)

def task2():
    raise Exception("Failure from task 2")

def task3():
    pass

def run_task(task, stop_event):
    task_func = task["function"]
    task_name = task["name"]
    run_period = task["run_period"]
    pid = multiprocessing.current_process().pid
    # name = multiprocessing.current_process().name

    logger = logging.getLogger(task_name)

    def signal_handler(signum, frame):
        logger.debug(f"Received SIGINT in process {pid}")

    signal.signal(signal.SIGINT, signal_handler)

    while not stop_event.is_set():
        start_time = time.time()
        logger.debug("Task {} executed at {}".format(pid, time.ctime()))
        try:
            task_func()
        except Exception as e:
            logger.error(f"Task {pid} failed with error: {e}")

        run_time = time.time() - start_time

        if run_time < run_period:
            logger.debug("Task {} took {} seconds".format(pid, run_time))
            remaining_seconds = run_period - run_time
        else:
            logger.warning(f"Task {pid} took longer than run_period (run time: {run_time:0.2f}, run period: {run_period} seconds)")
            # use mod to get to next period
            remaining_seconds = run_period - (run_time % run_period)
            logger.warning(f"Task {pid} will run again in {remaining_seconds:0.2f} seconds")

        # if we are waiting and stop event is set, break the loop
        while remaining_seconds > 0:
            if stop_event.is_set():
                break

            if remaining_seconds > 1:
                time.sleep(1)
                remaining_seconds -= 1
            else:
                time.sleep(remaining_seconds)

    logger.info(f"Task {pid} is gracefully stopped")

def main():
    tasks = [
        {"name": "Task 1", "function": task1, "run_period": 5},
        {"name": "Task 2", "function": task2, "run_period": 7},
        {"name": "Task 3", "function": task3, "run_period": 10},
    ]

    processes = []
    stop_event = multiprocessing.Event()

    for task in tasks:
        logger.info("Starting task {} with run_period {} seconds".format(task["name"], task["run_period"]))
        process = multiprocessing.Process(target=run_task, args=(task, stop_event))
        processes.append(process)
        process.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("Ctrl+C pressed ...")
        logger.info("Stopping gracefully all processes ...")
        stop_event.set()
        logger.info("Waiting for all processes to stop ...")

        try:
            for process in processes:
                process.join()
        except KeyboardInterrupt:
            logger.info("Ctrl+C pressed again ...")
            logger.info("Terminating all processes ...")
            for process in processes:
                process.terminate()
                process.join()

        logger.info("All processes are stopped")


if __name__ == "__main__":
    main()

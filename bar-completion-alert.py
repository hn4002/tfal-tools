#!/opt/homebrew/bin/python3 

# Run this script to get an alert at the completion of every 1 minute bar
# Usage:  python3 bar-completion-alert.py

import logging
import os
import sys
import time
from datetime import datetime
from logging.handlers import RotatingFileHandler

import schedule

#=====================================================================================
# Logging Setup
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
# File logger
fileHandler = RotatingFileHandler(f"/usr/local/log/bar-completion-alert.log", maxBytes=10000000, backupCount=10)
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)
# Console logger
consoleHandler = logging.StreamHandler(sys.stdout)
consoleHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)

#=====================================================================================
# SETTINGS
#=====================================================================================
alert_1_minute = True
alert_2_minutes = True
alert_5_minutes = True
alert_15_minutes = True



#=====================================================================================
def run_alert_bar_completion():
    # Get current minute
    current_minute = datetime.now().minute
    print(f"current_minute = {current_minute}")
    if current_minute % 15 == 0:
        if alert_15_minutes:
            os.system("say '15 minutes'")
            logger.info(f"Bar completion alert - 15 minutes - ALERT TRUE - (current_minute = {current_minute}, alert_15_minutes = {alert_15_minutes})")
        else:
            logger.info(f"Bar completion alert - 15 minutes - ALERT FALSE (current_minute = {current_minute}, alert_15_minutes = {alert_15_minutes})")
    elif current_minute % 5 == 0:
        if alert_5_minutes:
            os.system("say '5 minutes'")
            logger.info(f"Bar completion alert - 5 minutes - ALERT TRUE (current_minute = {current_minute}, alert_5_minutes = {alert_5_minutes})")
        else:
            logger.info(f"Bar completion alert - 5 minutes - ALERT FALSE (current_minute = {current_minute}, alert_5_minutes = {alert_5_minutes})")
    elif current_minute % 2 == 0:
        if alert_2_minutes:
            os.system("say '2 minutes'")
            logger.info(f"Bar completion alert - 2 minutes - ALERT TRUE (current_minute = {current_minute}, alert_2_minutes = {alert_2_minutes})")
        else:
            logger.info(f"Bar completion alert - 2 minutes - ALERT FALSE (current_minute = {current_minute}, alert_2_minutes = {alert_2_minutes})")
    elif current_minute % 1 == 0:
        if alert_1_minute:
            os.system("say '1 minute'")
            logger.info(f"Bar completion alert - 1 minute - ALERT TRUE (current_minute = {current_minute}, alert_1_minute = {alert_1_minute})")
        else:
            logger.info(f"Bar completion alert - 1 minute - ALERT FALSE (current_minute = {current_minute}, alert_1_minute = {alert_1_minute})")
    else:
        logger.info("Bar completion alert - No alert (current_minute = {current_minute})")


#=====================================================================================
def main():
    logger.info("Started")

    # We want to schedule the job so that run_alert_bar_completion() is called at the exact completion of every 1 minute bar
    # The job will be scheduled to run every 1 minute
    schedule.every().minutes.at(':00').do(run_alert_bar_completion)

    # Scheduler loop
    while True:
        n = schedule.idle_seconds()
        logger.info(f"Seconds to run: {n} ")
        if n is None:
            time.sleep(1)
        elif n <= 0:
            # Do not sleep
            pass
        elif n > 1.5:
            time.sleep(1)
        else:
            # sleep exactly the right amount of time
            time.sleep(n)
        schedule.run_pending()

    logger.info("Bot Finished!")

#=====================================================================================
def test():
    run_alert_bar_completion()

#=====================================================================================
if __name__ == "__main__":
    main()
    #test()

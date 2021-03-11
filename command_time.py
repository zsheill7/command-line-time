import click
from datetime import date
from datetime import datetime
import pandas as pd
import csv

__author__ = "Zoe Sheill"

# What the user passes in:
# 1. The name of the activity 2. A category between 1-8 
# that the activity falls into

# Categories:
# 1. Classes
# 2. Early morning/night
# 3. Tutoring
# 4. Incomm
# 5. Friends in-house
# 6. Friends outside house
# 7: Minecraft/Youtube
# 8: Checking assignments/doing administrative type things
# 9: Messaging friends/discord
# 10: Music
# 11: Random Learning/Projects
# 12: Other

# What we need to do:
# Make it so the program starts a new column on a new day
# For each day, time goes on the left, activity goes on the right
# Get df from csv, add new entry, put df back into csv each time

# Example dictionary:
# {
#     "3/3": 
#     {
#         "9:30": {
#             "Activity": "Wake up",
#             "Category": 2
#         }
#     }
# }

# Example dataframe:
# Date  Time    Activity    Category
# 3/3   9:30    Wake up     Minecraft/Youtube

# Function call:
# python3 command_time.py -a "Minecraft" -c 7 test

# Commands are entered in post-doing, so after you finish a task, you enter in what you just finished


@click.group()
@click.option('--activity', '-a', type=str,
help='Name of task done at that time')
@click.option('--category', '-c', type=str,
help='Category (from 1 to 12) of which category this task falls into - in comments above')
@click.pass_context
def main(ctx, activity, category):
    """
    Uses command line to log time
    """
    ctx.obj = {
        'activity': activity,
        'category': category
    }
    pass

@main.command()
@click.pass_context
def test(ctx):
    """
    Main command for testing command line tool.
    Commands should be in the format:
    python command_time.py -t Minecraft -c 7
    """
    input_task()

@click.pass_context
def input_task(ctx):
    """ 
    Given a task from the user in the form ./command_time "Minecraft" 7
    This modifies the existing CSV to have a new line item for Minecraft with the 
    category Minecraft/Youtube. t means task and c means category
    """
    categories_dict = {
        1 : "Classes",
        2 : "Early morning/night",
        3 : "Tutoring",
        4 : "Incomm",
        5 : "Friends in-house",
        6 : "Friends outside house",
        7 : "Minecraft/Youtube",
        8 : "Checking assignments/doing administrative type things",
        9 : "Messaging friends/discord",
        10: "Music",
        11: "Random Learning/Projects",
        12: "Other"
    }

    activity = ctx.obj["activity"]
    category = ctx.obj["category"]
    # print("activity: ", activity)
    # print("category: ", category)

    today = date.today()
    today_date = today.strftime("%d/%m")
    now = datetime.now()
    current_time = now.strftime("%H:%M")

    # print("today_date: ", today_date)
    # print("current_time: ", current_time)

    # record_dict = {}
    #
    # if today_date not in record_dict:
    #     record_dict[today_date] = {
    #         current_time: {
    #             "Activity": activity,
    #             "Category": categories_dict[int(category)]
    #         }
    #     }
    # else:
    #     record_dict[today_date][current_time] = {
    #         {
    #             "Activity": activity,
    #             "Category": categories_dict[int(category)]
    #         }
    #     }
    # print("recording dict")
    # print(record_dict)


    output_file_name = '/Users/zoe/Documents/coding/command-line-time/time_record_2021.csv'

    # fields = ['date', 'time', 'activity', 'category']
    df = pd.read_csv(output_file_name, index_col=0)
    
    df = df.append({'date': today_date, 'time': current_time, 'activity': activity, "category": categories_dict[int(category)]}, ignore_index=True)

    df.to_csv(output_file_name)



if __name__ == "__main__":
    main()
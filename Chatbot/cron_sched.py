# sudo python3 -m pip install python-crontab
# Cron scheduler

from crontab import CronTab
import subprocess
import os

def create_cron(rep_time,pyScript,remark):
    # True= current user
    my_cron = CronTab(user=True)
    # Specific case when every 90 seconds
    path=os.path.dirname(os.path.abspath(__file__))+"/"
    pyScript=f"cd {path};{pyScript}"
    if rep_time==90:
        job = my_cron.new(command=(f'sleep 90;{pyScript}'), comment=remark)
        job.minute.every(1)
        job.enable()
    rep_time/=60
    rep_time=int(rep_time)
    job = my_cron.new(command=pyScript, comment=remark)
    job.minute.every(rep_time)
    job.enable()
    # Clear all task restrictions, ie this would remove every 3 minutes
    # job.clear()
    # save cron job
    my_cron.write()
    return (f'Created job: {remark}')

def find_cron(input):
    # sudo crontab -u devasc -l
    cron_jobs=subprocess.run(['sudo', 'crontab', '-u', 'devasc', '-l'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    #Evaluate
    if input in cron_jobs:
        cron_found=(f'Found {input} Job')
    else:
        cron_found=(f'No job {input} found')
    return cron_found

def run_cron(cron_job_comment,cron_job_command):
    my_cron = CronTab(user=True)
    flag=False
    for job in my_cron:
        if job.comment == cron_job_comment:
            if job.command==cron_job_command:
                job.run()
                flag=True
                break
    if flag==False:
        return_data=(f'{cron_job_comment} not Found')
    else:
        return_data=(f'{cron_job_comment} Ran')
    return 

def del_cron(cron_job):
    my_cron = CronTab(user=True)
    flag=0
    for job in my_cron:
        if job.comment == cron_job:
            my_cron.remove(job)
            my_cron.write()
            flag=1
    if flag==0:
        return f'{cron_job} not found'
    else:
        return f'deleted {cron_job}'
# def parse_cron():


# def print_var():
#     for (name, value) in cron.env.items():
#         print(name)
#         print(value)

'''
Cron TAB Research
=====
Article 1 - https://www.cyberciti.biz/faq/linux-show-what-cron-jobs-are-setup/
Article 2 - https://towardsdatascience.com/how-to-schedule-python-scripts-with-cron-the-only-guide-youll-ever-need-deea2df63b4e

=====
Display all cronjobs per user
    sudo crontab -u userName -l
So for our labe we do
    sudo crontab -u devasc -l
Alternatively
    crontab -l
Cron jobs can be ran in /etc/crontab file
    less /etc/crontab


'''
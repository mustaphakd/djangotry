import time
import sqlite3
from jenkinsapi.jenkins import Jenkins

class JenkinsJob:
    'A Jenkins Job '

    def __init__(self, name, status, timeChecked):
        self.name = name
        self.status = status
        self.timeChecked = timeChecked
    


def listJenkinsJobs(url, username, password):
    'function list jobs from a given instance'

    jenkins = Jenkins(url, username, password)
    job_names = jenkins.keys()

    if (len(job_names) < 1):
        return

    time_retrieved = "%s" % (time.asctime( time.localtime(time.time())))

    jobs = []

    for job_name in job_names:
      current_job = jenkins[job_name]
      job_status = "running"

      isrunning = current_job.is_queued_or_running()

      if not isrunning:
          current_build = current_job.get_last_build()
          job_status = "%s" % (current_build.get_status())
          
      jobs.append(JenkinsJob(job_name,job_status, time_retrieved))
    
    conn = sqlite3.connect('jobs.db')
    #cursor = conn.cursor()

    conn.execute(''' CREATE TABLE IF NOT EXISTS jenkins_jobs
    ( id        INT PRIMARY KEY NOT NULL,
      name      TEXT NOT NULL,
      status    TEXT NOT NULL,
      time_checked TEXT NOT NULL
    ); ''')

    if len(jobs) < 1:
        return

    processed_jobs = []

    for job in jobs:
        processed_jobs
            .append((job.name, job.status, job.timeChecked))

    del jobs
    cursor = conn.cursor()

    try:
        cursor.executemany(
            'INSERT INTO jenkins_jobs VALUES (?,?,?)',
            processed_jobs)

        conn.commit()
    except:
        conn.rollback()
    
    conn.close()

# Logs Analysis Project

### by Louis Magdaleno
### 9/13/2018

Logs Analysis Project, part of the Udacity
[Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## Project Overview
To write SQL queries that will extract the information needed to answer
the following three questions about a PSQL database.

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Project Files
* README.md ( this file)
* log_analysis_tool.py (Python code that will query the news database
                        and answer the three questions mentioned above.)
* output.txt ( plain text file of results from running the python code)

## Requirements
* VirtualBox 3.1
* Vagrant
* Python 3
* psycopg2
* PostgreSQL
* Ubuntu VM image provided by Udacity

## Running the Code
1. Copy the log_analysis_tool.py file into the vagrant/ directory on your VM.
2. Connect to your VM via shell by using the command `vagrant ssh`
3. Ensure that all required software is installed, particularly psycopg2 for Python3.
4. Run the following command to execute the Python code and view the query results.
    `python3 log_analysis_tool.py`
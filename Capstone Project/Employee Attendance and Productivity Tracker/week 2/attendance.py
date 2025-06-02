import pandas as pd
import numpy as np

attendance_df = pd.read_csv("attendance.csv")
tasks_df = pd.read_csv("tasks.csv")

attendance_df['date'] = pd.to_datetime(attendance_df['date'])
attendance_df['clock_in'] = pd.to_datetime(attendance_df['clock_in'])
attendance_df['clock_out'] = pd.to_datetime(attendance_df['clock_out'])

attendance_df['clock_out'].fillna(pd.NaT, inplace=True)

attendance_df['work_hours'] = np.where(
    attendance_df['clock_out'].notna(),
    (attendance_df['clock_out'] - attendance_df['clock_in']).dt.total_seconds() / 3600,
    np.nan
)

merged_df = pd.merge(
    attendance_df,
    tasks_df.groupby(['employee_id', 'date'])['task_id'].count().rename('tasks_completed'),
    on=['employee_id', 'date'],
    how='left'
)

merged_df['productivity_score'] = merged_df['tasks_completed'] / merged_df['work_hours']

merged_df['productivity_score'].replace([np.inf, -np.inf], np.nan, inplace=True)

summary = merged_df.groupby('employee_id').agg({
    'work_hours': 'mean',
    'productivity_score': 'mean',
    'date': 'count'
}).rename(columns={'date': 'days_worked'})

top_performers = summary.nlargest(5, 'productivity_score')

frequent_absentees = summary[summary['days_worked'] < 5].nsmallest(5, 'days_worked')

report = f"""
Employee Performance Report
---------------------------

Top Performers (by productivity score):
{top_performers[['work_hours', 'productivity_score']]}

Frequent Absentees (less than 5 days worked):
{frequent_absentees[['days_worked', 'work_hours']]}

Overall Statistics:
- Average work hours per day: {summary['work_hours'].mean():.2f}
- Average productivity score: {summary['productivity_score'].mean():.2f}
"""

print(report)

merged_df.to_csv('cleaned_attendance_tasks.csv', index=False)
with open('performance_report.txt', 'w') as f:
    f.write(report)
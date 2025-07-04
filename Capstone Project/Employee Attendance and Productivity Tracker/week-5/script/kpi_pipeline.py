import pandas as pd
import os
os.makedirs("output", exist_ok=True)
attendance_df = pd.read_csv("C:/Users/adity/Downloads/Capstone Projects/Capstone Projects/Employee Attendance/week-5/data/attendance_logs.csv")
tasks_df = pd.read_csv("C:/Users/adity/Downloads/Capstone Projects/Capstone Projects/Employee Attendance/week-5/data/tasks.csv")
attendance_df['clockin'] = pd.to_datetime(attendance_df['clockin'])
attendance_df['clockout'] = pd.to_datetime(attendance_df['clockout'])
attendance_df['workhours'] = (attendance_df['clockout'] - attendance_df['clockin']).dt.total_seconds() / 3600
attendance_df['workhours'] = attendance_df['workhours'].round(2)
combined_df = pd.merge(attendance_df, tasks_df, on='employeeid', how='inner')
department_kpis = combined_df.groupby('department').agg({
    'workhours': 'mean',
    'taskscompleted': 'mean',
    'employeeid': 'count'
}).reset_index()
department_kpis.rename(columns={
    'workhours': 'avg_workhours',
    'taskscompleted': 'avg_tasks_completed',
    'employeeid': 'records_count'
}, inplace=True)
department_kpis.to_csv('output/department_kpis.csv', index=False)
print(department_kpis)

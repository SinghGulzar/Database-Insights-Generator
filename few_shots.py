few_shots= [
    {'Question' : "How many employees are male employees?",
     'SQLQuery' : "SELECT count(*) from employees where gender='m'",
     'SQLResult': "Result of the SQL query",
     'Answer' :'179973' },
    {'Question': "what is the maximum salary given to employee?",
     'SQLQuery':"select max(salary) from salaries",
     'SQLResult': "Result of the SQL query",
     'Answer':"158220"},
    {'Question': "How many male and femle employees working in company?" ,
     'SQLQuery' : "select gender, count(gender) from employees group by gender",
     'SQLResult': "Result of the SQL query",
     'Answer':"m=179973,f=120051"} ,
     {'Question' : "how many unique name are there in employees?" ,
      'SQLQuery': "select count(distinct first_name) from employees",
      'SQLResult': "Result of the SQL query",
      'Answer' : "1275"},
    {'Question': "get the employee number of the employee who is having 3rd highest salary",
     'SQLQuery' : "select emp_no,round(avg(salary)) from salaries group by emp_no order by 2 desc limit 2,1",
     'SQLResult': "Result of the SQL query",
     'Answer' :"37558"
     }
        ]
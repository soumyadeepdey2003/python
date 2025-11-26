import pandas as pd

d=pd.DataFrame({

    "Name":['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    "Age":[25, 30, 35, 28, 32],
    "Salary":[50000, 60000, 75000, 55000, 68000],
    "Department":[ 'HR', 'IT', 'Finance', 'IT', 'HR' ]

})

print(d)
print(d.info())

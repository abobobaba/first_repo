from datetime import datetime as dt

deployment_date = input("please enter the deployment date in this format dd/mm/yy: ")
deployment = dt.strptime(deployment_date, "%d/%m/%y")

today = dt.now()

days = (deployment.date() - today.date()).days
days = abs(days)

print(days)
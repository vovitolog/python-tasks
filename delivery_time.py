hours_now = int(input())
minutes_now = int(input())
minutes_wait = int(input())
days_wait = minutes_wait // 1440
hours_output = ((minutes_wait - days_wait * 1440 + minutes_now) // 60 + hours_now) % 24
minutes_output = (minutes_wait + minutes_now) % 60
result = f"{{{hours_output:02}:{minutes_output:02}}}"
print(result[1:-1])

week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for i in range(0, len(week)):
    print(f"Day #{i+1} is {week[i]} and it is {'working day' if i < 5 else 'weekend'}.")
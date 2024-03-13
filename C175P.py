import matplotlib.pyplot as plt
import psutil


app_name_dict = {}


count = 0


for p in psutil.process_iter():
    
    count += 1
    if count <= 6:
        name = p.name()
        cpu_usage = p.cpu_percent()
        print("Name:", name, "- CPU Usage:", cpu_usage)
        app_name_dict.update({name: cpu_usage})
    else:
        break


keymax = max(app_name_dict, key=app_name_dict.get)
print("Application with Maximum CPU Usage:", keymax)


keymin = min(app_name_dict, key=app_name_dict.get)
print("Application with Minimum CPU Usage:", keymin)


name_list = [keymax, keymin]
print("Name List:", name_list)


app = app_name_dict.values()
max_app = max(app)
min_app = min(app)
print("Maximum CPU Usage:", max_app)
print("Minimum CPU Usage:", min_app)


max_min_list = [max_app, min_app]
print("Max Min List:", max_min_list)


plt.figure(figsize=(8, 6))
plt.xlabel('Applications')
plt.ylabel('CPU Usage (%)')


plt.bar(name_list, max_min_list, width=0.4, color=['blue', 'green'])


plt.show()

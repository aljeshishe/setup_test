import tools
print(tools.a)
import clearml
task = clearml.Task.init(project_name="grachev")
print(task)

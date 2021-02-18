import tools
print(tools.a)
tools.run()
import tools2
print(tools2.a)

import clearml
task = clearml.Task.init(project_name="grachev")
print(task)

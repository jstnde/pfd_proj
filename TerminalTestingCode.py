import os

process1 = os.system("pytest --headless --edge --html=reportedge.html --maximize -n=4")
process2 = os.system("pytest --headless --chrome --html=reportchrome.html --maximize -n=4")

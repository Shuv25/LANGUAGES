class employee:
    def __init__(self):
        print("Constructor is called")
    def __del__(self):
        print("distrcutor is called")

e=employee()
del e
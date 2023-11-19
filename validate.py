class valid:
    def __init__(self):
        pass
    def age(self,ag):
        try:
            if ag>7 or ag<25:
                return True
            else:
                return False
        except:
            return "False"
    def Phone(self,tell):
        try:
            if tell>=61000000 or tell<=6999999999:
                return True
            else:
                return False
        except:
            return "False"
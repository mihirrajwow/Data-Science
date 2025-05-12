class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

mihirApplication = RailwayForm()
mihirApplication.name = "Mihir"
mihirApplication.train = "Vande Bharat"
mihirApplication.printData()
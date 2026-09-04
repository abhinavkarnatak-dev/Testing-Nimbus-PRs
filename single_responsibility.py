class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def get_report(self):
        return f"{self.title}\n{self.content}"

class ReportPrinter:
    @staticmethod
    def print_report(report):
        print(report.get_report())

if __name__ == '__main__':
    report = Report("Monthly Report", "Sales were high.")
    ReportPrinter.print_report(report)

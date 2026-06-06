
from fpdf import FPDF


class Cs50(FPDF):
    def __init__(self, name):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.name = name

    def header(self):
        self.set_font("helvetica", "B", 40)
        self.cell(0, 20, "CS50 Shirtificate", align="C")

    def shirtificate(self):
        self.image("cs50p/week_8/shirtificate.png", x=10, y=60, w=190)
        self.set_font("helvetica", "B", 25)
        self.set_text_color(255,255,255)
        self.set_xy(0, 140)
        self.cell(210, 10, f"{self.name} took CS50", align="C")

def main():
    name = input("Name: ")

    pdf = Cs50(name)

    pdf.add_page()
    pdf.shirtificate()

    pdf.output("h.pdf")


if __name__ == "__main__":
    main()

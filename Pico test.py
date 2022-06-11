from guizero import App, Picture, Text, TextBox

with open(r"C:\Users\ewa_1\PycharmProjects\GUI\led_value.txt") as f:
    led = f.read()


def pin_test():
    if led == "1":
        yesorno.value = "Tak"
    else:
        yesorno.value = "Nie"


app = App(title="Raspberry Pi Pico Pin Testing", height=700, width=500)
pico = Picture(app, r"C:\Users\ewa_1\Downloads\sensors_pico_u2if_pinout.png")
question1 = Text(app, text="Wybierz pin do testowania:")
pinnum = TextBox(app, command=pin_test)
question2 = Text(app, text="Czy wybrany pin działa prawidłowo?")
yesorno = TextBox(app, command=pin_test)
app.display()

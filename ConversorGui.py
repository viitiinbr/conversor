# Conversor de temperaturas com interface gráfica
from conversor import *
import PySimpleGUI as psg

frame_layout = [
                        [psg.Radio('Celsius --> Fahrenheit: ', key='cel_fah', group_id='1', default=True)],
                        [psg.Radio('Fahrenheit --> Celsius: ', key='fah_cel', group_id='1')],
                ]

layout = [

        [
                psg.Text('Informe a temperatura: '),
                psg.Frame('Converter: ', frame_layout)
        ],
        [
                psg.InputText('', key='temp', ),
        ],
        [
                psg.Button('Converter'), psg.Button('Canlcelar'),
                psg.Text("", key='temp_convertida'),
        ],
]

janela = psg.Window('Conversor de Temperatura', layout)

while True:
        evento, valores = janela.read()

        if evento == psg.WIN_CLOSED or evento == 'Canlcelar':
                break
        else:
                # print(valores)
                temp = valores['temp']
                fah = cel_fah(int(temp))
                janela['temp_convertida'].update(f'{temp}ºC = {fah}ºF')
janela.close()
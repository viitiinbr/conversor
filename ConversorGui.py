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
                psg.Button('Converter'),
                psg.Button('Canlcelar'),
                psg.Button('Limpar'),
                psg.Text("", key='temp_convertida'),
        ],
]

janela = psg.Window('Conversor de Temperatura', layout)

def limpar():
        janela['temp'].update("")
        janela['cel_fah'].update(True)
        janela['temp_convertida'].update("")

while True:
        evento, valores = janela.read()

        if evento == psg.WIN_CLOSED or evento == 'Canlcelar':
                break
        elif evento == 'Limpar':
                limpar()
        else:
                # print(valores)
                if valores['cel_fah']:
                        temp = cel_fah(float(valores['temp']))
                        janela['temp_convertida'].update(f'{valores["temp"]}ºC = {temp}ºF')
                else:
                        temp = fah_cel(float(valores['temp']))
                        janela['temp_convertida'].update(f'{valores["temp"]}ºF = {temp}ºC')
                # limpar()
janela.close()

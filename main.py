from pyscript import document, display

import arrr
import matplotlib.pyplot as plt
import numpy as np


def evaluate_model(Vmax, p1, p2, p3, q1, q2):
    v = Vmax * (q1-q2) / (1 + p1*q1 + p2*q2 + p3*q1*q2)
    return v

def get_param_values():
    Vmax = document.querySelector("#Vmax-value")
    p1 = document.querySelector("#p1-value")
    p2 = document.querySelector("#p2-value")
    p3 = document.querySelector("#p3-value")
    return float(Vmax.value), float(p1.value), float(p2.value), float(p3.value)

def set_param_values(Vmax, p1, p2, p3):
    document.querySelector("#Vmax-value").value = Vmax
    document.querySelector("#p1-value").value = p1
    document.querySelector("#p2-value").value = p2
    document.querySelector("#p3-value").value = p3

def make_plot(event):
    Vmax, p1, p2, p3 = get_param_values()

    q1 = np.linspace(0, 10, 5)
    q2 = np.linspace(0, 4, 4)

    fig, ax = plt.subplots()

    for q2i in q2:
        y = []
        for q1i in q1:
            y.append(evaluate_model(Vmax, p1, p2, p3, q1i, q2i))
        label_string = f'q2 = {q2i}'
        print(label_string)
        plt.plot(q1, y, label=label_string)

    plt.xlabel('q1')
    plt.ylabel('v')
    plt.legend(loc='lower right')
    display(fig, target="output")


def translate_english(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    output_div.innerText = arrr.translate(english)
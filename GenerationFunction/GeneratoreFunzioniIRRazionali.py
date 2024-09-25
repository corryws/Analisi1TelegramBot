import matplotlib.pyplot as plt
import random
import math

# Funzione per pulire e semplificare le espressioni
def simplify_expression(coeff, variable):
    if coeff == 1:
        return variable  # Elimina il coefficiente "1"
    elif coeff == -1:
        return f"-{variable}"  # Elimina il coefficiente "-1"
    else:
        return f"{coeff}{variable}"

# Funzione per generare un'equazione casuale con espressioni razionali, irrazionali, logaritmo e valore assoluto
def generate_rational_irrational_function_text():
    # Genera coefficienti casuali per le espressioni
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)

    # Genera costanti casuali
    const_rational = random.randint(1, 10)
    const_irrational = random.randint(1, 10) * random.choice([math.sqrt(2), math.sqrt(3), math.pi])

    # Funzioni più complesse con logaritmo, valore assoluto, e combinazioni non banali
    functions = [
        f"f(x) = \\frac{{{simplify_expression(a, 'x')} + {b}}}{{{simplify_expression(c, 'x')} + {d}}}",
        f"f(x) = \\sqrt{{{simplify_expression(a, 'x')} + {b}}}",
        f"f(x) = \\frac{{{a}}}{{x^2 + {b}x + {c}}}",
        f"f(x) = {simplify_expression(a, 'x^2')} + {simplify_expression(b, 'x')} + {c}",
        f"f(x) = {simplify_expression(a, 'x^2')} + \\ln({simplify_expression(b, 'x')} + {c})",
        f"f(x) = {simplify_expression(a, '|x + ' + str(b) + '|')} + {c}",
        f"f(x) = \\ln({simplify_expression(a, 'x^2')} + {b})",
        f"f(x) = \\frac{{\\ln({simplify_expression(a, 'x')} + {b})}}{{{c}}}",
        f"f(x) = \\frac{{{a}}}{{\\ln(x + {b})}} + \\sqrt{{x}}",
        f"f(x) = \\frac{{\\ln({simplify_expression(a, 'x^2')} + {b})}}{{\\sqrt{{x + {c}}}}}",
        f"f(x) = \\frac{{{a}}}{{|x + {b}|}} + {simplify_expression(c, 'x^2')}"
    ]
    
    # Seleziona casualmente una funzione complessa
    function = random.choice(functions)
    
    return function


def ReturnRationalIrrationalFunctionImage():
    # Genera la funzione
    function_text = generate_rational_irrational_function_text()

    # Configura l'immagine
    plt.figure(figsize=(6, 2))
    plt.text(0.5, 0.5, f"${function_text}$", fontsize=18, ha='center', va='center')

    # Rimuovi assi
    plt.axis('off')

    # Salva l'immagine come .jpg
    image_path = "C:/Users/co72/OneDrive/Desktop/bottelegram/rational_irrational_function_final.jpg"
    plt.savefig(image_path, bbox_inches='tight', pad_inches=0.1, format='jpg')

    # Restituisci il percorso dell'immagine generata
    return image_path


# Funzione main per richiamare ReturnRationalIrrationalFunctionImage
def main():
    # Chiama la funzione che genera l'immagine
    image_path = ReturnRationalIrrationalFunctionImage()
    
    # Stampa il percorso dell'immagine generata
    print(f"Immagine generata e salvata in: {image_path}")
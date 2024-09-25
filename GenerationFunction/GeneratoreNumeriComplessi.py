import matplotlib.pyplot as plt
import random

# Funzione per generare un'equazione casuale sui numeri complessi
def generate_complex_equation_text():
    # Genera costanti casuali
    real = random.randint(-10, 10)
    imag = random.randint(-10, 10)
    const_real = random.randint(-10, 10)
    const_imag = random.randint(-10, 10)
    const_complex = complex(const_real, const_imag)
    
    # Sostituisce la "j" con "i" per la parte immaginaria
    const_complex_str = str(const_complex).replace('j', 'i')
    
    # Possibili equazioni
    operations = [
        f"z - |z|^2 = {const_complex_str}", 
        f"Im(z) + Re(z) = {const_complex_str}",
        f"|z|^2 + z = {const_complex_str}", 
        f"z + 1/z = {const_complex_str}", 
        f"Re(z) * Im(z) = {const_real}",
        f"z^2 + |z| = {const_complex_str}",
        f"Im(z) - Re(z) = {const_real}",
        f"z + |z|^2 = {const_complex_str}",
        f"Re(z) / Im(z) = {const_real}",
        f"z^2 - 2z = {const_complex_str}",
        f"z + Re(z) = {const_complex_str}"
    ]
    
    # Seleziona casualmente un'equazione
    equation = random.choice(operations)
    
    return equation


def ReturnComplexImage():
    # Genera l'equazione
    equation_text = generate_complex_equation_text()

    # Configura l'immagine
    plt.figure(figsize=(6, 2))
    plt.text(0.5, 0.5, f"${equation_text}$", fontsize=18, ha='center', va='center')

    # Rimuovi assi
    plt.axis('off')

    # Salva l'immagine come .jpg
    image_path = "C:/Users/co72/OneDrive/Desktop/bottelegram/complex_equation_final.jpg"
    plt.savefig(image_path, bbox_inches='tight', pad_inches=0.1, format='jpg')

    # Mostra l'immagine generata
    return image_path

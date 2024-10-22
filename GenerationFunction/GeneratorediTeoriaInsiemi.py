def ReturnTeoriaFunzioniContinue():
    Teorema = (
        "INTRODUZIONE ALLE FUNZIONI CONTINUE\n"
        "una funzione f:X->R si dice continua in X se lo è per ogni punto di X\n"
        "Una funzione f(x) è contina in x0 se:\n\n"
        "1)f(x0) esiste \n 2)lim x->x0 f(x) = f(x0) \n 3)lim x->x0 f(x) esiste ed è finito\n\n"

        "TEOREMA DELL'ESISTENZA DEGLI ZERI\n\n"
        "[Richiesta conoscenza della definizione di funzione continua]\n"
        "IPOTESI: Sia f:[a,b] -> R una funzione Continua in [a,b] tale che:\n"
        "f(a) > 0 e f(b) < 0\n\n"
        "TESI: Da questa ipotesi allora Esisterà un punto c € ]a,b[ tale che f(c) = 0\n\n"
        "DIMOSTRAZIONE: Il Teorema lo si dimostra usando la tecnica della bisezione.\n"
        "divido in due parti l'intervallo [a,b] e ne valuto la funzione nel punto di mezzo\n"
        "Se quest'ultima dovesse risultare nulla/0 allora il teorema è dimostrato.\n"
        "Caso contrario, ripeto l'operazione di bisezione suddividendo la metà\n"
        "dell'intervallo precedente tale che f(a1) > 0 e f(b1) < 0.\n"
        "continuando così si otteranno due successioni numeriche {an} e {bn}\n"
        "entrambi convergenti allo stesso limite. Dimostriamo quindi che:\n"
        "il limite f(an)>=0 e il limite f(bn) <= 0 per cui necessariamente\n"
        "f(c) = 0 è la tesi dimostrata\n\n"

        "-----------------------------------------------------\n\n"

        "TEOREMA DI WEIERSTRASS\n\n"
        "[Richiesta conoscenza di Sottoinsieme, chiuso, limitato, Estremo sup e inf]\n"
        "IPOTESI: Sia K un sottoinsieme chiuso e limitato di R e f:K->R continua in K\n"
        "TESI: Da questa ipotesi f avrà un Massimo e un Minimo\n"
        "dunque Esisterà un x1,x2 € K tale che f(x1) = sup f\n"
        "e f(x2) = inf f\n\n"
 
        "/Teoria"
    )
    return Teorema

def ReturnTeoriaDifferenziale():
    Teorema =(
        "Teoremi fondamentali del Calcolo Differenziale\n\n"

        "Nota importante da sapere su questi teoremi è quello che le funzioni che trattano\n"
        "devono essere finite e analizzare in un intervallo chiuse [a,b] e non devono\n"
        "presentare punti di non derivabilità[Cuspide,Flesso a tangente veritcale, Angoloso]\n"

        "I teoremi fondamentali del Calcolo Differenziali sono 4\n"
        "[FERMAT,ROLLE,CAUCHY,LAGRANGE] e gli argomenti da sapere per sapere\n"
        "a sua volta questi teoremi sono i seguenti:\n"
        "-Teorema di confronto tra limiti\n"
        "-Teorema di Weierstrass\n"

        "-----------------------------------------------------\n\n"

        "TEOREMA DI FERMAT\n\n"
        "[Richiesta conoscenza del Teorema di confronto tra limiti]\n"
        "Esso stabilisce una condizione necessaria affinché un punto sia di estremo relativo\n"
        "che potranno essere di Massimo o Minimo assoluto\n"
        "IPOTESI: Sia f:(a,b) -> R una funzione Reale, devono verificarsi i seguenti casi\n"
        "- x0 sia un punto interno di (a,b)\n"
        "- f sia derivabile in x0\n"
        "- x0 sia un punto di estremo relativo per f(Max o Min relativo)\n\n"
        "TESI: Da questa ipotesi allora f'(x0) = 0\n\n"
        "DIMOSTRAZIONE:Supponiamo che x0 sia un punto di estremo relativo Minimo allora\n"
        "esiste δ > 0 tale che: \n"
        "f(x) >= f(x0) Vx € ]x0 - δ, x0 + δ[\n"
        "Da ciò segue subito che, per il teorema di confronto tra limiti si ha che\n"
        "il limire del rapporto incrementale destro sia maggiore di 0 e quello sinistro minore\n"
        "di 0. Quindi, la tesi f'(x0) = 0 si ha per l'unicità del limite\n"

        "-----------------------------------------------------\n\n"

        "TEOREMA DI ROLLE\n\n"
        "[Richiesta conoscenza del Teorema di Fermat e Weierstrass]\n"
        "IPOTESI: data una funzione f:[a,b] -> R, essa deve essere\n"
        "- Continua in [a,b]\n"
        "- derivabile in ]a,b[\n"
        "- f(a) = f(b)\n\n"
        "TESI: Data questa ipotesi, la tesi dice che esisterà un punto c € ]a,b[ tale che f'(c) = 0\n\n"
        "DIMOSTRAZIONE: Il teorema lo si dimostra partendo dal Teorema di Weierstrass, per esso la funzione f\n"
        "ammette massimo e minimo in [a,b]. Se essi sono assunti nei punti a e b la funzione è costante ottenendo un\n"
        "ovvia conclusione. In caso contrario la tesi segue invece il Teorema di Fermat\n\n"
        "Il Teorema di Rolle assicura quindi l'esistenza di una o più tangenti orizzontali nell'intervallo ]a,b[\n\n"
        
        "-----------------------------------------------------\n\n"

        "TEOREMA DI CAUCHY\n\n"
        "[Richiesta conoscenza del Teorema di Rolle]\n"
        "Garantisce che esiste un c in ]a,b[\n"
        "IPOTESI: Sia f,g:[a,b] -> R due funzione Reali, devono verificarsi i seguenti casi\n"
        "- f e g siano continue in [a,b]\n"
        "- f e g siano derivabili in ]a,b[\n\n"
        "TESI: Da questa ipotesi allora Esiste un c € ]a,b[\n"
        "tale che [f(b) - f(a)]g'(c) = [g(b) - g(a)]f'(c)\n\n"
        "DIMOSTRAZIONE:la funzione w(x) = [f(b) - f(a)]g'(c) = [g(b) - g(a)]f'(c) \n"
        "soddisfa le ipotesi del TEOREMA DI ROLLE. Allora esisterà c € ]a,b[ tale che\n"
        "se si effettua w'(c) = 0 e si divide per g(b) - g(a) si otterrà la tesi\n"

        "-----------------------------------------------------\n\n"

        "TEOREMA DI LAGRANGE\n\n"
        "[Richiesta conoscenza del Teorema di Rolle]\n"
        "Garantisce che esiste una o più rette tangenti alla retta secante a,b\n"
        "IPOTESI: Sia f:[a,b] -> R una funzione Reale, devono verificarsi i seguenti casi\n"
        "- f sia continua in [a,b]\n"
        "- f sia derivabile in ]a,b[\n\n"
        "TESI: Da questa ipotesi allora Esiste un c € ]a,b[\n"
        "tale che f(b) - f(a) = [b - a]f'(c) \n"
        "o anche(semplificando) f'(c) = f(b) - f(a) / b - a \n\n"
        "DIMOSTRAZIONE: sia data la funzione w(x) = f(b) - f(a) / b - a che\n"
        "soddisferà le ipotesi del TEOREMA DI ROLLE. e dunque esisterà un\n"
        "c € ]a,b[ tale che w'(c) = 0. ricavandone così la Tesi\n"
        "COROLLARIO 1: se f'(c) = 0 V c € [a,b] f(c) è costante\n"
        "COROLLARIO 2: se f(c) e g(c) hanno la stessa derivata, sono la stessa funzione\n"
        "ma differenziate da una costante. y1 = x^3 + 1 è uguale a y2 = x^3 - 4\n"

        "-----------------------------------------------------\n\n"

        "TEOREMA DI CARATTERIZZAZIONE DELLE FUNZIONI A DERIVATA NULLA\n\n"
        "[Richiesta conoscenza del Teorema di Lagrange]\n"
        "IPOTESI: Sia f:[a,b] -> R una funzione Reale, devono verificarsi i seguenti casi\n"
        "- f sia continua in [a,b]\n"
        "- f sia derivabile in ]a,b[\n"
        "- f'(c) = 0  V x € ]a,b[\n"
        "TESI: Da questa ipotesi allora f è costante di [a,b]\n\n"
        "DIMOSTRAZIONE: Siano x1 e x2 € [a,b] con x1 < x2 applichiamo il Teorema di Lagrange\n"
        "alla restrizione di f all'intervallo [x1,x2] per dimostrare che f(x1) = f(x2) e si ha dunque\n"
        "l'esistenza di un c € [x1,x2] tale che f'(c) = f(x1) - f(x2) / x1 - x2 provandone la tesi\n"

        "-----------------------------------------------------\n\n"
 
        "/Teoria"
    )
    return Teorema
import numpy as np
import matplotlib.pyplot as plt


class Signal:
    def __init__(self, name, values):
        self.name = name
        self.values = np.array(values, dtype=float)

    def mean_value(self):
        return np.mean(self.values)

    def min_value(self):
        return np.min(self.values)

    def max_value(self):
        return np.max(self.values)

    def plot(self):
        plt.figure(figsize=(10, 3))
        plt.plot(self.values, color="steelblue")
        plt.title(self.name)
        plt.xlabel("Vzorky")
        plt.ylabel("Amplituda")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def count_above(self, threshold):
        count_above = np.sum(self.values > threshold)



class ECGSignal(Signal):                              # ← závorka = dědíme od Signal
    def __init__(self, name, values, sampling_rate, lead="II"):
        super().__init__(name, values)                # ← zavolá __init__ rodiče
        self.sampling_rate = sampling_rate
        self.lead = lead

    def duration_seconds(self):
        return len(self.values) / self.sampling_rate

    def __str__(self):
        return (
            f"[{self.name}] svod={self.lead}, "
            f"vzorkování={self.sampling_rate} Hz, "
            f"délka={self.duration_seconds():.2f} s, "
            f"průměr={self.mean_value():.2f}"
        )


class RespirationSignal(Signal):
    def __init__(self, name, values, breathing_rate):
        super().__init__(name, values)
        self.breathing_rate = breathing_rate #frekvence dechů v dechách za minutu

    def breath_print(self):
        print(self.breathing_rate)




ekg = RespirationSignal(
    "EKG pacienta 42",
    [0.5, 1.2, 1.8, 0.9, 2.1, 1.5, 0.7, 1.1, 1.3, 0.8],
    16
)

ekg.plot()
ekg.breath_print()

# # Metody zděděné ze Signal – ECGSignal je nikde nedefinuje, přesto fungují:
# print(ekg.mean_value())    # 1.19
# print(ekg.max_value())     # 2.1
# ekg.plot()                 # vykreslí graf
#
# # Vlastní metody ECGSignal:
# print(f"Délka záznamu: {ekg.duration_seconds():.3f} s")
# print(f"Svod: {ekg.lead}")
#
# # __str__ je definovaná v ECGSignal, takže print používá tuhle verzi:
# print(ekg)
# # [EKG pacienta 42] svod=I, vzorkování=500 Hz, délka=0.02 s, průměr=1.19

#___________________________________________________________________________________________


#dozávorky se dá ta původní třída a bude se to chovat jako kdybych tam zkopíroval všechno z té rodičovské třídy
#abych nepřepsal init, tak to potřebuju jenom rozšířit, takže když napíšu init
#tak první tam zavolám super().__init__(co tu bylo) a tím se mi tu přepíše všechno co bylo v tom initu té původní
#při zavolání to budu používat jako jiné třídy
#agent je to co běží na mojem počítačí a model je to co on si volá aby mi zjistil co potřebuju
# aby mi to fungovalo ddobře, tak je potřeba:
#-pracovat v jedné složce kde jsou věci které ve složce potřebuje aby ho to nemátlo
#-před prací s agentem si to commitnout a pak si zkontrolova změny
#-agent umí i pracovat s githubem
#-je fajn si vytvořit instrukční soubor nebo nechat agenta tento soubor vytvořit
#-nedávat moc dlouhý kontext, pak začne blbnout
#- nechat si zapisovat apoznámky aby když začne blbnout, tak abych ho mohl zapnout znova (třeba markdown v readme)

#mohu mu dát i soubor kde budou skilly kde má napsané jak to má dělat a on si ho dá do kontextu až když ho bude potřebovat
# díky MCP serveru mi může dělat ledacos(klidně si ten server najde sám a od té doby to bude umět)

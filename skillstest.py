from pyscript import document


elements = {
    "H": "Symbol: H<br>Element: Hydrogen<br>Atomic Number: 1<br>Atomic Mass: 1.008",
    "HE": "Symbol: He<br>Element: Helium<br>Atomic Number: 2<br>Atomic Mass: 4.0026",
    "C": "Symbol: C<br>Element: Carbon<br>Atomic Number: 6<br>Atomic Mass: 12.011",
    "N": "Symbol: N<br>Element: Nitrogen<br>Atomic Number: 7<br>Atomic Mass: 14.007",
    "O": "Symbol: O<br>Element: Oxygen<br>Atomic Number: 8<br>Atomic Mass: 15.999",
    "F": "Symbol: F<br>Element: Fluorine<br>Atomic Number: 9<br>Atomic Mass: 18.998",
    "NE": "Symbol: Ne<br>Element: Neon<br>Atomic Number: 10<br>Atomic Mass: 20.180",
    "P": "Symbol: P<br>Element: Phosphorus<br>Atomic Number: 15<br>Atomic Mass: 30.974",
    "S": "Symbol: S<br>Element: Sulfur<br>Atomic Number: 16<br>Atomic Mass: 32.06",
    "CL": "Symbol: Cl<br>Element: Chlorine<br>Atomic Number: 17<br>Atomic Mass: 35.45",
    "AR": "Symbol: Ar<br>Element: Argon<br>Atomic Number: 18<br>Atomic Mass: 39.948",
    "SE": "Symbol: Se<br>Element: Selenium<br>Atomic Number: 34<br>Atomic Mass: 78.971",
    "BR": "Symbol: Br<br>Element: Bromine<br>Atomic Number: 35<br>Atomic Mass: 79.904",
    "KR": "Symbol: Kr<br>Element: Krypton<br>Atomic Number: 36<br>Atomic Mass: 83.798",
    "I": "Symbol: I<br>Element: Iodine<br>Atomic Number: 53<br>Atomic Mass: 126.90",
    "XE": "Symbol: Xe<br>Element: Xenon<br>Atomic Number: 54<br>Atomic Mass: 131.29",
    "RN": "Symbol: Rn<br>Element: Radon<br>Atomic Number: 86<br>Atomic Mass: 222",
}

NOT_FOUND_MESSAGE = "Element does not exist in the non-metals list."


def element(event=None):
    symbol = document.getElementById("symbol_input").value.strip().upper()
    result = elements.get(symbol, NOT_FOUND_MESSAGE)
    document.getElementById("result").innerHTML = result
# -------------------------------------------------------------------------------
# Name:        Get meteo data from https://www.danepubliczne.imgw.pl.
# Created:     20.12.2023
# Licence:     GNU
# Info:        Typy danych w plikach
# ------------------------------------------------------------------------------- typ danych w pliku meteo

"""
'B00300S' # Temperatura powietrza (oficjalna)
'B00305A' # Temperatura gruntu (czujnik)
'B00202A' # Kierunek wiatru (czujnik)
'B00702A' # Średnia prędkość wiatru czujnik 10 minut
'B00703A' # Prędkość maksymalna (czujnik)
'B00608S' # Suma opadu 10-minutowego
'B00604S' # Suma opadu dobowego
'B00606S' # Suma opadu godzinowego
'B00802A' # Wilgotność względna powietrza (czujnik)
'B00714A' # Największy poryw w okresie 10 min ze stacji Synoptycznej
'B00910A' # Zapas wody w śniegu (obserwator)
"""


def meteo_type(file_name):
    if 'B00300S' in file_name:  # Temperatura powietrza (oficjalna)
        return 'Ts'
    elif 'B00305A' in file_name:  # Temperatura gruntu (czujnik)
        return 'Tg'
    elif 'B00202A' in file_name:  # Kierunek wiatru (czujnik)
        return 'dd'
    elif 'B00702A' in file_name:  # Średnia prędkość wiatru (czujnik) z 10 minut
        return 'ff'
    elif 'B00703A' in file_name:  # Prędkość maksymalna (czujnik)
        return 'fx'
    elif 'B00608S' in file_name:  # Suma opadu 10-minutowego
        return 'r10m'
    elif 'B00604S' in file_name:  # Suma opadu dobowego
        return 'r24h'
    elif 'B00606S' in file_name:  # Suma opadu godzinowego
        return 'r1h'
    elif 'B00802A' in file_name:  # Wilgotność względna powietrza (czujnik)
        return 'rh'
    elif 'B00714A' in file_name:  # Największy poryw w okresie 10 min ze stacji Synoptycznej
        return 'qnt10'
    elif 'B00910A' in file_name:  # Zapas wody w śniegu (obserwator)
        return 'rws'
    else:
        return 'none'


# ------------------------------------------------------------------------------- typ danych w pliku hydro

"""
'B00020S' # Stan wody operacyjny
'B00050S' # Przepływ operacyjny
'B00014A' # Stan wody kontrolny
'B00101A' # Temperatura wody  (obserwator)

Stan wody operacyjny – są to dane operacyjne informujące o stanie wody w przekroju
    stacji wodowskazowej, podlegające wstępnej weryfikacji automatycznej i manualnej.
    Stan wody operacyjny nie może być wykorzystywany w sprawach sądowych.

Przepływ operacyjny – są to dane operacyjne, informujące o szacowanym przepływie wody
    w przekroju stacji wodowskazowej, wyliczane na podstawie stanu wody operacyjnego.
    Przepływ operacyjny nie może być wykorzystywany w sprawach sądowych.

Stan wody kontrolny - są to obserwacje stanu wody, wykonywane przez pracowników IMGW PIB
    podczas rutynowych kontroli działania urządzeń pomiarowych.
"""


def hydro_type(file_name):
    if 'B00020S' in file_name:  # Stan wody operacyjny
        return 'stan_wody'
    elif 'B00050S' in file_name:  # Przepływ operacyjny
        return 'przeplyw'
    elif 'B00014A' in file_name:  # Stan wody kontrolny
        return 'stan_wody_kontrolny'
    elif 'B00101A' in file_name:  # Temperatura wody  (obserwator)
        return 'temperatura'
    else:
        return 'none'

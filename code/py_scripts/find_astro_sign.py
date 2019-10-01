def find_sign(month,day):
    astro_sign = None
    if month == 12:
        astro_sign = 'Sagittaire' if (day < 22) else 'capricorne'
    elif month == 1:
        astro_sign = 'Capricorne' if (day < 20) else 'Verseau'
    elif month == 2:
        astro_sign = 'Verseau' if (day < 19) else 'Poissons'
    elif month == 3:
        astro_sign = 'Poissons' if (day < 21) else 'Bélier'
    elif month == 4:
        astro_sign = 'Bélier' if (day < 20) else 'Taureau'
    elif month == 5:
        astro_sign = 'Taureau' if (day < 21) else 'Gémeaux'
    elif month == 6:
        astro_sign = 'Gémeaux' if (day < 21) else 'Cancer'
    elif month == 7:
        astro_sign = 'Cancer' if (day < 23) else 'Lion'
    elif month == 8:
        astro_sign = 'Lion' if (day < 23) else 'Vierge'
    elif month == 9:
        astro_sign = 'Vierge' if (day < 23) else 'Balance'
    elif month == 10:
        astro_sign = 'Balance' if (day < 23) else 'Scorpion'
    elif month == 11:
        astro_sign = 'Scorpion' if (day < 22) else 'Sagittaire'
    return astro_sign
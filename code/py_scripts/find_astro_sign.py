def find_sign(month,day):
    astro_sign = None
    if month == 12:
        if (day < 22):
            astro_sign = 'Sagittaire'
        else:
            astro_sign = 'capricorne'
    elif month == 1:
        if (day < 20):
            astro_sign = 'Capricorne'
        else:
            astro_sign = 'Verseau'
    elif month == 2:
        if (day < 19):
            astro_sign = 'Verseau'
        else:
            astro_sign = 'Poissons'
    elif month == 3:
        if (day < 21):
            astro_sign = 'Poissons'
        else:
            astro_sign = 'Bélier'
    elif month == 4:
        if (day < 20):
            astro_sign = 'Bélier'
        else:
            astro_sign = 'Taureau'
    elif month == 5:
        if (day < 21):
            astro_sign = 'Taureau'
        else :
            astro_sign = 'Gémeaux'
    elif month == 6:
        if (day < 21):
            astro_sign = 'Gémeaux'
        else:
            astro_sign ='Cancer'
    elif month == 7:
        if (day < 23):
            astro_sign = 'Cancer'
        else:
            astro_sign = 'Lion'
    elif month == 8:
        if (day < 23):
            astro_sign = 'Lion'
        else:
            astro_sign = 'Vierge'
    elif month == 9:
        if (day < 23):
            astro_sign = 'Vierge'
        else:
            astro_sign = 'Balance'
    elif month == 10:
        if (day < 23):
            astro_sign = 'Balance'
        else:
            astro_sign = 'Scorpion'
    elif month == 11:
        if (day < 22):
            astro_sign = 'Scorpion'
        else:
            astro_sign = 'Sagittaire'
    return astro_sign
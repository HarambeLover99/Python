def how_eligible(essay):
    counter = 0
    if '?' in essay:
        counter = counter +1
    if ',' in essay:
        counter = counter +1
    if '"' in essay:
        counter = counter +1
    if '!' in essay:
        counter = counter +1
    return counter
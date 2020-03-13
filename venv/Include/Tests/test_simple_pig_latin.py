from Include.Classes.SimplePigLatin import pig_it

def test_pig_it():
    assert pig_it('Pig latin is cool') == 'igPay atinlay siay oolcay'
    assert pig_it('This is my string') =='hisTay siay ymay tringsay'
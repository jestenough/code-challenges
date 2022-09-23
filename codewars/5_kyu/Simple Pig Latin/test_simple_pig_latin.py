from solution_simple_pig_latin import pig_it


def test_pig_it():
    assert(pig_it('Pig latin is cool') == 'igPay atinlay siay oolcay')
    assert(pig_it('This is my string') == 'hisTay siay ymay tringsay')
    assert(pig_it('Quis custodiet ipsos custodes ?') == 'uisQay ustodietcay psosiay ustodescay ?')
    assert(pig_it('O tempora o mores !') == 'Oay emporatay oay oresmay !')

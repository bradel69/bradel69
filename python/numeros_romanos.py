# -*- coding: utf-8 -*-

def para_romana_unidades(valor):
    #             0   1    2    3     4   5   6     7      8     9   
    r_unidades = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
    return r_unidades[valor];

def para_romana_dezenas(valor):
    #                 10  20    30   40   50  60    70     80   90   
    r_dezenas = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    return r_dezenas[valor];

def para_romana_centenas(valor):
    #                100  200  300  400 500  600   700    800  900   
    r_centenas = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    return r_centenas[valor];

def para_romana_milhares(valor):
    #                1000  2000  3000
    r_milhares = ["","M","MM","MMM"]
    return r_milhares[valor];

def para_romana(numero):
    milhares = int(numero/1000)
    centenas = int((numero-milhares*1000)/100);
    dezenas = int((numero-milhares*1000-centenas*100)/10);
    unidades = numero-milhares*1000-centenas*100-dezenas*10;
    return para_romana_milhares(milhares)+para_romana_centenas(centenas)+para_romana_dezenas(dezenas) \
       +para_romana_unidades(unidades);

valor = 3999;

if (valor<=3999):
    print ( valor, "em numeração romana", para_romana(valor) );

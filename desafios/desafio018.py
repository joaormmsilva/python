from math import sin,cos,tan,radians

ang = radians(int(input('Qual angulo gostaria: ')))

seno = sin(ang)
cosseno = cos(ang)
tangente = tan(ang)


print("o angulo que vc escolheu foi {}\nO seno dele é {:.2f}\nO cosseno dele é {:.2f}\nE a tangente dele é {:.2f}".format(ang,seno,cosseno,tangente))
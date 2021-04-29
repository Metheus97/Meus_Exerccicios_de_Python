import math
ângulo = int(input('Digite o ângulo que você deseja: '))

sen = math.sin(math.radians(ângulo))
cos = math.cos(math.radians(ângulo))
tan = math.tan(math.radians(ângulo))
print('O seno do seu ângulo é {:.2f} \n O coseno do seu ângulo é {:.2f} \n A tangente do seu ângulo é {:.2f}'.format(sen, cos, tan))


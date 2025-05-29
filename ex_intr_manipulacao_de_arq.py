def converterByteParaMb(tamanhoEmByte: int) -> float:
  return round(float(tamanhoEmByte / (1024 * 1024)), 2)

def calcularPercentual(tamanhoArquivo: float, tamanhoTotal: float) -> float:
  return round(float((tamanhoArquivo / tamanhoTotal) * 100), 2)

def escreverArquivo(matriz) -> None:
  with open('usuarioFinal.txt', 'w') as f:
    f.write('Nr. Usuario  Espaço utilizado  % do uso\n')
    f.write('--- -------- ----------------- --------\n') # Linha para separar o cabeçalho dos dados
    for usuario in matriz:
      # Define a largura de cada coluna usando f-strings e especificadores de formato
      f.write(f'{usuario[0]:<4} {usuario[1]:<9} {usuario[2]} MB      {usuario[3]}%\n')
    

with open('usuario.txt', 'r') as f:
  usuarios = f.read()

tamanho_total = 0
dados_usuario = []
matriz = []
n = 1

for usuario in usuarios.split('\n'):
  usuario = usuario.split(',')
  dados_usuario.append(n)
  dados_usuario.append(usuario[0])
  dados_usuario.append(converterByteParaMb(int(usuario[1])))
  tamanho_total += int(usuario[1])
  n += 1
  matriz.append(dados_usuario)
  dados_usuario = []

#print(tamanho_total)
tamanho_total = converterByteParaMb(tamanho_total)
for usuario in matriz:
  usuario.append(calcularPercentual(usuario[2], tamanho_total))

escreverArquivo(matriz)

with open('usuarioFinal.txt', 'r') as f:
  print(f.read())

import regex as re

V_A = '([áéíóú])'
V = '(?i)([aeiouáéíóúü]|y$)'
V_S_A = '([aeiou])'
V_abierta = '(?i)([aeoáéó])'
V_cerrada = '(?i)([iíuúü$y])'
C1 = '(?i)(ch|ll|rr|[bcdfgjklmnñpqrstvwxz])'
C2 = '(?i)([bcdfgjklmnñpqrstvwxz])'
R1 = f'(?i)(?P<S1>{V})(?P<S2>{C1}{V})'
R2a = f'(?i)(?P<S1>{V})(?P<S2>[pcbgf][rl]{V})'
R2b = f'(?i)(?P<S1>{V})(?P<S2>[dt][r]{V})'
R2c = f'(?i)(?P<S1>{V}{C1})(?P<S2>{C1}{V})'
R3a = f'(?i)(?P<S1>{V}{C1})(?P<S2>([pcbgf][rl]|[dt][r]){V})'
R3b = f'(?i)(?P<S1>{V}[bdnmlr][s])(?P<S2>{C1}{V})'
R3c = f'(?i)(?P<S1>{V}[s][t])(?P<S2>{C1}{V})'
R4 = f'(?i)(?P<S1>{V}([s][t]|[bdnmlr][s]))(?P<S2>[pcbgf][rl]{V})'
R5b = (f'(?i)((?P<S1>[aeo])(?P<S2>[íú])|(?P<S1>[íú])(?P<S2>[aeo])|(?P<S1>[a])(?P<S2>[á])|(?P<S1>[á])(?P<S2>[a])|'
       f'(?P<S1>[a])(?P<S2>[a])|(?P<S1>[e])(?P<S2>[é])|(?P<S1>[é])(?P<S2>[e])|(?P<S1>[e])(?P<S2>[e])|(?P<S1>[i])'
       f'(?P<S2>[í])|(?P<S1>[i])(?P<S2>[i])|(?P<S1>[í])(?P<S2>[i])|(?P<S1>[o])(?P<S2>[ó])|(?P<S1>[ó])(?P<S2>[o])|'
       f'(?P<S1>[o])(?P<S2>[o])|(?P<S1>[u])(?P<S2>[ú])|(?P<S1>[u])(?P<S2>[u])|(?P<S1>[ú])(?P<S2>[u])|(?P<S1>[áa])'
       f'(?P<S2>[e])|(?P<S1>[a])(?P<S2>[eé])|(?P<S1>[ée])(?P<S2>[a])|(?P<S1>[e])(?P<S2>[áa])|(?P<S1>[áa])(?P<S2>[o])'
       f'|(?P<S1>[a])(?P<S2>[óo])|(?P<S1>[oó])(?P<S2>[a])|(?P<S1>[o])(?P<S2>[áa])|(?P<S1>[eé])(?P<S2>[o])|(?P<S1>[e])'
       f'(?P<S2>[oó])|(?P<S1>[oó])(?P<S2>[e])|(?P<S1>[o])(?P<S2>[eé]))')
R5c = (f'(?i)((?P<S1>[aeo])(?P<S2>[h][íú])|(?P<S1>[íú])(?P<S2>[h][aeo])|(?P<S1>[a])(?P<S2>[h][á])|(?P<S1>[á])'
       f'(?P<S2>[h][a])|(?P<S1>[a])(?P<S2>[h][a])|(?P<S1>[e])(?P<S2>[h][é])|(?P<S1>[é])(?P<S2>[h][e])|(?P<S1>[e])'
       f'(?P<S2>[h][e])|(?P<S1>[i])(?P<S2>[h][í])|(?P<S1>[i])(?P<S2>[h][i])|(?P<S1>[í])(?P<S2>[h][i])|(?P<S1>[o])'
       f'(?P<S2>[h][ó])|(?P<S1>[ó])(?P<S2>[h][o])|(?P<S1>[o])(?P<S2>[h][o])|(?P<S1>[u])(?P<S2>[h][ú])|(?P<S1>[u])'
       f'(?P<S2>[h][u])|(?P<S1>[ú])(?P<S2>[h][u])|(?P<S1>[áa])(?P<S2>[h][e])|(?P<S1>[a])(?P<S2>[h][eé])|(?P<S1>[ée])'
       f'(?P<S2>[h][a])|(?P<S1>[e])(?P<S2>[h][áa])|(?P<S1>[áa])(?P<S2>[h][o])|(?P<S1>[a])(?P<S2>[h][óo])|(?P<S1>[oó])'
       f'(?P<S2>[h][a])|(?P<S1>[o])(?P<S2>[h][áa])|(?P<S1>[eé])(?P<S2>[h][o])|(?P<S1>[e])(?P<S2>[h][oó])|(?P<S1>[oó])'
       f'(?P<S2>[h][e])|(?P<S1>[o])(?P<S2>[h][eé]))')
R5a = f'[aeoáéó][iuy$]|[iu][aeoáéó]|[aeoáéó][h][iu$y]|[iu][h][aeoáéó]'
R5a_cerradas = f'[ií][u]|[i][úu]|[úuü][iy$]|[uü][íiy$]|[ií][h][u]|[i][h][úu]|[úuü][h][iy$]|[uü][h][íiy$]'
R6 = f'([iuü][aeoáéó][iuy$])'
FIN = '([aeiousn])'
er = re.compile(
    R1 + '|' + R2a + '|' + R2b + '|' + R2c + '|' + R3a + '|' + R3b + '|' + R3c + '|' + R4 + '|' + R5b + '|' + R5c)

vocales_acentuadas = re.compile(V_A)
vocal_abierta = re.compile(V_abierta)
vocal_cerrada = re.compile(V_cerrada)
consonantes_todas = re.compile(C1)
letra_final_aguda = re.compile(FIN)
vocal_sin_acentuar = re.compile(V_S_A)
diptongo_abierto = re.compile(R5a)
diptongo_cerrado = re.compile(R5a_cerradas)
triptongo = re.compile(R6)

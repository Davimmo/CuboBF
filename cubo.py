import numpy as np
import kociemba

rotate_x=np.array([
    [1, 0, 0],
    [0, 0, -1],
    [0, 1, 0]
    ])

rotate_y=np.array([
    [ 0,  0, -1],
    [ 0,  1,  0],
    [ 1,  0,  0]
])

rotate_z=np.array([
    [0, -1, 0],
    [1, 0, 0],
    [0, 0, 1]
])

class Cubinho:
    def __init__(self,coordenada,adesivos,tipo_de_peça):
        self.coordenada=coordenada
        self.adesivos=adesivos
        self.tipo_de_peça=tipo_de_peça

class Cubo:
    def __init__(self):
        self.estado_inicial=[]
        self.lista_de_cubinhos=[]
        self.coordenadas=[]
        for z in range(-1,2):
            for y in range(-1,2):
                for x in range(-1,2):
                    self.coordenadas.append(np.array([x,y,z]))
        
        for item in self.coordenadas:
            tipo_de_peça=None
            adesivos={}
            x=item[0]
            y=item[1]
            z=item[2]

            if x==1:
                adesivos['azul']=np.array([1,0,0])
            if x==-1:
                adesivos['verde']=np.array([-1,0,0])
            if y==1:
                adesivos['vermelho']=np.array([0,1,0])
            if y==-1:
                adesivos['laranja']=np.array([0,-1,0])
            if z==1:
                adesivos['amarelo']=np.array([0,0,1])
            if z==-1:
                adesivos['branco']=np.array([0,0,-1])
            
            if len(adesivos)==2:
                tipo_de_peça='meio'
            if len(adesivos)==3:
                tipo_de_peça='quina'
            if len(adesivos)==1:
                tipo_de_peça='centro'
            if len(adesivos)==0:
                tipo_de_peça='nucleo'

            self.lista_de_cubinhos.append(Cubinho(item,adesivos,tipo_de_peça))
            self.estado_inicial.append(Cubinho(item,adesivos,tipo_de_peça))

        self.ladoR=[x for x in self.lista_de_cubinhos if x.coordenada[0]==1]
        self.ladoL=[x for x in self.lista_de_cubinhos if x.coordenada[0]==-1]
        self.ladoB=[x for x in self.lista_de_cubinhos if x.coordenada[1]==1]
        self.ladoF=[x for x in self.lista_de_cubinhos if x.coordenada[1]==-1]
        self.ladoU=[x for x in self.lista_de_cubinhos if x.coordenada[2]==1]
        self.ladoD=[x for x in self.lista_de_cubinhos if x.coordenada[2]==-1]
        self.ladoM=[x for x in self.lista_de_cubinhos if x.coordenada[0]==0]
        self.ladoS=[x for x in self.lista_de_cubinhos if x.coordenada[1]==0]
        self.ladoE=[x for x in self.lista_de_cubinhos if x.coordenada [2]==0]

        self.ladoRw=[x for x in self.lista_de_cubinhos if x.coordenada[0]>=0]
        self.ladoLw=[x for x in self.lista_de_cubinhos if x.coordenada[0]<=0]
        self.ladoBw=[x for x in self.lista_de_cubinhos if x.coordenada[1]>=0]
        self.ladoFw=[x for x in self.lista_de_cubinhos if x.coordenada[1]<=0]
        self.ladoUw=[x for x in self.lista_de_cubinhos if x.coordenada[2]>=0]
        self.ladoDw=[x for x in self.lista_de_cubinhos if x.coordenada[2]<=0]

    #Atualiza os lados dos cubos depois de realizar as rotações nas peças (cubinhos)
    def refresh(self):
        self.ladoR=[x for x in self.lista_de_cubinhos if x.coordenada[0]==1]
        self.ladoL=[x for x in self.lista_de_cubinhos if x.coordenada[0]==-1]
        self.ladoB=[x for x in self.lista_de_cubinhos if x.coordenada[1]==1]
        self.ladoF=[x for x in self.lista_de_cubinhos if x.coordenada[1]==-1]
        self.ladoU=[x for x in self.lista_de_cubinhos if x.coordenada[2]==1]
        self.ladoD=[x for x in self.lista_de_cubinhos if x.coordenada[2]==-1]
        self.ladoM=[x for x in self.lista_de_cubinhos if x.coordenada[0]==0]
        self.ladoS=[x for x in self.lista_de_cubinhos if x.coordenada[1]==0]
        self.ladoE=[x for x in self.lista_de_cubinhos if x.coordenada [2]==0]

        self.ladoRw=[x for x in self.lista_de_cubinhos if x.coordenada[0]>=0]
        self.ladoLw=[x for x in self.lista_de_cubinhos if x.coordenada[0]<=0]
        self.ladoBw=[x for x in self.lista_de_cubinhos if x.coordenada[1]>=0]
        self.ladoFw=[x for x in self.lista_de_cubinhos if x.coordenada[1]<=0]
        self.ladoUw=[x for x in self.lista_de_cubinhos if x.coordenada[2]>=0]
        self.ladoDw=[x for x in self.lista_de_cubinhos if x.coordenada[2]<=0] 


    def show(self,lado):
        for peça in lado:
            print(f'coordenada:{peça.coordenada}',end=', ')
            for adesivo in peça.adesivos:
                print(f'{adesivo}:{peça.adesivos[adesivo]}',end=' ')
            print()
        print('-'*100)

    def rotate(self, lado, matriz):
        #Aqui eu descobri a duras penas que mudar a ordem entre a matriz e o vetor faz TOTAL diferença,
        #por isso prestem MUITA atenção nas aulas de algebra linear galera
        #No caso eu estou usando as matrizes de rotação trânspostas porque meu vetor é de linha e não coluna

        for cubinho in lado:
            # Atualiza a coordenada do cubinho
            cubinho.coordenada = np.dot(cubinho.coordenada, matriz)
            
            # Atualiza os adesivos do cubinho
            for k in cubinho.adesivos:  # Use list() para evitar modificações durante a iteração
                cubinho.adesivos[k] = np.dot(cubinho.adesivos[k], matriz)


#Funções de rotação dos lados e centros do cubo

    def R(self):
        self.rotate(self.ladoR,rotate_x)
        self.refresh()
    def R_(self):
        self.rotate(self.ladoR,np.transpose(rotate_x))
        self.refresh()
    def L(self):
        self.rotate(self.ladoL,np.transpose(rotate_x))
        self.refresh()
    def L_(self):
        self.rotate(self.ladoL,rotate_x)
        self.refresh()
    def F(self):
        self.rotate(self.ladoF,rotate_y)
        self.refresh()
    def F_(self):
        self.rotate(self.ladoF,np.transpose(rotate_y))
        self.refresh()
    def B(self):
        self.rotate(self.ladoB,np.transpose(rotate_y))
        self.refresh()
    def B_(self):
        self.rotate(self.ladoB,rotate_y)
        self.refresh()
    def U(self):
        self.rotate(self.ladoU,rotate_z)  
        self.refresh()
    def U_(self):
        self.rotate(self.ladoU,np.transpose(rotate_z))
        self.refresh()
    def D(self):
        self.rotate(self.ladoD,np.transpose(rotate_z))
        self.refresh()
    def D_(self):
        self.rotate(self.ladoD,rotate_z)
        self.refresh()

    #Movimentos dos centros

    def M(self):
        self.rotate(self.ladoM,np.transpose(rotate_x))
        self.refresh()
    def M_(self):
        self.rotate(self.ladoM,rotate_x)
        self.refresh()
    def S(self):
        self.rotate(self.ladoS,rotate_y)
        self.refresh()
    def S_(self):
        self.rotate(self.ladoS,np.transpose(rotate_y))
        self.refresh()
    def E(self):
        self.rotate(self.ladoE,rotate_z)
        self.refresh()
    def E_(self):
        self.rotate(self.ladoE,np.transpose(rotate_z))
        self.refresh()

    #Movimentos duplos

    def D2(self):
        self.D()
        self.D()
    def U2(self):
        self.U()
        self.U()
    def B2(self):
        self.B()
        self.B()
    def F2(self):
        self.F()
        self.F()
    def L2(self):
        self.L()
        self.L()
    def R2(self):
        self.R()
        self.R()

    
    #Duplos dos centros
    def M2(self):
        self.M()
        self.M()
    def S2(self):
        self.S()
        self.S()
    def E2(self):
        self.E()
        self.E()

    #Movimentos dupla camada

    def Rw(self):
        self.rotate(self.ladoRw,rotate_x)
        self.refresh()
    def Rw_(self):
        self.rotate(self.ladoRw,np.transpose(rotate_x))
        self.refresh()
    def Lw(self):
        self.rotate(self.ladoLw,np.transpose(rotate_x))
        self.refresh()
    def Lw_(self):
        self.rotate(self.ladoLw,rotate_x)
        self.refresh()
    def Fw(self):
        self.rotate(self.ladoFw,rotate_y)
        self.refresh()
    def Fw_(self):
        self.rotate(self.ladoFw,np.transpose(rotate_y))
        self.refresh()
    def Bw(self):
        self.rotate(self.ladoBw,np.transpose(rotate_y))
        self.refresh()
    def Bw_(self):
        self.rotate(self.ladoBw,rotate_y)
        self.refresh()
    def Uw(self):
        self.rotate(self.ladoUw,rotate_z)
        self.refresh()
    def Uw_(self):
        self.rotate(self.ladoUw,np.transpose(rotate_z))
        self.refresh()
    def Dw(self):
        self.rotate(self.ladoDw,np.transpose(rotate_z))
        self.refresh()
    def Dw_(self):
        self.rotate(self.ladoDw,rotate_z)
        self.refresh()
    
    #Movimentos duplos dupla camada
     
    def Rw2(self):
        self.Rw()
        self.Rw()
    def Lw2(self):
        self.Lw()
        self.Lw()
    def Fw2(self):
        self.Fw()
        self.Fw()
    def Bw2(self):
        self.Bw()
        self.Bw()
    def Uw2(self):
        self.Uw()
        self.Uw()
    def Dw2(self):
        self.Dw()
        self.Dw()

    def X(self):
        self.rotate(self.lista_de_cubinhos,rotate_x)
        self.refresh()

    def X_(self):
        self.rotate(self.lista_de_cubinhos,np.transpose(rotate_x))
        self.refresh()

    def Y(self):
        self.rotate(self.lista_de_cubinhos,rotate_y)
        self.refresh()
    def Y_(self):
        self.rotate(self.lista_de_cubinhos,np.transpose(rotate_y))
        self.refresh()

    def Z(self):
        self.rotate(self.lista_de_cubinhos,rotate_z)
        self.refresh()

    def Z_(self):
        self.rotate(self.lista_de_cubinhos,np.transpose(rotate_z))
        self.refresh()

    def esta_resolvido(self):
        for i, j in zip(self.lista_de_cubinhos, self.estado_inicial):
            if not (np.array_equal(i.coordenada, j.coordenada) and i.adesivos == j.adesivos):
                return False             
        return True

    
    def meios_corretos(self):
        zipada=zip(self.lista_de_cubinhos,self.estado_inicial)
        for i,j in zipada:
            if (i.tipo_de_peça=='meio' and j.tipo_de_peça=='meio'):
                if (not(np.array_equal(i.coordenada,j.coordenada)) or i.adesivos!=j.adesivos):
                    return False
        return True
    
    def quinas_corretas(self):
        zipada=zip(self.lista_de_cubinhos,self.estado_inicial)
        for i,j in zipada:
            if i.tipo_de_peça=='quina' and j.tipo_de_peça=='quina':
                if (not(np.array_equal(i.coordenada,j.coordenada)) or i.adesivos!=j.adesivos):
                    return False
        return True
    
    def executar_comandos(self,string_comando=None):

        comandos_dict={
            "R":self.R,
            "R'":self.R_,
            "L":self.L,
            "L'": self.L_,
            "F":self.F,
            "F'":self.F_,
            "B":self.B,
            "B'":self.B_,
            "U":self.U,
            "U'":self.U_,
            "D":self.D,
            "D'":self.D_,

            "M":self.M,
            "M'":self.M_,
            "S":self.S,
            "S'":self.S_,
            "E":self.E,
            "E'":self.E_,

            "R2":self.R2,
            "L2":self.L2,
            "F2":self.F2,
            "B2":self.B2,
            "U2":self.U2,
            "D2":self.D2,

            "M2":self.M2,
            "S2":self.S2,
            "E2":self.E2,

            "RW":self.Rw,
            "RW'":self.Rw_,
            "LW":self.Lw,
            "LW'":self.Lw_,
            "FW":self.Fw,
            "FW'":self.Fw_,
            "BW":self.Bw,
            "BW'":self.Bw_,
            "UW":self.Uw,
            "UW'":self.Uw_,
            "DW":self.Dw,
            "DW'":self.Dw_,

            "RW2":self.Rw2,
            "LW2":self.Lw2,
            "FW2":self.Fw2,
            "BW2":self.Bw2,
            "UW2":self.Uw2,
            "DW2":self.Dw2,

            "X":self.X,
            "Y":self.Y,
            "Z":self.Z,

            "X'":self.X_,
            "Y'":self.Y_,
            "Z'":self.Z_
            }

        if string_comando is not None:
            string_comando=string_comando.upper()
            lista_comandos=string_comando.split()
            print(" ".join(lista_comandos))
            for comando in lista_comandos:
                comandos_dict[comando]()

        else:
            string_comando=input("Digite os movimentos separados por espaços")
            string_comando=string_comando.upper()
            lista_comandos=string_comando.split()
            print(" ".join(lista_comandos))
            for comando in lista_comandos:
                comandos_dict[comando]()

    def reverter_notação(self,sequência: str):
        sequência=sequência.upper()
        sequência=sequência.split()
        sequência=sequência[::-1]
        nova_string=[]
        correspondência={
            "R":"R'",
            "R'":"R",
            "L":"L'",
            "L'":"L",
            "U":"U'",
            "U'":"U",
            "F":"F'",
            "F'":"F",
            "B":"B'",
            "B'":"B",
            "D":"D'",
            "D'":"D",

            "M":"M'",
            "M'":"M",
            "S":"S'",
            "S'":"S",
            "E":"E'",
            "E'":"E",

            "R2":"R2",
            "L2":"L2",
            "F2":"F2",
            "U2":"U2",
            "D2":"D2",
            "M2":"M2",
            "S2":"S2",

            "RW":"RW'",
            "RW'":"RW",
            "LW":"LW'",
            "LW'":"LW",
            "FW":"FW'",
            "FW'":"FW",
            "BW":"BW'",
            "BW'":"BW",
            "DW":"DW'",
            "DW'":"DW",

            "RW2":"RW2",
            "LW2":"LW2",
            "FW2":"FW2",
            "BW2":"BW2",
            "UW2":"UW2",
            "DW2":"DW2",

            "X":"X'",
            "X'":"X",
            "Y":"Y'",
            "Y'":"Y",
            "Z":"Z'",
            "Z'":"Z"
        }
        for letra in sequência:
            nova_string.append(correspondência[letra])
        
        nova_string=" ".join(nova_string)
        return str(nova_string)

    def encontrar_cor_na_direcao(self,lista, coordenada_procurada, direcao):
        # Percorre todos os cubinhos na lista
        for cubinho in lista:
            # Verifica se a coordenada do cubinho é a coordenada procurada
            if np.array_equal(cubinho.coordenada, np.array(coordenada_procurada)):
                # Percorre os adesivos (cores) do cubinho
                for cor, direcao_adesivo in cubinho.adesivos.items():
                    # Verifica se a direção do adesivo é a direção procurada
                    if np.array_equal(direcao_adesivo, direcao):
                        return cor  # Retorna a cor que está nessa direção
        return None  # Retorna None se não encontrar nenhum cubinho na coordenada ou sem cor na direção
    
    def string_kociemba(self):
        #preciso ajustar para caso a orientação seja alterada
        dicionario_cores={
            'amarelo':'U',
            'azul':'R',
            'laranja':'F',
            'branco':'D',
            'verde':'L',
            'vermelho':'B'
        }
        cubo_string=""
        ordem_kociemba_U=[
        #TOPO ou U
        [-1,1,1],
        [0,1,1],
        [1,1,1],
        [-1,0,1],
        [0,0,1],
        [1,0,1],
        [-1,-1,1],
        [0,-1,1],
        [1,-1,1]
        ]
        ordem_kociemba_R=[
        #DIREITA ou R
        [1,-1,1],
        [1,0,1],
        [1,1,1],
        [1,-1,0],
        [1,0,0],
        [1,1,0],
        [1,-1,-1],
        [1,0,-1],
        [1,1,-1]
        ]
        ordem_kociemba_F=[
        #FRENTE ou F
        [-1,-1,1],
        [0,-1,1],
        [1,-1,1],
        [-1,-1,0],
        [0,-1,0],
        [1,-1,0],
        [-1,-1,-1],
        [0,-1,-1],
        [1,-1,-1]
        ]
        ordem_kociemba_D=[
        #BAIXO ou D
        [-1,-1,-1],
        [0,-1,-1],
        [1,-1,-1],
        [-1,0,-1],
        [0,0,-1],
        [1,0,-1],
        [-1,1,-1],
        [0,1,-1],
        [1,1,-1]
        ]
        ordem_kociemba_L=[
        #ESQUERDA ou L
        [-1,1,1],
        [-1,0,1],
        [-1,-1,1],
        [-1,1,0],
        [-1,0,0],
        [-1,-1,0],
        [-1,1,-1],
        [-1,0,-1],
        [-1,-1,-1]
        ]
        #TRASEIRA ou B
        ordem_kociemba_B=[
        [1,1,1],
        [0,1,1],
        [-1,1,1],
        [1,1,0],
        [0,1,0],
        [-1,1,0],
        [1,1,-1],
        [0,1,-1],
        [-1,1,-1]
        ]

        for coordenada in ordem_kociemba_U:
            cor=self.encontrar_cor_na_direcao(self.ladoU,coordenada,np.array([0,0,1]))
            cubo_string+=dicionario_cores[cor]

        for coordenada in ordem_kociemba_R:
            cor=self.encontrar_cor_na_direcao(self.ladoR,coordenada,np.array([1,0,0]))
            cubo_string+=dicionario_cores[cor]

        for coordenada in ordem_kociemba_F:
            cor=self.encontrar_cor_na_direcao(self.ladoF,coordenada,np.array([0,-1,0]))
            cubo_string+=dicionario_cores[cor]

        for coordenada in ordem_kociemba_D:
            cor=self.encontrar_cor_na_direcao(self.ladoD,coordenada,np.array([0,0,-1]))
            cubo_string+=dicionario_cores[cor]

        for coordenada in ordem_kociemba_L:
            cor=self.encontrar_cor_na_direcao(self.ladoL,coordenada,np.array([-1,0,0]))
            cubo_string+=dicionario_cores[cor]

        for coordenada in ordem_kociemba_B:
            cor=self.encontrar_cor_na_direcao(self.ladoB,coordenada,np.array([0,1,0]))
            cubo_string+=dicionario_cores[cor]
        
        return cubo_string

        
class Bf:
    def __init__(self):
        self.cubo=Cubo()
        self.T_perm="R U R' U' R' F R2 U' R' U' R U R' F'"
        
    def A(self):
        casoA="Lw2 D' L2"
        self.cubo.executar_comandos(f'{casoA} {self.T_perm} {self.cubo.reverter_notação(casoA)}')
    def B(self):
        print("Você provavelmente cometeu um erro no B")
    def C(self):
        casoC=" Lw2 D L2"
        self.cubo.executar_comandos(f'{casoC} {self.T_perm} {self.cubo.reverter_notação(casoC)}')
    def D(self):
        self.cubo.executar_comandos(f'{self.T_perm}')
    def E(self):
        casoE="L' Dw L'"
        self.cubo.executar_comandos(f'{casoE} {self.T_perm} {self.cubo.reverter_notação(casoE)}')
    def F(self):
        casoF="Dw' L"
        self.cubo.executar_comandos(f'{casoF} {self.T_perm} {self.cubo.reverter_notação(casoF)}')
    def G(self):
        casoG="L Dw L'"
        self.cubo.executar_comandos(f'{casoG} {self.T_perm} {self.cubo.reverter_notação(casoG)}')
    def H(self):
        casoH="Dw L'"
        self.cubo.executar_comandos(f'{casoH} {self.T_perm} {self.cubo.reverter_notação(casoH)}')
    def I(self):
        casoI="Lw D' L2"
        self.cubo.executar_comandos(f'{casoI} {self.T_perm} {self.cubo.reverter_notação(casoI)}')
    def J(self):
        casoJ="Dw2 L"
        self.cubo.executar_comandos(f'{casoJ} {self.T_perm} {self.cubo.reverter_notação(casoJ)}')
    def K(self):
        casoK="Lw D L2"
        self.cubo.executar_comandos(f'{casoK} {self.T_perm} {self.cubo.reverter_notação(casoK)}')
    def L(self):
        casoL="L'"
        self.cubo.executar_comandos(f'{casoL} {self.T_perm} {self.cubo.reverter_notação(casoL)}')
    def M(self):
        print("Você provavelmente cometeu um erro no M")
    def N(self):
        casoN="Dw L"
        self.cubo.executar_comandos(f'{casoN} {self.T_perm} {self.cubo.reverter_notação(casoN)}')
    def O(self):
        casoO="D' Lw D L2"
        self.cubo.executar_comandos(f'{casoO}  {self.T_perm} {self.cubo.reverter_notação(casoO)}')
    def P(self):
        casoP="Dw' L'"
        self.cubo.executar_comandos(f'{casoP} {self.T_perm} {self.cubo.reverter_notação(casoP)}')
    def Q(self):
        casoQ="Lw' D L2"
        self.cubo.executar_comandos(f'{casoQ} {self.T_perm} {self.cubo.reverter_notação(casoQ)}')
    def R(self):
        casoR="L"
        self.cubo.executar_comandos(f'{casoR} {self.T_perm} {self.cubo.reverter_notação(casoR)}')
    def S(self):
        casoS="Lw' D' L2"
        self.cubo.executar_comandos(f'{casoS} {self.T_perm} {self.cubo.reverter_notação(casoS)}')            
    def T(self):
        casoT="Dw2 L'"
        self.cubo.executar_comandos(f'{casoT} {self.T_perm} {self.cubo.reverter_notação(casoT)}')
    def U(self):
        casoU="D' L2"
        self.cubo.executar_comandos(f'{casoU} {self.T_perm} {self.cubo.reverter_notação(casoU)}')
    def V(self):
        casoV="D2 L2"
        self.cubo.executar_comandos(f'{casoV} {self.T_perm} {self.cubo.reverter_notação(casoV)}')
    def W(self):
        casoW="D L2"
        self.cubo.executar_comandos(f'{casoW} {self.T_perm} {self.cubo.reverter_notação(casoW)}')
    def X(self):
        casoX="L2"
        self.cubo.executar_comandos(f'{casoX} {self.T_perm} {self.cubo.reverter_notação(casoX)}')

    def executar_comandos(self,string_comando=None):
        comandos_dict={
            "A":self.A,
            "B":self.B,
            "C":self.C,
            "D":self.D,
            "E":self.E,
            "F":self.F,
            "G":self.G,
            "H":self.H,
            "I":self.I,
            "J":self.J,
            "K":self.K,
            "L":self.L,
            "M":self.M,
            "N":self.N,
            "O":self.O,
            "P":self.P,
            "Q":self.Q,
            "R":self.R,
            "S":self.S,
            "T":self.T,
            "U":self.U,
            "V":self.V,
            "W":self.W,
            "X":self.X
        }

        if string_comando is not None:
            string_comando=string_comando.upper()
            lista_comandos=string_comando.split()
            print(" ".join(lista_comandos))
            for comando in lista_comandos:
                comandos_dict[comando]()

        else:
            string_comando=input("Digite os movimentos separados por espaços")
            string_comando=string_comando.upper()
            lista_comandos=string_comando.split()
            print(" ".join(lista_comandos))
            for comando in lista_comandos:
                comandos_dict[comando]()
    
#U R F D L B
c1=Bf()
c1.cubo.executar_comandos("R' F2 D R2 B D2 R' F2 D' L B2 U2 R F2 U2 R B' D' L F' D' L F2 D2 L".replace("’","'"))
c1.executar_comandos('D L T O H I P F U X A S U')
print(c1.cubo.meios_corretos())


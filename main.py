from cliente import Cliente
from ponto_entrega import Ponto_entrega
from pedido import Pedido
from veiculo import Veiculo
from rota import Rota
from otimizador_rotas import OtimizadorRotas

def menu_principal():
    c1 = Cliente("João", "1")
    lista_clientes = [c1]
    v1 = Veiculo("Fiat Uno", 200.0)
    lista_veiculos = [v1]
    
    lista_rotas = []
    ponto_A = Ponto_entrega(2, 3)   
    ponto_B = Ponto_entrega(10, 0)  
    ponto_C = Ponto_entrega(6, 8)
    lista_pedidos_soltos = [
        Pedido("P001", c1, ponto_A, 30.0),
        Pedido("P002", c1, ponto_B, 50.0),
        Pedido("P003", c1, ponto_C, 60.0)
    ]
    lista_rotas_ativas = []
    
    otimizador = OtimizadorRotas()

    while True:
        print("\n================ SYSTEMA DE ROTAS ================")
        print("1 - Menu Clientes")
        print("2 - Menu Veículos")
        print("3 - Menu Pedidos")
        print("4 - Menu Rotas (Otimização)")
        print("0 - Sair do Sistema")
        print("==================================================")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            while True:
                print("\n------------------ CLIENTE ------------------")
                print("1. Criar cliente")
                print("2. Excluir cliente")
                print("3. Listar clientes")
                print("4. Voltar")
                print("---------------------------------------------")
                op_cli = input("Opção: ").strip()

                if op_cli == "1":
                    nome = input("Nome do cliente: ").strip()
                    id_cli = input("ID do cliente: ").strip()
                    if nome and id_cli:
                        lista_clientes.append(Cliente(nome, id_cli))
                        print(f"Cliente {nome} cadastrado com sucesso!")
                    else:
                        print("Erro: Nome e ID não podem ser vazios.")

                elif op_cli == "2":
                    id_busca = input("Digite o ID do cliente a excluir: ").strip()
                    encontrado = False
                    for c in lista_clientes:
                        if c.id == id_busca:
                            lista_clientes.remove(c)
                            print("Cliente removido com sucesso!")
                            encontrado = True
                            break
                    if not encontrado:
                        print("Cliente não encontrado.")

                elif op_cli == "3":
                    print("\n[Lista de Clientes]")
                    if not lista_clientes:
                        print("Nenhum cliente cadastrado.")
                    for c in lista_clientes:
                        print(c)

                elif op_cli == "4":
                    break

        elif opcao == "2":
            while True:
                print("\n------------------ VEÍCULO ------------------")
                print("1. Criar veículo")
                print("2. Excluir veículo")
                print("3. Listar veículos")
                print("4. Voltar")
                print("---------------------------------------------")
                op_vei = input("Opção: ").strip()

                if op_vei == "1":
                    modelo = input("Modelo do veículo: ").strip()
                    try:
                        carga_max = float(input("Carga máxima (kg): ").strip())
                        if modelo and carga_max > 0:
                            lista_veiculos.append(Veiculo(modelo, carga_max))
                            print(f"Veículo {modelo} cadastrado com sucesso!")
                        else:
                            print("Dados inválidos.")
                    except ValueError:
                        print("Erro: Carga máxima deve ser um número.")

                elif op_vei == "2":
                    mod_busca = input("Digite o modelo do veículo a excluir: ").strip()
                    encontrado = False
                    for v in lista_veiculos:
                        if v.modelo == mod_busca:
                            lista_veiculos.remove(v)
                            print("Veículo removido com sucesso!")
                            encontrado = True
                            break
                    if not encontrado:
                        print("Veículo não encontrado.")

                elif op_vei == "3":
                    print("\n[Lista de Veículos]")
                    if not lista_veiculos:
                        print("Nenhum veículo cadastrado.")
                    for v in lista_veiculos:
                        print(v)

                elif op_vei == "4":
                    break

        elif opcao == "3":
            while True:
                print("\n------------------ PEDIDO ------------------")
                print("1. Criar pedido")
                print("2. Excluir pedido")
                print("3. Listar pedidos")
                print("4. Voltar")
                print("--------------------------------------------")
                op_ped = input("Opção: ").strip()

                if op_ped == "1":
                    if not lista_clientes:
                        print("Erro: Cadastre pelo menos um cliente antes de criar um pedido.")
                        continue
                    
                    nome_ped = input("Nome/Código do pedido: ").strip()
                    
                    print("Clientes disponíveis:")
                    for idx, c in enumerate(lista_clientes):
                        print(f"[{idx}] {c.nome}")
                    try:
                        idx_cli = int(input("Escolha o número do cliente: "))
                        cliente_escolhido = lista_clientes[idx_cli]
                        
                        print("Informe o ponto de entrega:")
                        x = int(input("Coordenada X: "))
                        y = int(input("Coordenada Y: "))
                        ponto_entrega = Ponto_entrega(x, y)
                        
                        peso = float(input("Peso da encomenda (kg): "))
                        
                        novo_pedido = Pedido(nome_ped, cliente_escolhido, ponto_entrega, peso)
                        lista_pedidos_soltos.append(novo_pedido)
                        print(f"Pedido {nome_ped} criado com sucesso!")
                    except (ValueError, IndexError):
                        print("Erro: Entrada inválida. Pedido não foi criado.")

                elif op_ped == "2":
                    nome_busca = input("Digite o nome do pedido a excluir: ").strip()
                    encontrado = False
                    for p in lista_pedidos_soltos:
                        if p.nome == nome_busca:
                            lista_pedidos_soltos.remove(p)
                            print("Pedido excluído com sucesso!")
                            encontrado = True
                            break
                    if not encontrado:
                        print("Pedido não encontrado.")

                elif op_ped == "3":
                    print("\n[Lista de Pedidos]")
                    if not lista_pedidos_soltos:
                        print("Nenhum pedido cadastrado.")
                    for p in lista_pedidos_soltos:
                        print(p)

                elif op_ped == "4":
                    break

        elif opcao == "4":
            while True:
                print("\n------------------ GERENCIAR ROTAS ------------------")
                print("1. Criar Nova Rota (Vincular Motorista + Veículo)")
                print("2. Adicionar Pedidos a uma Rota Ativa")
                print("3. Otimizar e Rodar Análise de Rota")
                print("4. Listar todas as Rotas")
                print("5. Voltar")
                print("-----------------------------------------------------")
                op_rot = input("Opção: ").strip()

                if op_rot == "1":
                    if not lista_veiculos:
                        print("Cadastre um veículo primeiro!")
                        continue
                    
                    print("Selecione o veículo:")
                    for idx, v in enumerate(lista_veiculos):
                        print(f"[{idx}] {v.modelo}")
                    
                    try:
                        idx_v = int(input("Número do veículo: "))
                        v_escolhido = lista_veiculos[idx_v]
                        motorista = input("Nome do motorista: ").strip()
                        nova_rota = Rota([], v_escolhido, motorista)
                        lista_rotas_ativas.append(nova_rota)
                        print(f"Rota criada para {motorista} no {v_escolhido.modelo}!")
                    except (ValueError, IndexError):
                        print("Entrada inválida.")

                elif op_rot == "2":
                    # Pega um pedido do depósito e joga no caminhão
                    if not lista_rotas_ativas or not lista_pedidos_soltos:
                        print("Você precisa de rotas criadas e pedidos soltos no depósito!")
                        continue
                    
                    print("Selecione a Rota que deseja abastecer:")
                    for idx, r in enumerate(lista_rotas_ativas):
                        print(f"[{idx}] Motorista: {r.motorista} | Veículo: {r.veiculo.modelo}")
                    
                   
                    try:
                        idx_r = int(input("Número da rota: "))
                        rota_escolhida = lista_rotas_ativas[idx_r]
                        
                        print("\nPedidos disponíveis no depósito:")
                        for idx, p in enumerate(lista_pedidos_soltos):
                            print(f"[{idx}] {p.nome} ({p.peso_encomenda} kg)")
                        
                        idx_p = int(input("Número do pedido para adicionar: "))
                        pedido_escolhido = lista_pedidos_soltos[idx_p]
                        
                        
                        rota_escolhida.adicionar_pedido(pedido_escolhido)
                        lista_pedidos_soltos.remove(pedido_escolhido) 
                        print(f"Pedido {pedido_escolhido.nome} despachado para a triagem da rota.")
                        
                    except (ValueError, IndexError): # <--- O Pylance estava reclamando da falta disso aqui!
                        print("Erro: Entrada inválida ou seleção fora dos limites.")

                elif op_rot == "3":
                    if not lista_rotas_ativas:
                        print("Nenhuma rota ativa.")
                        continue
                        
                    print("Selecione a rota para rodar o algoritmo do vizinho mais próximo:")
                    for idx, r in enumerate(lista_rotas_ativas):
                        print(f"[{idx}] {r.motorista}")
                        
                    try:
                        idx_r = int(input("Número da rota: "))
                        rota_para_otimizar = lista_rotas_ativas[idx_r]
                        otimizador.processar_vizinho_proximo(rota_para_otimizar)
                        
                        print("\n================ ROTA OTIMIZADA ================")
                        print(rota_para_otimizar)
                        if otimizador.pedidos_nao_alocados:
                            print("\nPedidos Não Alocados (Capacidade Excedida):")
                            for ped in otimizador.pedidos_nao_alocados:
                                print(f"-> {ped.nome} - Peso: {ped.peso_encomenda} kg")
                        else:
                            print("\nPedidos Não Alocados: Nenhum! Todos os pedidos couberam.")

                        
                        print("================================================")
                    except (ValueError, IndexError):
                        print("Erro na seleção.")
                    
                
                elif op_rot == "4":
                    print("\n================ LISTA DE ROTAS ATIVAS ================")
                    if not lista_rotas_ativas:
                        print("Nenhuma rota criada no sistema até agora.")
                    for idx, r in enumerate(lista_rotas_ativas):
                        print(f"\n[ROTA ID: {idx}]")
                        print(r)
                    print("=======================================================")

                elif op_rot == "5":
                    break

        elif opcao == "0":
            print("Saindo do sistema... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
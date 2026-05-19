# Sistema de Otimização de Rotas de Entregas (Logística)

Este sistema foi desenvolvido como projeto prático para a disciplina de Programação Orientada a Objetos em Python. Ele utiliza o algoritmo do **Vizinho Mais Próximo** para otimizar sequências de entregas logísticas com base na proximidade geográfica (distância euclidiana), respeitando o limite de capacidade de carga dos veículos.

## 🛠️ Tecnologias e Conceitos Utilizados
- **Linguagem:** Python 3
- **Conceitos de POO:** Abstração, Encapsulamento (Getters/Setters), Composição e Polimorfismo (`__str__`).
- **Estruturas de Dados:** Listas e manipulação dinâmica de objetos na memória.
- **Robustez:** Tratamento de exceções (`try/except`) contra entradas inválidas.

## 📂 Estrutura do Projeto
```text
sistema_rotas/
│
├── main.py             # Painel de controle e menus interativos
├── cliente.py          # Classe Cliente (dados do comprador)
├── ponto_entrega.py    # Classe Ponto_entrega (coordenadas X, Y)
├── pedido.py           # Classe Pedido (composição de Cliente e Ponto)
├── veiculo.py          # Classe Veiculo (modelo e capacidade de carga)
├── rota.py             # Classe Rota (guarda o itinerário e motorista)
└── otimizador_rotas.py # Motor do algoritmo (Vizinho Mais Próximo)


🚀 Como Executar o Sistema
Abra o terminal na pasta raiz do projeto.

Execute o comando:

Bash
python main.py
O sistema já iniciará com dados de teste pré-carregados (Cliente João, Veículo Fiat Uno e 3 pedidos estratégicos no depósito) para facilitar a avaliação do algoritmo.

📦 Como Testar o Fluxo Completo
Digite 4 para entrar no menu Gerenciar Rotas.

Escolha a Opção 1 para criar uma rota, selecione o Fiat Uno e informe o nome do motorista.

Escolha a Opção 2 para adicionar pedidos a essa rota. Adicione os pedidos disponíveis.

Escolha a Opção 3 para rodar a otimização. O sistema aplicará o algoritmo, ordenará as paradas e exibirá o relatório final separando os pedidos que excederam a capacidade do veículo.
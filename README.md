# Longano

Sistema base para uma agência de seguros de vida, desenvolvido em Python com o framework Flet para interface desktop/web. O projeto foi pensado para facilitar o cadastro de clientes, apresentação de planos, geração e envio de contratos, além da integração com plataformas de pagamentos, comunicação e armazenamento de dados.

## Sobre o projeto

O Longano é uma aplicação para apoiar uma agência de seguros de vida em processos como:

- autenticação básica de usuários;
- seleção de planos e coberturas;
- cadastro de clientes e coleta de dados essenciais;
- geração e personalização de contratos;
- envio de documentos para assinatura digital;
- geração de cobrança e pagamento via API;
- envio de mensagens e notificações por WhatsApp;
- armazenamento de informações em banco de dados no Firebase.

A proposta da aplicação é centralizar essas etapas em uma interface simples e profissional, permitindo maior eficiência operacional para a equipe da agência.

## Tecnologias e ferramentas utilizadas

### Linguagens de programação

- Python
- JSON
- XML (para manipulação de documentos e templates)

### Framework

- Flet

### Plataformas e serviços integrados

- Asaas: processamento de cobranças e pagamentos;
- ClickSign: assinatura digital de contratos e documentos;
- AvisaAPI: envio de mensagens via WhatsApp;
- Firebase: armazenamento e persistência de dados do cliente e registros do processo.

### Bibliotecas principais

- `flet` — desenvolvimento da interface da aplicação;
- `requests` — consumo das APIs externas;
- `firebase-admin` — integração com Firebase;
- `holidays` — cálculo de vencimentos considerando feriados;
- `lxml` — manipulação de arquivos XML/documentos.

## Estrutura do projeto

- `main.py` — ponto de entrada da aplicação;
- `tela_login.py` — tela de autenticação;
- `pagina_produtos.py` — catálogo de planos/seguros;
- `cadastro_cliente.py` — fluxo de cadastro do cliente;
- `api_asaas.py` — integração com a API do Asaas;
- `clicksign.py` — integração com a API do ClickSign;
- `avisaapi.py` — integração com a API do AvisaAPI;
- `firebase.py` — conexão com Firebase;
- `contrato1.py` — manipulação e personalização do contrato;
- `assets/` — imagens, documentos e arquivos estáticos do app;
- `storage/` — armazenamento local e dados auxiliares.

## Fluxo principal da aplicação

1. O usuário acessa a tela de login.
2. A partir da tela inicial, o sistema apresenta os planos disponíveis.
3. Ao selecionar um plano, o usuário preenche os dados do cliente.
4. O sistema gera ou atualiza o contrato e envia o documento para assinatura digital.
5. O cliente é cadastrado na plataforma de pagamentos.
6. Uma cobrança é criada e o pagamento pode ser realizado via PIX ou outros meios.
7. O sistema envia notificações via WhatsApp.
8. As informações do cadastro são salvas no Firebase.

## Pré-requisitos

Antes de executar o projeto, verifique se você possui:

- Python 3.9 ou superior;
- pip ou outro gerenciador de dependências;
- acesso às APIs de Asaas, ClickSign e AvisaAPI;
- credenciais válidas do Firebase;
- ambiente local configurado para executar aplicações Flet.

## Execução

### Executar a aplicação desktop

```bash
python main.py
```

Ou, se preferir a execução com Flet diretamente:

```bash
flet run
```

### Executar em modo web

```bash
flet run --web
```

## Licença

Este projeto está sendo desenvolvido para fins educacionais e de negócio interno da base do sistema. Caso seja reutilizado em outros contextos, ajuste a licença conforme a necessidade do projeto.

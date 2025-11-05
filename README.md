# Importa Pedidos GeoSales → ERP (Python Integration)

Integração entre a API **GeoSales** e a API de destino (ERP/Datasul, etc), desenvolvida em **Python**, para automatizar a leitura e envio de pedidos.

---

## Estrutura do Projeto

```
Importa_Pedidos_GeoSales_Python/
├── src/
│   ├── api_origem_geosales.py     # Leitura da API GeoSales (GET)
│   ├── api_destino_erp.py         # Envio dos pedidos para o ERP (POST)
│   ├── config.py                  # URLs e tokens de ambiente
│   ├── main.py                    # Ponto de execução do processo
│   └── transform.py               # (opcional) Transformações de dados
├── .env                           # Variáveis de ambiente (não versionado)
├── requirements.txt               # Dependências do projeto
└── .gitignore                     # Ignora venv, cache e arquivos sensíveis
```

---

## Configuração do Ambiente

### 1 Clonar o repositório
```bash
git clone https://github.com/jardelsampaio/Importa_Pedidos_GeoSales_Python.git
cd Importa_Pedidos_GeoSales_Python
```

### 2️ Criar e ativar o ambiente virtual
```bash
python -m venv venv
.env\Scripts\Activate.ps1   # Windows PowerShell
```

### 3️ Instalar dependências
```bash
pip install -r requirements.txt
```

---

##  Arquivo `.env`

Crie um arquivo `.env` na raiz do projeto com suas credenciais e URLs:

```
# API GEO SALES
API_ORIGEM_URL=http://sav.geosales.com.br/erp-integrator/montanahomolog/sync/pedido/
API_ORIGEM_TOKEN=SEU_TOKEN_AQUI

# API ERP DESTINO
API_DESTINO_URL=https://georesttst.montana.com.br/dts/datasul-rest/resources/prg/rest/v1/apiPedido/pedido
API_DESTINO_USER=usuario
API_DESTINO_PASS=senha_aqui
```

> ⚠️ **Importante:** o arquivo `.env` está no `.gitignore`, então ele **não será enviado ao GitHub**.

---

## ▶️ Execução

Após configurar o `.env`:

```bash
python src/main.py
```

O programa:
1. Lê os pedidos e itens da **API GeoSales**
2. Agrupa por `cd_pedido_palm`
3. Envia os dados para a **API ERP destino**
4. Exibe logs de sucesso/erro no terminal

---

## 🧠 Dependências principais

| Biblioteca | Descrição |
|-------------|------------|
| `requests` | Consumo das APIs REST |
| `python-dotenv` | Leitura das variáveis do arquivo `.env` |
| `json` | Manipulação dos dados recebidos |
| `re` | Correções de formatação (vírgulas, caracteres especiais) |

---

## 💡 Próximos Passos
- [ ] Adicionar logging estruturado (logfile)
- [ ] Criar job no **Airflow** para execução automática
- [ ] Adicionar tratamento de falhas e reenvio

---

## 👨‍💻 Autor
**Jardel Sampaio**  
Engenheiro de Dados | Integrações ERP & GeoSales  
📧 [LinkedIn](https://linkedin.com/in/jardelsampaio) | 🌐 [GitHub](https://github.com/jardelsampaio)

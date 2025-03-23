# 🌾 FarmTech Solutions — Sistema de Gestão Agrícola

Sistema desenvolvido em **Python** e **R** para apoiar a agricultura digital. Permite o registro e análise de áreas cultivadas, cálculo de insumos, exportação de relatórios, análise estatística e exibição da previsão do tempo em tempo real.

---

## 🚀 Funcionalidades

- Registro e cálculo de área para as culturas:
  - **Cana-de-açúcar**
  - **Milho**
- Cálculo automático de **insumos necessários** por plantio
- Atualização e exclusão de registros de forma interativa
- Exportação de relatórios em **formato CSV**
- Execução de **análise estatística com R** (média e desvio padrão)
- Exibição da **previsão do tempo em São Paulo (SP)**, usando a API da OpenWeatherMap

---

## 📁 Estrutura do Projeto

```text
src/
├── main.py
├── models/
│   └── cultura.py
├── r_scripts/
│   ├── analise.R
│   └── clima.R
├── services/
│   ├── handlers/
│   │   ├── atualizar.py
│   │   ├── inserir.py
│   │   ├── listar.py
│   │   └── remover.py
│   └── utils/
│       ├── analise.py
│       ├── exportar.py
│       └── solicitar_valor.py
├── utils/
│   ├── limpar_console.py
│   └── menu.py
data/
└── culturas.csv
logs/
└── clima.log
└── README.md
```

---

## 🛠️ Requisitos

### Python

- Python 3.9+ instalado
- Instalar as dependências:

```bash
pip install -r requirements.txt
```

Conteúdo do `requirements.txt`:

```
python-dotenv
```

### R

- R instalado (https://cran.r-project.org/)
- Instale os pacotes necessários no terminal R:

```r
install.packages("httr")
install.packages("jsonlite")
```

---

## 🌐 API do Clima — OpenWeatherMap

O sistema utiliza a OpenWeatherMap para exibir a previsão do tempo automaticamente ao iniciar.

### Obtenção da API Key:

1. Acesse: https://openweathermap.org/api  
2. Crie uma conta gratuita ou faça login  
3. Acesse **"My API Keys"** no menu do usuário  
4. Copie sua chave (ex: `e9369c6f5346f6074aa039c98ce79d49`)  

### Crie o arquivo `.env` na raiz com:

```env
OWM_API_KEY=sua_api_key_aqui
```

> ⚠️ **Nunca compartilhe sua chave em repositórios públicos**

---

## ▶️ Como Executar o Sistema

No terminal:

```bash
python3 main.py
```

---

## 📊 Executar scripts R separadamente (opcional)

```bash
Rscript r_scripts/analise.R
Rscript r_scripts/clima.R
```

---

## 🖥️ Exemplo de Saída

```text
========== SISTEMA DE GESTAO AGRICOLA ==========
🌞 PREVISAO DO TEMPO
📍 São Paulo
☁️  CÉU LIMPO
🌡️  24.0 °C    💧 75%    💨 4.6 m/s

1. Registrar dados de plantio
2. Consultar analise de area e insumos
3. Atualizar informacoes de plantio
4. Excluir registro de plantio
5. Encerrar sistema
6. Exportar relatorio em CSV
7. Executar analise estatistica (R)

Escolha uma opcao: _
```

---

## 👨‍💻 Autor

Desenvolvido por **Moisés Lima**  
🎓 Projeto Acadêmico — FIAP | FarmTech Solutions  
🌐 Tecnologias: Python · R · OpenWeatherMap API · CSV · Terminal Apps

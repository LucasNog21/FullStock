# 📦 FullStock — Sistema de Gerenciamento de Estoque

**FullStock** é um sistema web desenvolvido em **Python (Django)** voltado para o **gerenciamento de estoque** e **controle de vendas** de pequenas e médias empresas.  
Ele oferece uma interface administrativa completa, dashboards interativos e suporte a múltiplos usuários com diferentes níveis de permissão.

> ⚠️ Algumas funcionalidades ainda estão em desenvolvimento, e o sistema está em fase inicial de implementação.

---

## 🧭 Visão Geral

O **FullStock** funciona como um **sistema de gerenciamento de estoque** especializado na gestão de produtos e fornecedores.  
Seu objetivo é automatizar o controle de estoque, pedidos e vendas, proporcionando uma visualização em tempo real do desempenho e das finanças da empresa.

O sistema é voltado tanto para **administradores**, que podem criar, editar e excluir produtos, quanto para **usuários**, que poderão acompanhar os itens disponíveis e realizar pedidos.

---

## 🏗️ Tecnologias Utilizadas

- **Backend:** [Python 3](https://www.python.org/) + [Django Framework](https://www.djangoproject.com/)
- **Frontend:** HTML5, CSS3
- **Banco de Dados:** SQLite (desenvolvimento)
- **Hospedagem prevista:** AWS (Amazon Web Services)
- **Controle de versão:** Git + GitHub

---

## 🚀 Funcionalidades

### ✅ Funcionalidades já implementadas
- Sistema de **autenticação** e **registro de usuários**
- Divisão de perfis entre **ADMIN** e **USER**
- Cadastro, edição e exclusão de:
  - **Produtos**
  - **Categorias**
  - **Fornecedores**
  - **Pedidos (Orders)**
- Upload de imagens de produtos
- **Atualização automática** da quantidade de produtos com base em pedidos realizados
- Interface **Dashboard** para administradores:
  - Exibe total de produtos
  - Total de vendas realizadas
  - Faturamento estimado
  - Produtos com **estoque baixo** (menos de 10 unidades)

---

## 🧩 Funcionalidades em desenvolvimento
- 📊 Gráficos dinâmicos de desempenho e faturamento
- 💵 Controle detalhado de **vendas (Sales)** e cálculo automático de lucro líquido
- 📦 Integração de pedidos de clientes diretamente via portal do usuário
- ☁️ Hospedagem e deploy automático em AWS
- 📱 Interface responsiva e aprimorada para dispositivos móveis

---

## 🧠 Estrutura do Projeto

```
FullStock/
│
├── project/                  # Configurações principais do Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── stock/                    # Aplicação principal do sistema
│   ├── models.py             # Modelos de dados (User, Product, Sale, etc.)
│   ├── views.py              # Views baseadas em classes (CBVs)
│   ├── forms.py              # Formulários do sistema
│   ├── urls.py               # Rotas da aplicação
│   └── templates/stock/      # Templates HTML
│
├── static/                   # Arquivos estáticos (CSS, JS, imagens)
│
├── media/                    # Uploads de imagens de produtos
│
├── manage.py                 # Comando principal do Django
└── README.md                 # Este arquivo
```

---

## ⚙️ Instalação e Execução

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/LucasNog21/FullStock.git
cd FullStock
```

### 2️⃣ Criar ambiente virtual
```bash
python -m venv venv
source venv/bin/activate    # Linux / Mac
venv\Scripts\activate       # Windows
```

### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Aplicar migrações
```bash
python manage.py migrate
```

### 5️⃣ Criar superusuário
```bash
python manage.py createsuperuser
```

### 6️⃣ Rodar o servidor
```bash
python manage.py runserver
```

Acesse o sistema em:
👉 **http://127.0.0.1:8000/**

---

## 🔒 Permissões de Acesso

- **Administrador (`ADMIN`):**
  - Acesso completo ao sistema (dashboard, CRUDs, relatórios).
- **Usuário comum (`USER`):**
  - Acesso limitado às informações públicas e pedidos.

O acesso ao **Dashboard** é restrito a usuários do grupo `ADMIN`.  
O link para o dashboard só é exibido no menu se o usuário for administrador.

---

## 🧮 Cálculos automáticos

- Ao criar um **pedido (Order)**:
  - O sistema aumenta automaticamente o estoque do produto conforme a quantidade pedida.
  - O valor do pedido é calculado automaticamente com base no preço do produto.

- Ao criar uma **venda (Sale)**:
  - O sistema calcula o **lucro** como a diferença entre `salePrice` e `productionPrice`.
  - A quantidade do produto em estoque é reduzida automaticamente (em implementação).

---

## 🧑‍💻 Contribuição

1. Faça um fork do projeto  
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça o commit das mudanças:
   ```bash
   git commit -m "Adiciona nova funcionalidade"
   ```
4. Envie para o seu fork:
   ```bash
   git push origin minha-feature
   ```
5. Crie um Pull Request 🚀

---


> _FullStock — Gerencie seu estoque com eficiência e simplicidade._

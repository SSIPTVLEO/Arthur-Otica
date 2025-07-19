# Sistema Arthurótica - Completo - Instruções de Uso

## Descrição
Sistema web local completo para gerenciamento de vendas e ordens de serviço da Arthurótica. O sistema permite gerenciar todas as informações através de 5 abas principais, salvando automaticamente todas as informações no arquivo Excel fornecido.

## 🎯 Funcionalidades Principais
- ✅ **5 Abas Completas**: Cliente, Ordem Serviço, Receita, Armação e Lente, Pagamento
- ✅ **Inserção de novos registros** em todas as abas
- ✅ **Visualização em tabelas** de todos os registros
- ✅ **Edição** de registros existentes (Cliente)
- ✅ **Exclusão** de registros em todas as abas
- ✅ **Salvamento automático** no arquivo Excel original
- ✅ **Interface responsiva** e amigável
- ✅ **Relacionamento entre dados** (Cliente → Ordem → Receita/Armação/Pagamento)

## 📋 Abas do Sistema

### 1. **ABA CLIENTE**
**Campos:**
- Nome * (obrigatório)
- CPF * (obrigatório)
- Data de Nascimento
- Endereço
- Bairro
- Cidade
- Telefone

**Funcionalidades:**
- Criar, editar, visualizar e excluir clientes
- Dados salvos na aba "Cliente" do Excel

### 2. **ABA ORDEM SERVIÇO**
**Campos:**
- Número da OS * (obrigatório)
- Data do Pedido * (obrigatório)
- ID do Cliente * (seleção dos clientes cadastrados)

**Funcionalidades:**
- Criar e visualizar ordens de serviço
- Vinculação automática com clientes
- Dados salvos na aba "Ordem Serviço" do Excel

### 3. **ABA RECEITA**
**Campos:**
- ID da OS * (seleção das ordens cadastradas)
- **Olho Direito - Longe:** Esférico, Cilíndrico, Eixo, DNP, Altura, Adição
- **Olho Esquerdo - Longe:** Esférico, Cilíndrico, Eixo, DNP, Altura, Adição
- **Perto:** Esférico O.D/O.E, Cilíndrico O.D/O.E, Eixo O.D/O.E

**Funcionalidades:**
- Cadastro completo de receitas oftalmológicas
- Dados salvos na aba "Receita" do Excel

### 4. **ABA ARMAÇÃO E LENTE**
**Campos:**
- ID da OS * (seleção das ordens cadastradas)
- Ponte, Horizontal, Vertical, Diagonal Maior
- Marca da Armação, Referência da Armação, Material da Armação
- Lente Comprada, Tratamento, Coloração

**Funcionalidades:**
- Cadastro de especificações de armação e lente
- Dados salvos na aba "Armação e lente" do Excel

### 5. **ABA PAGAMENTO**
**Campos:**
- ID da OS * (seleção das ordens cadastradas)
- Valor da Lente * (obrigatório)
- Valor da Armação * (obrigatório)
- Forma de Pagamento * (À Vista, Cartão de Crédito, Cartão de Débito, PIX, Parcelado, Dinheiro)
- Entrada, Número de Parcelas, Valor das Parcelas
- Status * (Pendente, Em Produção, Pronto, Entregue, Cancelado)

**Funcionalidades:**
- Gestão completa de pagamentos
- Cálculo automático do valor total
- Dados salvos na aba "Pagamento" do Excel

## 🚀 Como Usar o Sistema

### 1. **Iniciando o Sistema**
```bash
# 1. Navegue até a pasta do sistema
cd sistema-arthurotica

# 2. Ative o ambiente virtual
source venv/bin/activate

# 3. Inicie o servidor
python src/main.py

# 4. Acesse no navegador
http://localhost:5000
```

### 2. **Fluxo de Trabalho Recomendado**
1. **Cadastrar Cliente** (Aba Cliente)
2. **Criar Ordem de Serviço** (Aba Ordem Serviço)
3. **Registrar Receita** (Aba Receita)
4. **Especificar Armação e Lente** (Aba Armação e Lente)
5. **Gerenciar Pagamento** (Aba Pagamento)

### 3. **Navegação entre Abas**
- Clique nas abas no topo da tela para alternar entre as funcionalidades
- Os dados são carregados automaticamente ao acessar cada aba
- Selects são populados automaticamente com dados relacionados

### 4. **Criando Registros**
1. Preencha os campos obrigatórios (marcados com *)
2. Preencha campos opcionais conforme necessário
3. Clique em "Criar [Tipo]" para salvar
4. Os dados são salvos automaticamente no Excel

### 5. **Visualizando e Gerenciando Dados**
- Clique em "Atualizar Lista" para recarregar dados
- Use botões "Editar" e "Excluir" nas tabelas
- Todas as alterações são sincronizadas com o Excel

## 📁 Estrutura de Arquivos
```
sistema-arthurotica/
├── SISTEMA-ARTHURÓTICA.xlsx    # Arquivo Excel com dados
├── src/
│   ├── main.py                 # Servidor principal
│   ├── static/index.html       # Interface do usuário
│   ├── models/                 # Modelos de dados
│   └── routes/                 # APIs para cada aba
├── venv/                       # Ambiente virtual Python
└── INSTRUÇÕES-COMPLETAS.md     # Este arquivo
```

## 🔧 Funcionalidades Técnicas

### **Salvamento Automático**
- Todos os dados são salvos simultaneamente no banco SQLite local e no Excel
- Sincronização automática entre banco e Excel
- Backup automático dos dados

### **Relacionamentos**
- Cliente → Ordem de Serviço (1:N)
- Ordem de Serviço → Receita (1:1)
- Ordem de Serviço → Armação e Lente (1:1)
- Ordem de Serviço → Pagamento (1:1)

### **Validações**
- Campos obrigatórios são validados
- Formatos de data são verificados
- Valores numéricos são validados

## ⚠️ Observações Importantes

### **Backup e Segurança**
1. **Faça backup regular** do arquivo Excel
2. **Não abra o Excel** enquanto o sistema estiver rodando
3. **Mantenha o ambiente virtual ativado** durante o uso

### **Limitações**
- Sistema roda apenas localmente (localhost:5000)
- Acesso simultâneo limitado a um usuário
- Requer Python 3.11+ instalado

### **Dependências**
- Flask (servidor web)
- SQLAlchemy (banco de dados)
- openpyxl (manipulação Excel)
- Todas as dependências estão no requirements.txt

## 🛠️ Solução de Problemas

### **Erro ao iniciar o servidor**
```bash
# Verifique se está na pasta correta
pwd

# Ative o ambiente virtual
source venv/bin/activate

# Instale dependências se necessário
pip install -r requirements.txt
```

### **Dados não aparecem**
1. Clique em "Atualizar Lista" na aba correspondente
2. Verifique se o arquivo Excel está na pasta correta
3. Reinicie o servidor se necessário

### **Erro ao salvar no Excel**
1. Feche o arquivo Excel se estiver aberto
2. Verifique permissões de escrita na pasta
3. Confirme que o arquivo não está corrompido

### **Problemas de relacionamento**
1. Certifique-se de criar Cliente antes da Ordem
2. Crie Ordem antes de Receita/Armação/Pagamento
3. Use os selects para vincular registros corretamente

## 📊 Relatórios e Dados

### **Visualização no Excel**
- Abra o arquivo SISTEMA-ARTHURÓTICA.xlsx para ver todos os dados
- Cada aba contém os dados correspondentes do sistema
- Use filtros e fórmulas do Excel para análises

### **Exportação**
- Os dados estão sempre sincronizados no Excel
- Faça cópias do arquivo Excel para backup
- Use o Excel para relatórios e análises avançadas

## 🎯 Próximos Passos
1. **Teste todas as funcionalidades** com dados reais
2. **Configure backup automático** do arquivo Excel
3. **Treine usuários** no fluxo de trabalho recomendado
4. **Monitore o desempenho** e ajuste conforme necessário

---
**Sistema desenvolvido para uso local - Arthurótica**
**Versão Completa com 5 Abas Integradas**


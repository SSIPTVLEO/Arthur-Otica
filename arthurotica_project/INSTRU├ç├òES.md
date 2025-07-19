# Sistema Arthurótica - Instruções de Uso

## Descrição
Sistema web local para gerenciamento de vendas e ordens de serviço da Arthurótica. O sistema permite inserir, editar, visualizar e excluir registros, salvando automaticamente todas as informações no arquivo Excel fornecido.

## Funcionalidades
- ✅ Inserção de novos registros
- ✅ Visualização de todos os registros
- ✅ Edição de registros existentes
- ✅ Exclusão de registros
- ✅ Salvamento automático no Excel
- ✅ Interface responsiva e amigável
- ✅ Cálculo automático do valor total

## Como Usar

### 1. Iniciando o Sistema
1. Abra o terminal/prompt de comando
2. Navegue até a pasta do sistema:
   ```
   cd sistema-arthurotica
   ```
3. Ative o ambiente virtual:
   ```
   source venv/bin/activate
   ```
4. Inicie o servidor:
   ```
   python src/main.py
   ```
5. Abra seu navegador e acesse: `http://localhost:5000`

### 2. Criando um Novo Registro
1. Preencha os campos obrigatórios:
   - ID da OS
   - Valor da Lente
   - Valor da Armação
   - Forma de Pagamento
   - Status
2. Preencha os campos opcionais se necessário:
   - Entrada
   - Número de Parcelas
   - Valor das Parcelas
3. Clique em "Criar Registro"
4. O registro será salvo automaticamente no Excel

### 3. Visualizando Registros
- Os registros aparecem automaticamente na tabela "Registros Existentes"
- Clique em "Atualizar Lista" para recarregar os dados

### 4. Editando um Registro
1. Clique no botão "Editar" na linha do registro desejado
2. Modifique os campos necessários no formulário de edição
3. Clique em "Salvar Alterações"
4. As mudanças serão salvas automaticamente no Excel

### 5. Excluindo um Registro
1. Clique no botão "Excluir" na linha do registro desejado
2. Confirme a exclusão
3. O registro será removido do banco e do Excel

## Campos do Sistema

### Obrigatórios
- **ID da OS**: Identificador único da ordem de serviço
- **Valor da Lente**: Valor em reais da lente
- **Valor da Armação**: Valor em reais da armação
- **Forma de Pagamento**: À Vista, Cartão de Crédito, Cartão de Débito, PIX, Parcelado, Dinheiro
- **Status**: Pendente, Em Produção, Pronto, Entregue, Cancelado

### Opcionais
- **Entrada**: Valor da entrada (se houver)
- **Número de Parcelas**: Quantidade de parcelas
- **Valor das Parcelas**: Valor de cada parcela

### Automático
- **Valor Total**: Calculado automaticamente (Valor da Lente + Valor da Armação)

## Arquivos Importantes
- `SISTEMA-ARTHURÓTICA.xlsx`: Arquivo Excel onde os dados são salvos
- `src/main.py`: Arquivo principal do sistema
- `src/static/index.html`: Interface do usuário
- `src/database/app.db`: Banco de dados SQLite local

## Observações Importantes
1. **Backup**: Faça backup regular do arquivo Excel
2. **Sincronização**: Todos os dados são salvos tanto no banco local quanto no Excel
3. **Acesso Local**: O sistema roda apenas localmente (localhost:5000)
4. **Dependências**: Mantenha o ambiente virtual ativado ao usar o sistema

## Solução de Problemas

### Erro ao iniciar o servidor
- Verifique se o ambiente virtual está ativado
- Certifique-se de estar na pasta correta
- Verifique se todas as dependências estão instaladas

### Dados não aparecem
- Clique em "Atualizar Lista"
- Verifique se o arquivo Excel está na pasta correta
- Reinicie o servidor se necessário

### Erro ao salvar no Excel
- Verifique se o arquivo Excel não está aberto em outro programa
- Confirme as permissões de escrita na pasta
- Verifique se o arquivo Excel existe e não está corrompido

## Suporte
Para dúvidas ou problemas, verifique:
1. Se todos os campos obrigatórios estão preenchidos
2. Se o arquivo Excel está acessível
3. Se o servidor está rodando corretamente
4. Se não há erros no terminal/prompt

---
**Sistema desenvolvido para uso local - Arthurótica**


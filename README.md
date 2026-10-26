<h1 align="center">📊 Salesforce CSV Data Import Suite</h1>

<p align="center">
  Ferramentas desktop desenvolvidas para preparação, transformação, consulta e atualização de dados no Salesforce, automatizando tarefas operacionais e reduzindo ajustes manuais durante processos de importação e manutenção de registros.
</p>

<p align="center">
  A suíte reúne ferramentas independentes para Pessoa Física (PF), Pessoa Jurídica (PJ), geração de consultas SOQL e preparação de dados para atualização de Contracts.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Ativo-success" alt="Status Ativo">
  <img src="https://img.shields.io/badge/Plataforma-Windows-blue" alt="Plataforma Windows">
  <img src="https://img.shields.io/badge/Linguagem-Python-orange" alt="Python">
  <img src="https://img.shields.io/badge/Interface-Tkinter-lightgrey" alt="Tkinter">
  <img src="https://img.shields.io/badge/Integração-Salesforce-00A1E0" alt="Salesforce">
</p>

---

<h2>⬇️ Releases</h2>

<table>
  <thead>
    <tr>
      <th>Versão</th>
      <th>Módulo</th>
      <th>Descrição</th>
      <th>Download</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1.6.3</td>
      <td>PF</td>
      <td>Importação e preparação de dados para Pessoa Física</td>
      <td><a href="https://github.com/joaoandradegp-wq/Salesforce-CSV_Data_Import/releases/download/1.6.3/SF-DataImport_PF-Multi.exe">Clique aqui</a></td>
    </tr>
    <tr>
      <td>1.6.2.1</td>
      <td>PJ</td>
      <td>Importação e preparação de dados para Pessoa Jurídica</td>
      <td><a href="https://github.com/joaoandradegp-wq/Salesforce-CSV_Data_Import/releases/download/1.6.2.1/SF-DataImport_PJ.exe">Clique aqui</a></td>
    </tr>
    <tr>
      <td>1.1</td>
      <td>SOQL Generator</td>
      <td>Geração de consultas SOQL por múltiplos IDs ou valores</td>
      <td><a href="https://github.com/joaoandradegp-wq/Salesforce-CSV_Data_Import/releases/download/1.0/SF-SOQL_Generator.exe">Clique aqui</a></td>
    </tr>
    <tr>
      <td>1.0.1</td>
      <td>Update Contract Database</td>
      <td>Preparação de dados para atualização de Contracts</td>
      <td><a href="https://github.com/joaoandradegp-wq/Salesforce-CSV_Data_Import/releases/download/1.0.1/SF-Update_Contract_Database_PF.exe">Clique aqui</a></td>
    </tr>
  </tbody>
</table>

<blockquote>
  <strong>Observação:</strong> SOQL Generator e Update Contract Database são ferramentas independentes dos módulos de importação PF e PJ.
</blockquote>

---

<h2>🧭 Comparativo PF × PJ</h2>

<table>
  <thead>
    <tr>
      <th>Característica</th>
      <th>👤 PF - Pessoa Física</th>
      <th>🏢 PJ - Pessoa Jurídica</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Foco</strong></td>
      <td>Preparação de dados de clientes Pessoa Física</td>
      <td>Preparação de Contracts e Assets</td>
    </tr>
    <tr>
      <td><strong>Objetos</strong></td>
      <td>Account, Contract, Asset</td>
      <td>Account, Contract, Asset</td>
    </tr>
    <tr>
      <td><strong>Relacionamento</strong></td>
      <td>1 Account → 1 Contract / 1 Asset</td>
      <td>1 Account → N Contracts / N Assets</td>
    </tr>
    <tr>
      <td><strong>Recursos</strong></td>
      <td>UPDATE opcional de Account, UPSERT de Asset por <code>Placa__c</code>, SOQL por CPF e tratamento de CPF</td>
      <td>Distribuição automática de <code>AccountId</code>, validação Contract × Asset e UPSERT de Asset por <code>Placa__c</code></td>
    </tr>
  </tbody>
</table>

---

<h2>🚀 Como utilizar o Data Import PF/PJ</h2>

<table>
  <thead>
    <tr>
      <th>Passo</th>
      <th>Ação</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>Inserir os Account IDs da organização Salesforce</td></tr>
    <tr><td>2</td><td>Anexar o arquivo Excel</td></tr>
    <tr><td>3</td><td>Clicar em <strong>Processar e Salvar CSV</strong></td></tr>
    <tr><td>4</td><td>Selecionar o objeto desejado</td></tr>
    <tr><td>5</td><td>Copiar os dados gerados para a Área de Transferência, quando aplicável</td></tr>
    <tr><td>6</td><td>Abrir o Data Import do Salesforce Inspector ou o Data Loader</td></tr>
    <tr><td>7</td><td>Colar os dados com <code>CTRL + V</code>, quando aplicável</td></tr>
    <tr><td>8</td><td>Ajustar os campos solicitados pelo Salesforce e executar a operação</td></tr>
  </tbody>
</table>

---

<h2>👤 Módulo Pessoa Física</h2>

<h3>Leitura de planilha</h3>
<p>Importação de arquivos <code>.xlsx</code> e <code>.xls</code> com abas obrigatórias <code>Account</code>, <code>Contract</code> e <code>Ativo</code>, incluindo validação das abas e da quantidade de registros.</p>

<h3>Vinculação automática</h3>
<ul>
  <li>1 Account → 1 Contract.</li>
  <li>1 Account → 1 Asset.</li>
  <li>Associação dos registros por meio do <code>AccountId</code>.</li>
  <li>Distribuição dos Account IDs informados conforme os registros da planilha.</li>
</ul>

<h3>Transformação de dados</h3>
<p>Conversão de datas, padronização de CPF, renomeação de campos, conversão de Status do Asset e aplicação de <code>RecordTypeId</code>.</p>

<h3>Exportação</h3>
<p>Arquivos <code>Account.csv</code>, <code>Contract.csv</code> e <code>Asset.csv</code>, com codificação UTF-8.</p>

<h3>Regras por objeto</h3>
<table>
  <thead>
    <tr><th>Objeto</th><th>Campo</th><th>Regra</th></tr>
  </thead>
  <tbody>
    <tr><td rowspan="6"><strong>Account</strong></td><td><code>Id</code></td><td>Recebe os Account IDs informados. A quantidade deve corresponder aos registros da aba.</td></tr>
    <tr><td><code>Email</code> → <code>Email__c</code></td><td>Renomeação de campo</td></tr>
    <tr><td><code>CPF__pc</code></td><td>Remove caracteres não numéricos, garante 11 dígitos e preserva zeros à esquerda</td></tr>
    <tr><td><code>RecordTypeId</code></td><td><code>0125A0000013RxeQAE</code></td></tr>
    <tr><td><code>AreaNegocio__c</code></td><td><code>Leves</code></td></tr>
    <tr><td>Operação</td><td>UPDATE opcional</td></tr>
    <tr><td rowspan="9"><strong>Contract</strong></td><td><code>Id</code></td><td>Recebe o ID da Conta conforme a regra implementada</td></tr>
    <tr><td><code>AccountId</code></td><td>Recebe os IDs informados, mantendo a relação 1:1</td></tr>
    <tr><td><code>Status</code></td><td><code>Draft</code></td></tr>
    <tr><td><code>IRIS_Categoria_Contrato__c</code></td><td><code>2</code></td></tr>
    <tr><td>Datas</td><td>Convertidas para <code>YYYY-MM-DD</code></td></tr>
    <tr><td><code>IRIS_CapturaReservaPrimeiraParcela__c</code></td><td><code>TRUE</code></td></tr>
    <tr><td><code>IRIS_ReservaPrimeiraParcela__c</code></td><td><code>TRUE</code></td></tr>
    <tr><td><code>RecordTypeId</code></td><td><code>012U6000000OTnFIAW</code></td></tr>
    <tr><td>Operação</td><td>INSERT</td></tr>
    <tr><td rowspan="7"><strong>Asset</strong></td><td><code>Id</code></td><td>Recebe o ID da Conta conforme a regra implementada</td></tr>
    <tr><td><code>AccountId</code></td><td>Recebe os IDs informados, mantendo a relação 1:1</td></tr>
    <tr><td>Datas</td><td>Convertidas para <code>YYYY-MM-DD</code></td></tr>
    <tr><td><code>RecordType.Name</code> → <code>RecordTypeId</code></td><td>Renomeação</td></tr>
    <tr><td><code>RecordTypeId</code></td><td><code>012HY0000004NyFYAU</code></td></tr>
    <tr><td>Status</td><td><code>Disponível</code> → <code>Locado</code>; <code>Alugado</code> → <code>Locado</code></td></tr>
    <tr><td>Operação</td><td>UPSERT via <code>Placa__c</code></td></tr>
  </tbody>
</table>

<h3>🔎 SOQL por CPF</h3>
<p>Localiza a aba <code>Account</code> ou <code>Clientes</code>, utiliza o campo <code>CPF__pc</code>, remove caracteres não numéricos, padroniza os CPFs para 11 dígitos, elimina duplicidades e copia a consulta gerada para a Área de Transferência.</p>

<pre><code>SELECT Id, Name, CPF__pc
FROM Account
WHERE CPF__pc IN (...)
ORDER BY Name</code></pre>

---

<h2>🏢 Módulo Pessoa Jurídica</h2>

<h3>Leitura de planilha</h3>
<p>Importação de arquivos <code>.xlsx</code> e <code>.xls</code> com abas obrigatórias <code>Account</code>, <code>Contract</code> e <code>Ativo</code>, incluindo validação das abas.</p>

<h3>Vinculação automática</h3>
<ul>
  <li>1 Account → N Contracts.</li>
  <li>1 Account → N Assets.</li>
  <li>Distribuição automática de <code>AccountId</code>.</li>
  <li>Validação de consistência entre Contract e Asset.</li>
</ul>

<h3>Transformação de dados</h3>
<p>Conversão de datas, tratamento de <code>ContractTerm</code>, renomeação de campos, aplicação de <code>RecordTypeId</code> e conversões específicas.</p>

<h3>Exportação</h3>
<p>Arquivos <code>Account.csv</code>, <code>Contract.csv</code> e <code>Asset.csv</code>, com codificação UTF-8.</p>

<h3>Regras por objeto</h3>
<table>
  <thead>
    <tr><th>Objeto</th><th>Campo</th><th>Regra</th></tr>
  </thead>
  <tbody>
    <tr><td rowspan="5"><strong>Account</strong></td><td><code>Id</code></td><td>Recebe o Account ID informado</td></tr>
    <tr><td><code>Email</code> → <code>Email__c</code></td><td>Renomeação de campo</td></tr>
    <tr><td><code>CPF__pc</code></td><td>Tratamento específico</td></tr>
    <tr><td><code>RecordTypeId</code></td><td><code>0125A0000013RibQAE</code></td></tr>
    <tr><td><code>AreaNegocio__c</code></td><td><code>Leves</code></td></tr>
    <tr><td rowspan="11"><strong>Contract</strong></td><td><code>Id</code></td><td>Recebe o ID da Conta conforme a regra implementada</td></tr>
    <tr><td><code>AccountId</code></td><td>Distribuído automaticamente entre os Contracts</td></tr>
    <tr><td><code>Status</code></td><td><code>Draft</code></td></tr>
    <tr><td><code>IRIS_Categoria_Contrato__c</code></td><td><code>2</code></td></tr>
    <tr><td>Datas</td><td>Convertidas para <code>YYYY-MM-DD</code></td></tr>
    <tr><td><code>ContractTerm</code></td><td>Tratado automaticamente</td></tr>
    <tr><td>Valor <code>0</code></td><td>Convertido para vazio</td></tr>
    <tr><td><code>IRIS_CapturaReservaPrimeiraParcela__c</code></td><td><code>false</code></td></tr>
    <tr><td><code>IRIS_ReservaPrimeiraParcela__c</code></td><td><code>false</code></td></tr>
    <tr><td><code>RecordTypeId</code></td><td><code>012U6000009ru5eIAA</code></td></tr>
    <tr><td>Operação</td><td>INSERT</td></tr>
    <tr><td rowspan="5"><strong>Asset</strong></td><td><code>Id</code></td><td>Recebe o ID da Conta conforme a regra implementada</td></tr>
    <tr><td><code>AccountId</code></td><td>Distribuído automaticamente entre os Assets</td></tr>
    <tr><td>Datas</td><td>Convertidas para <code>YYYY-MM-DD</code></td></tr>
    <tr><td><code>RecordType.Name</code> → <code>RecordTypeId</code></td><td>Renomeação</td></tr>
    <tr><td><code>RecordTypeId</code></td><td><code>012U6000009ru5JIAQ</code></td></tr>
    <tr><td><strong>Asset</strong></td><td>Operação</td><td>UPSERT via <code>Placa__c</code></td></tr>
  </tbody>
</table>

<h3>🔍 Validação Contract × Asset</h3>
<p>Compara <code>IRIS_Contrato__r.IRIS_CodigoContratoMasterLocavia__c</code> com <code>IRIS_CodigoContratoMasterLocavia__c</code>. Se um Asset referenciar um contrato inexistente, o processamento é interrompido.</p>

<h3>🔧 Renomeações automáticas</h3>
<table>
  <thead><tr><th>Origem</th><th>Destino</th></tr></thead>
  <tbody>
    <tr><td><code>ContractNumber</code></td><td><code>_ContractNumber</code></td></tr>
    <tr><td><code>Account.Name</code></td><td><code>_Account.Name</code></td></tr>
    <tr><td><code>IDExternoAX__c</code></td><td><code>_IDExternoAX__c</code></td></tr>
    <tr><td><code>EndDate</code></td><td><code>_EndDate</code></td></tr>
    <tr><td><code>RecordType.DeveloperName</code></td><td><code>_RecordType.DeveloperName</code></td></tr>
    <tr><td><code>IRIS_Codigo_Status_do_Tanque__c</code></td><td><code>_IRIS_Codigo_Status_do_Tanque__c</code></td></tr>
    <tr><td><code>IRIS_Codigo_Situacao_do_Agendamento__c</code></td><td><code>_IRIS_Codigo_Situacao_do_Agendamento__c</code></td></tr>
  </tbody>
</table>

<h3>🔎 SOQL por CNPJ</h3>
<p>A interface apresenta a opção <strong>Gerar SOQL por CNPJ</strong>. A implementação descrita utiliza o campo <code>CPF__pc</code>, remove caracteres não numéricos, padroniza os valores para 11 dígitos, elimina duplicidades e copia a consulta para a Área de Transferência.</p>

<blockquote>
  <strong>Atenção:</strong> apesar do nome da opção, o campo utilizado no código atual é <code>CPF__pc</code>, com tratamento para 11 dígitos. Isso não corresponde ao formato convencional de um CNPJ.
</blockquote>

<h3>⚠️ Status do Contract</h3>
<p>O programa gera <code>Status = Draft</code>. A conversão posterior de Draft para Ativo não é realizada pelo programa.</p>

---

<h2>🔎 SOQL Generator</h2>

<p>Ferramenta desktop independente para gerar consultas SOQL a partir de múltiplos IDs ou valores, permitindo selecionar o objeto Salesforce, configurar o campo de filtro e dividir automaticamente as consultas em partes.</p>

<h3>🚀 Como usar</h3>
<table>
  <thead><tr><th>Passo</th><th>Ação</th></tr></thead>
  <tbody>
    <tr><td>1</td><td>Selecionar o objeto Salesforce</td></tr>
    <tr><td>2</td><td>Colar os IDs ou valores no campo de entrada</td></tr>
    <tr><td>3</td><td>Definir a quantidade máxima de valores por parte</td></tr>
    <tr><td>4</td><td>Clicar em <strong>GERAR PARTES</strong></td></tr>
    <tr><td>5</td><td>Selecionar o botão correspondente à parte desejada</td></tr>
    <tr><td>6</td><td>A consulta é copiada para a Área de Transferência</td></tr>
  </tbody>
</table>

<h3>⚙️ Objetos disponíveis</h3>
<table>
  <thead>
    <tr><th>Objeto</th><th>Campos do SELECT</th><th>Campo utilizado no filtro</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><code>IRIS_Cupom__c</code></td>
      <td><code>id</code>, <code>IRIS_Cupom__c</code>, <code>name</code></td>
      <td><code>name</code></td>
    </tr>
    <tr>
      <td><code>Opportunity</code></td>
      <td><code>id</code>, <code>Name</code>, <code>IRIS_CodigoContratoLocavia__c</code>, <code>StageName</code></td>
      <td><code>id</code></td>
    </tr>
    <tr>
      <td><code>Contract</code></td>
      <td><code>id</code>, <code>IRIS_CodigoContratoLocavia__c</code>, <code>Status</code></td>
      <td><code>IRIS_CodigoContratoLocavia__c</code></td>
    </tr>
    <tr>
      <td><code>Asset</code></td>
      <td><code>id</code>, <code>IRIS_NomedoAtivo__c</code>, <code>Placa__c</code></td>
      <td><code>Placa__c</code></td>
    </tr>
  </tbody>
</table>

<h3>🔧 Recursos</h3>
<ul>
  <li>Interface gráfica desenvolvida com Python e Tkinter.</li>
  <li>Seleção de objeto por lista suspensa.</li>
  <li>Entrada de valores separados por espaços, quebras de linha, vírgulas ou ponto e vírgula.</li>
  <li>Limite configurável de valores por consulta, com padrão de <strong>500 valores por parte</strong>.</li>
  <li>Divisão automática dos valores conforme o limite definido.</li>
  <li>Geração de consultas SOQL com os valores entre aspas simples.</li>
  <li>Ordenação dos resultados por <code>CreatedDate DESC</code>.</li>
  <li>Criação dinâmica de botões individuais para cada parte gerada.</li>
  <li>Cópia individual das consultas para a Área de Transferência.</li>
  <li>Limpeza das partes anteriores ao trocar de objeto.</li>
  <li>Validação do objeto selecionado, da entrada de valores e do limite configurado.</li>
</ul>

<h3>📝 Exemplo de consulta - Contract</h3>
<pre><code>SELECT id, IRIS_CodigoContratoLocavia__c, Status
FROM Contract
WHERE IRIS_CodigoContratoLocavia__c IN ('valor1','valor2','valor3')
ORDER BY CreatedDate DESC</code></pre>

<h3>📝 Exemplo de consulta - Asset</h3>
<pre><code>SELECT id, IRIS_NomedoAtivo__c, Placa__c
FROM Asset
WHERE Placa__c IN ('ABC1234','DEF5678')
ORDER BY CreatedDate DESC</code></pre>

---

<h2>🔄 Update Contract Database</h2>

<p>Ferramenta independente para preparação de dados do objeto Contract, com tratamento de planilhas, conversão de campos, comparação de execuções anteriores e geração de arquivo para atualização no Salesforce.</p>

<h3>🚀 Como usar</h3>
<table>
  <thead><tr><th>Passo</th><th>Ação</th></tr></thead>
  <tbody>
    <tr><td>1</td><td>Selecionar o arquivo XLSX</td></tr>
    <tr><td>2</td><td>Processar a planilha</td></tr>
    <tr><td>3</td><td>Os dados são tratados automaticamente</td></tr>
    <tr><td>4</td><td>Uma aba <code>Salesforce</code> é criada</td></tr>
    <tr><td>5</td><td>O arquivo tratado é salvo</td></tr>
  </tbody>
</table>

<h3>🔧 De/Para de campos</h3>
<table>
  <thead><tr><th>Origem</th><th>Salesforce</th></tr></thead>
  <tbody>
    <tr><td>SF Id Contrato</td><td><code>id</code></td></tr>
    <tr><td>Locavia Data de início do contrato</td><td><code>StartDate</code></td></tr>
    <tr><td>Locavia Status Contrato</td><td><code>Status</code></td></tr>
    <tr><td>Data Cancelamento</td><td><code>IRIS_DataCancelamento__c</code></td></tr>
  </tbody>
</table>

<p>As datas são convertidas para o formato <code>YYYY-MM-DD</code>.</p>

<h3>🔄 Mapeamento de Status</h3>
<table>
  <thead><tr><th>Origem</th><th>Salesforce</th></tr></thead>
  <tbody>
    <tr><td>Em Vigência</td><td><code>Activated</code></td></tr>
    <tr><td>Aberto</td><td><code>Draft</code></td></tr>
    <tr><td>Assinado</td><td><code>Draft</code></td></tr>
    <tr><td>Em Assinatura</td><td><code>Draft</code></td></tr>
    <tr><td>Demais valores</td><td>Permanecem inalterados</td></tr>
  </tbody>
</table>

<p>A aba <code>Salesforce</code> gerada contém os campos <code>id</code>, <code>StartDate</code>, <code>Status</code> e <code>IRIS_DataCancelamento__c</code>.</p>

<h3>📊 Comparação com execução anterior</h3>
<p>Quando existe uma execução anterior, os registros são comparados pelo campo <code>id</code>, considerando <code>StartDate</code>, <code>Status</code> e <code>IRIS_DataCancelamento__c</code>.</p>

<p>São apresentados:</p>
<ul>
  <li>Total de registros.</li>
  <li>Novos registros.</li>
  <li>Registros atualizados.</li>
</ul>

<h3>📝 Log de execução</h3>
<p>As informações são registradas em <code>log_atualizacoes.txt</code>, incluindo data da execução, total de registros, novos registros e registros atualizados.</p>

<h3>📁 Arquivo de saída</h3>
<p>O arquivo tratado é salvo no formato <code>DD-MM-AAAA.xlsx</code>.</p>

---

<h2>📦 Dependências</h2>
<table>
  <thead><tr><th>Ferramenta</th><th>Dependências</th></tr></thead>
  <tbody>
    <tr><td>Data Import PF/PJ</td><td>Python · Tkinter · Pandas</td></tr>
    <tr><td>SOQL Generator</td><td>Python · Tkinter</td></tr>
    <tr><td>Update Contract Database</td><td>Python · Tkinter · openpyxl</td></tr>
  </tbody>
</table>

---

<p align="center">
  Automatizando a preparação, higienização, consulta e atualização de dados para Salesforce. ☁️
</p>

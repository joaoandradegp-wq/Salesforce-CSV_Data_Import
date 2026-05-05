<h1 align="center">📄 Excel → Salesforce CSV Converter</h1>

<p align="center">
Ferramenta para transformar planilhas Excel em arquivos CSV prontos para importação no Salesforce (Account, Contract e Asset).
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Ativo-success">
  <img src="https://img.shields.io/badge/Linguagem-Python-blue">
  <img src="https://img.shields.io/badge/Interface-Tkinter-lightgrey">
</p>

<h2>📌 Sobre</h2>

<p>
Este aplicativo foi desenvolvido para automatizar a preparação de dados para importação no Salesforce, eliminando a necessidade de tratamento manual em planilhas.
</p>

<p>
A ferramenta lê um arquivo Excel estruturado, aplica regras de negócio específicas e gera automaticamente três arquivos CSV:
</p>

<ul>
  <li><b>Account.csv</b></li>
  <li><b>Contract.csv</b></li>
  <li><b>Asset.csv</b></li>
</ul>

<p>
Esses arquivos já saem prontos para uso em processos de <b>UPSERT</b> e <b>INSERT</b> dentro do Salesforce.
</p>

<h2>⚙️ Como funciona</h2>

<p>
O fluxo da aplicação é baseado em dois inputs principais:
</p>

<ul>
  <li>Uma lista de <b>Account IDs</b> (colados manualmente)</li>
  <li>Um arquivo Excel contendo as abas de dados</li>
</ul>

<p>
A partir disso, o sistema faz o cruzamento das informações e gera os arquivos finais já estruturados.
</p>

<h2>📂 Estrutura esperada do Excel</h2>

<p>O arquivo precisa conter três abas:</p>

<ul>
  <li><b>Account</b> (ou similar)</li>
  <li><b>Contract</b> (ou similar)</li>
  <li><b>Ativo</b> (Asset)</li>
</ul>

<p>
A identificação é feita automaticamente pelo nome da aba (case insensitive).
</p>

<h2>🔗 Regra principal de vínculo</h2>

<p>
O relacionamento entre os dados é feito através da lista de <b>Account IDs</b> informada pelo usuário.
</p>

<ul>
  <li>Cada linha do Excel é associada a um Account ID correspondente</li>
  <li>A quantidade de IDs deve ser igual à quantidade de registros em cada aba</li>
  <li>Se houver divergência, o processamento é interrompido</li>
</ul>

<h2>🧠 Regras de negócio aplicadas</h2>

<h3>📌 ACCOUNT</h3>

<ul>
  <li>Campo <b>Id</b> é preenchido com os Account IDs informados</li>
  <li>Campo <b>Email</b> é automaticamente renomeado para <b>Email__c</b></li>
  <li>Campo <b>CPF__pc</b>:
    <ul>
      <li>Remove espaços</li>
      <li>Garante 11 dígitos (padding com zero à esquerda)</li>
    </ul>
  </li>
  <li><b>RecordTypeId</b> fixo: 0125A0000013RxeQAE</li>
  <li><b>AreaNegocio__c</b> fixado como "Leves" (quando existente)</li>
</ul>

<h3>📌 CONTRACT</h3>

<ul>
  <li>Campo <b>AccountId</b> vinculado aos IDs informados</li>
  <li>Campo <b>Status</b> fixado como <b>Draft</b></li>
  <li><b>IRIS_Categoria_Contrato__c</b> fixo: 2</li>
  <li>Campos de data são convertidos para formato <b>YYYY-MM-DD</b></li>
  <li>Campos booleanos específicos são forçados como <b>TRUE</b></li>
  <li><b>RecordTypeId</b> fixo: 012U6000000OTnFIAW</li>
</ul>

<h3>📌 ASSET</h3>

<ul>
  <li>Campo <b>AccountId</b> vinculado aos IDs informados</li>
  <li>Campos de data também convertidos para <b>YYYY-MM-DD</b></li>
  <li>Campo <b>RecordType.Name</b> é convertido para <b>RecordTypeId</b></li>
  <li><b>RecordTypeId</b> fixo: 012HY0000004NyFYAU</li>
</ul>

<h3>🔄 RENOMEAÇÕES AUTOMÁTICAS</h3>

<p>
Alguns campos são renomeados automaticamente para evitar conflitos ou bloqueios de atualização:
</p>

<ul>
  <li>ContractNumber → _ContractNumber</li>
  <li>Account.Name → _Account.Name</li>
  <li>IDExternoAX__c → _IDExternoAX__c</li>
  <li>EndDate → _EndDate</li>
  <li>RecordType.DeveloperName → _RecordType.DeveloperName</li>
</ul>

<p>
Campos específicos do IRIS também são renomeados para evitar falhas no processo de importação.
</p>

<h2>📊 Geração de SOQL</h2>

<p>
A ferramenta possui um recurso auxiliar que gera automaticamente uma query SOQL baseada nos CPFs presentes no Excel.
</p>

<p>
A query é copiada diretamente para a área de transferência, pronta para uso no Salesforce.
</p>

<h2>🚀 Como usar</h2>

<ol>
  <li>Cole os <b>Account IDs</b> (um por linha)</li>
  <li>Clique em <b>Anexar Arquivo</b> e selecione o Excel</li>
  <li>(Opcional) Gere a SOQL por CPF</li>
  <li>Clique em <b>Processar e Salvar CSV</b></li>
  <li>Copie os CSVs gerados diretamente pelo botão</li>
</ol>

<h2>🎯 O que isso resolve</h2>

<ul>
  <li>Elimina ajustes manuais em planilhas</li>
  <li>Garante consistência de dados para importação</li>
  <li>Evita erros de formatação e relacionamento</li>
  <li>Automatiza regras de negócio repetitivas</li>
  <li>Agiliza processos de carga no Salesforce</li>
</ul>

<h2>⚠️ Validações</h2>

<ul>
  <li>Arquivo Excel obrigatório</li>
  <li>Abas obrigatórias (Account, Contract, Ativo)</li>
  <li>Quantidade de IDs deve bater com registros</li>
  <li>Colunas obrigatórias devem existir</li>
</ul>

<h2>🖥️ Interface</h2>

<ul>
  <li>Campo para inserção de Account IDs</li>
  <li>Contador automático de IDs</li>
  <li>Botão de anexar Excel</li>
  <li>Geração de SOQL por CPF</li>
  <li>Botão de processamento</li>
  <li>Acesso rápido aos CSVs gerados</li>
</ul>

<h2>🛠️ Tecnologias</h2>

<ul>
  <li>Python</li>
  <li>pandas</li>
  <li>tkinter</li>
</ul>

<h2>📥 Output</h2>

<p>
Os arquivos são gerados na mesma pasta do Excel:
</p>

<ul>
  <li>Account.csv (UPSERT via CPF__pc)</li>
  <li>Contract.csv (INSERT)</li>
  <li>Asset.csv (UPSERT via Placa__c)</li>
</ul>

<p align="center">
Ferramenta feita para eliminar retrabalho em importações no Salesforce
</p>

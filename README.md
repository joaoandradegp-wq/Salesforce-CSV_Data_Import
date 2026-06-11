<h1 align="center">📊 Salesforce CSV Data Import Suite</h1>

<p align="center">
Ferramenta desktop desenvolvida para transformar planilhas Excel em arquivos CSV prontos para importação no Salesforce,
aplicando automaticamente regras de negócio, vínculos entre objetos e ajustes necessários para evitar erros no Data Loader ou Data Import do Salesforce Inspector.
</p>

<p align="center">
A suíte possui duas versões independentes:
<b>PF (Pessoa Física)</b> e <b>PJ (Pessoa Jurídica)</b>.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/PF-Pessoa%20Física-blue">
  <img src="https://img.shields.io/badge/PJ-Pessoa%20Jurídica-green">
  <img src="https://img.shields.io/badge/Linguagem-Python-blue">
  <img src="https://img.shields.io/badge/Interface-Tkinter-lightgrey">
</p>

<hr>

<table width="100%">
<tr>

<td width="100%" valign="top">

<h2>👤 PF - Pessoa Física</h2>

<h3>Objetos processados</h3>

<ul>
<li>Account</li>
<li>Contract</li>
<li>Asset</li>
</ul>

<h3>Principais recursos</h3>

<ul>
<li>Atualização Account</li>
<li>UPSERT por CPF__pc</li>
<li>SOQL automática</li>
<li>Relacionamento Account → Contract → Asset</li>
<li>Tratamento automático de CPF</li>
</ul>

</td>

<td width="100%" valign="top">

<h2>🏢 PJ - Pessoa Jurídica</h2>

<h3>Objetos processados</h3>

<ul>
<li>Contract</li>
<li>Asset</li>
</ul>

<h3>Principais recursos</h3>

<ul>
<li>Sem atualização Account</li>
<li>1 Account → N Contracts</li>
<li>Validação Contract × Asset</li>
<li>Preparado para MultiID futuro</li>
<li>Conversões automáticas PJ</li>
</ul>

</td>

</tr>
</table>

<hr>

<h2>🚀 Como usar</h2>

<ol>
<li>Inserir Account IDs da ORG, baseado no CPF/CNPJ.</li>
<li>Anexar Excel.</li>
<li>Clicar em <b>Processar CSV</b>.</li>
<li>Clicar nos botões que representam os objetos (Account/Contract/Asset)</li>
<li>O CSV vai estar copiado na <b>Área de Transferência</b> (CTRL+C).</li>
<li>Abrir o <b>Data Import</b> do Salesforce Inspector ou no Data Loader.</li>
<li>Colar o que foi copiado (CTRL+V).</li>
<li>Ajustar o que for pedido no Data Loader ou Salesforce Inspector.</li>
</ol>

<hr>

<h2>👤 Módulo Pessoa Física</h2>

<table width="100%">
<tr>

<td width="50%" valign="top">

<h3>📥 LEITURA DE PLANILHA</h3>

<ul>
<li>Importação Excel (.xlsx / .xls)</li>
<li>Detecção automática:</li>
<ul>
<li>Account</li>
<li>Contract</li>
<li>Asset</li>
</ul>
<li>Validação estrutural antes do processamento</li>
</ul>

</td>

<td width="50%" valign="top">

<h3>🔗 VINCULAÇÃO AUTOMÁTICA</h3>

<ul>
<li>Relacionamento automático entre objetos</li>
<li>Distribuição Account IDs</li>
<li>Vínculo Account → Contract → Asset</li>
<li>Consistência automática entre registros</li>
</ul>

</td>

</tr>

<tr>

<td width="50%" valign="top">

<h3>🔄 TRANSFORMAÇÃO DE DADOS</h3>

<ul>
<li>Conversão automática de datas</li>
<li>Padronização CPF</li>
<li>Renomeação automática de campos</li>
<li>Correção de inconsistências</li>
</ul>

</td>

<td width="50%" valign="top">

<h3>📤 EXPORTAÇÃO</h3>

<ul>
<li>Account.csv</li>
<li>Contract.csv</li>
<li>Asset.csv</li>
<li>Codificação UTF-8</li>
<li>Pronto para Data Loader e Inspector</li>
</ul>

</td>

</tr>
</table>

<h2>🧾 ACCOUNT</h2>

<ul>
<li>Campo <b>Id</b> é preenchido com os Account IDs informados</li>
<li>Campo <b>Email</b> é automaticamente renomeado para <b>Email__c</b></li>

<li>Campo <b>CPF__pc</b>:
<ul>
<li>Remove espaços</li>
<li>Garante 11 dígitos (padding com zero à esquerda)</li>
</ul>
</li>

<li><b>RecordTypeId</b> fixo:
<ul><li>0125A0000013RxeQAE</li></ul>
</li>

<li><b>AreaNegocio__c</b> fixado como <b>Leves</b> (quando existente)</li>

<li>Operação esperada:
<ul><li><b>UPSERT via CPF__pc</b></li></ul>
</li>
</ul>

<h2>📄 CONTRACT</h2>

<ul>
<li>Campo <b>AccountId</b> vinculado aos IDs informados</li>
<li>Campo <b>Status</b> fixado como <b>Draft</b></li>

<li><b>IRIS_Categoria_Contrato__c</b> fixo:
<ul><li>2</li></ul>
</li>

<li>Campos de data convertidos para YYYY-MM-DD</li>
<li>Campos booleanos específicos são forçados como <b>TRUE</b></li>

<li><b>RecordTypeId</b> fixo:
<ul><li>012U6000000OTnFIAW</li></ul>
</li>

<li>Operação esperada:
<ul><li><b>INSERT</b></li></ul>
</li>
</ul>

<h2>🚗 ASSET</h2>

<ul>
<li>Campo <b>AccountId</b> vinculado aos IDs informados</li>
<li>Campos de data convertidos para YYYY-MM-DD</li>

<li>Campo <b>RecordType.Name</b> convertido para <b>RecordTypeId</b></li>

<li><b>RecordTypeId</b> fixo:
<ul><li>012HY0000004NyFYAU</li></ul>
</li>

<li>Conversão para Status válido:
<ul>
<li><b>Disponível</b> e <b>Alugado</b> → <b>Locado</b></li>
</ul>
</li>

<li>Operação esperada:
<ul><li><b>UPSERT por chave externa</b></li></ul>
</li>
</ul>

<hr>

<h2>🏢 Módulo Pessoa Jurídica</h2>

<table width="100%">
<tr>

<td width="50%" valign="top">

<h3>📥 LEITURA DE PLANILHA</h3>

<ul>
<li>Importação Excel (.xlsx / .xls)</li>
<li>Detecção automática:</li>
<ul>
<li>Contract</li>
<li>Ativo</li>
</ul>
<li>Validação estrutural antes do processamento</li>
</ul>

</td>

<td width="50%" valign="top">

<h3>🔗 VINCULAÇÃO AUTOMÁTICA</h3>

<ul>
<li>Relacionamento 1 Account → N Contracts</li>
<li>Distribuição automática AccountId</li>
<li>Validação Contract × Asset</li>
<li>Preparado para MultiID futuro</li>
</ul>

</td>

</tr>

<tr>

<td width="50%" valign="top">

<h3>🔄 TRANSFORMAÇÃO DE DADOS</h3>

<ul>
<li>Conversão automática de datas</li>
<li>Tratamento ContractTerm</li>
<li>Renomeação automática</li>
<li>Conversões específicas PJ</li>
</ul>

</td>

<td width="50%" valign="top">

<h3>📤 EXPORTAÇÃO</h3>

<ul>
<li>Contract.csv</li>
<li>Asset.csv</li>
<li>Codificação UTF-8</li>
<li>Pronto para Data Loader e Inspector</li>
</ul>

</td>

</tr>
</table>

<h2>📄 CONTRACT (PJ)</h2>

<ul>
<li>Campo <b>Id</b> removido automaticamente</li>

<li>Relacionamento:
<ul><li><b>1 Account → N Contracts</b></li></ul>
</li>

<li>Campo <b>AccountId</b> distribuído automaticamente</li>
<li>Campo <b>Status</b> fixado como <b>Draft</b></li>

<li><b>IRIS_Categoria_Contrato__c</b> fixo:
<ul><li>2</li></ul>
</li>

<li>Campos de data convertidos para YYYY-MM-DD</li>
<li><b>ContractTerm</b> tratado automaticamente</li>

<li>Campos booleanos:
<ul>
<li>IRIS_CapturaReservaPrimeiraParcela__c = false</li>
<li>IRIS_ReservaPrimeiraParcela__c = false</li>
</ul>
</li>

<li><b>RecordTypeId</b> fixo:
<ul><li>012U6000009ru5eIAA</li></ul>
</li>

<li>Operação esperada:
<ul><li><b>INSERT</b></li></ul>
</li>
</ul>

<h2>🚗 ASSET (PJ)</h2>

<ul>
<li>Campo <b>Id</b> removido automaticamente</li>
<li>Campo <b>AccountId</b> vinculado automaticamente</li>
<li>Campos de data convertidos para YYYY-MM-DD</li>

<li>Campo <b>RecordType.Name</b> convertido para <b>RecordTypeId</b></li>

<li><b>RecordTypeId</b> fixo:
<ul><li>012U6000009ru5JIAQ</li></ul>
</li>

<li>Operação esperada:
<ul><li><b>UPSERT via Placa__c</b></li></ul>
</li>
</ul>

<hr>

<h2>🔍 VALIDAÇÃO CONTRACT × ASSET</h2>

<p>O fluxo PJ valida automaticamente:</p>

<ul>
<li>IRIS_Contrato__r.IRIS_CodigoContratoMasterLocavia__c</li>
<li>IRIS_CodigoContratoMasterLocavia__c</li>
</ul>

<p>Caso Assets apontem contratos inexistentes, o processamento é interrompido.</p>

<hr>

<h2>🔧 RENOMEAÇÕES AUTOMÁTICAS</h2>

<ul>
<li>ContractNumber → _ContractNumber</li>
<li>Account.Name → _Account.Name</li>
<li>IDExternoAX__c → _IDExternoAX__c</li>
<li>EndDate → _EndDate</li>
<li>RecordType.DeveloperName → _RecordType.DeveloperName</li>
<li>IRIS_Codigo_Status_do_Tanque__c → _IRIS_Codigo_Status_do_Tanque__c</li>
<li>IRIS_Codigo_Situacao_do_Agendamento__c → _IRIS_Codigo_Situacao_do_Agendamento__c</li>
</ul>

<hr>

<p align="center">
Automatizando higienização e preparação de dados para cargas Salesforce ☁️
</p>

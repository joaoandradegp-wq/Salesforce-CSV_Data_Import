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

---

<table width="100%">
<tr>

<td width="50%" valign="top">

## 👤 PF — Pessoa Física

Fluxo voltado para atualização e higienização de dados de clientes Pessoa Física.

### Objetos processados

<ul>
<li>Account</li>
<li>Contract</li>
<li>Asset</li>
</ul>

### Principais recursos

<ul>
<li>Atualização Account</li>
<li>UPSERT por CPF__pc</li>
<li>SOQL automática</li>
<li>Relacionamento Account → Contract → Asset</li>
<li>Tratamento automático de CPF</li>
</ul>

</td>

<td width="50%" valign="top">

## 🏢 PJ — Pessoa Jurídica

Fluxo voltado para operações corporativas e gestão de contratos PJ.

### Objetos processados

<ul>
<li>Contract</li>
<li>Asset</li>
</ul>

### Principais recursos

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

---

# 👤 PF — Pessoa Física

## ✨ Funcionalidades

<table width="100%">

<tr>

<td width="25%" valign="top">

### 📥 LEITURA DE PLANILHA

<ul>
<li>Importação Excel (.xlsx / .xls)</li>
<li>Detecção automática:</li>

<ul>
<li>Account</li>
<li>Contract</li>
<li>Asset</li>
</ul>

<li>Validação estrutural</li>

</ul>

</td>

<td width="25%" valign="top">

### 🔗 VINCULAÇÃO AUTOMÁTICA

<ul>

<li>Relacionamento entre objetos</li>

<li>Distribuição Account IDs</li>

<li>Consistência automática</li>

<li>Vínculo Account → Contract → Asset</li>

</ul>

</td>

<td width="25%" valign="top">

### 🔄 TRANSFORMAÇÃO

<ul>

<li>Conversão de datas</li>

<li>Padronização CPF</li>

<li>Renomeação campos</li>

<li>Correção inconsistências</li>

</ul>

</td>

<td width="25%" valign="top">

### 📤 EXPORTAÇÃO

<ul>

<li>Account.csv</li>

<li>Contract.csv</li>

<li>Asset.csv</li>

<li>UTF-8</li>

</ul>

</td>

</tr>

</table>

---

## 🧾 ACCOUNT

<ul>

<li>Campo <b>Id</b> preenchido automaticamente</li>

<li>Email → Email__c</li>

<li>CPF__pc:</li>

<ul>

<li>Remove caracteres</li>

<li>Padroniza formato</li>

<li>Padding automático</li>

</ul>

<li>RecordType fixo</li>

<li>UPSERT via CPF__pc</li>

</ul>

---

## 📄 CONTRACT

<ul>

<li>AccountId automático</li>

<li>Status = Draft</li>

<li>Conversão datas</li>

<li>Flags automáticas</li>

<li>INSERT</li>

</ul>

---

## 🚗 ASSET

<ul>

<li>AccountId automático</li>

<li>Conversão datas</li>

<li>RecordType.Name → RecordTypeId</li>

<li>UPSERT por chave externa</li>

</ul>

---

# 🏢 PJ — Pessoa Jurídica

## ✨ Funcionalidades

<table width="100%">

<tr>

<td width="25%" valign="top">

### 📥 LEITURA DE PLANILHA

<ul>

<li>Importação Excel (.xlsx / .xls)</li>

<li>Detecção automática:</li>

<ul>

<li>Contract</li>

<li>Ativo</li>

</ul>

<li>Validação estrutural</li>

</ul>

</td>

<td width="25%" valign="top">

### 🔗 VINCULAÇÃO AUTOMÁTICA

<ul>

<li>1 Account → N Contracts</li>

<li>Relacionamento Assets</li>

<li>Validação cruzada</li>

<li>Preparado MultiID</li>

</ul>

</td>

<td width="25%" valign="top">

### 🔄 TRANSFORMAÇÃO

<ul>

<li>Conversão datas</li>

<li>Limpeza ContractTerm</li>

<li>Renomeações automáticas</li>

<li>Conversões PJ</li>

</ul>

</td>

<td width="25%" valign="top">

### 📤 EXPORTAÇÃO

<ul>

<li>Contract.csv</li>

<li>Asset.csv</li>

<li>UTF-8</li>

<li>Pronto Data Loader / Inspector</li>

</ul>

</td>

</tr>

</table>

---

## 📄 CONTRACT

<ul>

<li>Remove Id automaticamente</li>

<li>Relacionamento:</li>

<ul>
<li>1 Account → N Contracts</li>
</ul>

<li>Status = Draft</li>

<li>IRIS_Categoria_Contrato__c = 2</li>

<li>Conversão automática de datas</li>

<li>ContractTerm tratado automaticamente</li>

<li>Flags convertidas:</li>

<ul>

<li>IRIS_CapturaReservaPrimeiraParcela__c = false</li>

<li>IRIS_ReservaPrimeiraParcela__c = false</li>

</ul>

<li>INSERT</li>

</ul>

---

## 🚗 ASSET

<ul>

<li>Remove Id automaticamente</li>

<li>AccountId automático</li>

<li>Conversão datas</li>

<li>RecordType.Name → RecordTypeId</li>

<li>UPSERT via Placa__c</li>

</ul>

---

## 🔍 VALIDAÇÃO CONTRACT × ASSET

Antes da exportação o PJ valida automaticamente:

<ul>

<li>IRIS_Contrato__r.IRIS_CodigoContratoMasterLocavia__c</li>

<li>IRIS_CodigoContratoMasterLocavia__c</li>

</ul>

Caso Assets apontem contratos inexistentes o processamento é interrompido.

---

## 🔧 RENOMEAÇÕES AUTOMÁTICAS

<ul>

<li>ContractNumber → _ContractNumber</li>

<li>Account.Name → _Account.Name</li>

<li>IDExternoAX__c → _IDExternoAX__c</li>

<li>EndDate → _EndDate</li>

<li>RecordType.DeveloperName → _RecordType.DeveloperName</li>

<li>IRIS_Codigo_Status_do_Tanque__c → _IRIS_Codigo_Status_do_Tanque__c</li>

<li>IRIS_Codigo_Situacao_do_Agendamento__c → _IRIS_Codigo_Situacao_do_Agendamento__c</li>

</ul>

---

## 🚀 Como usar

1. Inserir Account IDs

2. Anexar Excel

3. Processar CSV

4. Importar no Salesforce

5. Utilizar Data Loader ou Inspector

---

<p align="center">
Automatizando higienização e preparação de dados para cargas Salesforce ☁️
</p>

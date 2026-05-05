<h1 align="center">📊 Excel to Salesforce CSV Converter</h1>

<p align="center">
Aplicação desktop desenvolvida para automatizar a preparação de dados para importação no Salesforce.
O sistema transforma planilhas Excel em arquivos CSV estruturados, aplicando regras de negócio, validações e vínculos entre objetos como Account, Contract e Asset.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Ativo-success">
  <img src="https://img.shields.io/badge/Linguagem-Python-blue">
  <img src="https://img.shields.io/badge/Interface-Tkinter-lightgrey">
</p>

---

## ✨ Funcionalidades

<table style="border: none; border-collapse: collapse;">
<tr>
<td width="50%" valign="top" style="border: none; padding: 15px;">

### 📥 IMPORTAÇÃO DE PLANILHA

<ul>
<li>Leitura de arquivos Excel (.xlsx / .xls)</li>
<li>Identificação automática das abas:</li>
<ul>
<li>Account</li>
<li>Contract</li>
<li>Ativo (Asset)</li>
</ul>
<li>Validação estrutural antes do processamento</li>
</ul>

</td>

<td width="50%" valign="top" style="border: none; padding: 15px;">

### 🧠 REGRAS DE NEGÓCIO

<ul>
<li>Vinculação automática entre objetos via AccountId</li>
<li>Normalização de dados (CPF, datas, textos)</li>
<li>Aplicação de valores fixos obrigatórios</li>
<li>Garantia de consistência entre registros</li>
</ul>

</td>
</tr>

<tr>
<td width="50%" valign="top" style="border: none; padding: 15px;">

### 🔄 TRANSFORMAÇÃO DE DADOS

<ul>
<li>Conversão de datas para padrão Salesforce (YYYY-MM-DD)</li>
<li>Renomeação automática de campos problemáticos</li>
<li>Tratamento de colunas bloqueadas para update</li>
<li>Padronização de campos como Email e CPF</li>
</ul>

</td>

<td width="50%" valign="top" style="border: none; padding: 15px;">

### 📊 GERAÇÃO DE CSV

<ul>
<li>Geração automática de 3 arquivos:</li>
<ul>
<li>Account.csv</li>
<li>Contract.csv</li>
<li>Asset.csv</li>
</ul>
<li>Codificação UTF-8 (compatível com Salesforce)</li>
<li>Arquivos prontos para importação via Data Loader</li>
</ul>

</td>
</tr>

<tr>
<td width="50%" valign="top" style="border: none; padding: 15px;">

### 🔍 GERAÇÃO DE SOQL

<ul>
<li>Extração automática de CPFs da planilha</li>
<li>Remoção de formatação e normalização</li>
<li>Geração de query pronta:</li>
<ul>
<li>SELECT Id, Name, CPF__pc FROM Account</li>
</ul>
<li>Resultado copiado direto para área de transferência</li>
</ul>

</td>

<td width="50%" valign="top" style="border: none; padding: 15px;">

### 🖥️ INTERFACE

<ul>
<li>Interface simples e direta (Tkinter)</li>
<li>Contador automático de IDs</li>
<li>Botões dinâmicos para copiar CSVs</li>
<li>Status visual de processamento</li>
</ul>

</td>
</tr>
</table>

---

## ⚙️ Regras de Negócio Aplicadas

### 🔗 Vinculação entre objetos

<ul>
<li>Todos os registros são vinculados via <b>AccountId</b></li>
<li>Os IDs informados são distribuídos automaticamente entre:</li>
<ul>
<li>Account</li>
<li>Contract</li>
<li>Asset</li>
</ul>
</ul>

---

### 🧾 Account

<ul>
<li>Recebe os IDs informados manualmente</li>
<li>Campo <b>CPF__pc</b> normalizado (11 dígitos)</li>
<li>Email padronizado para <b>Email__c</b></li>
<li>Campo fixo:</li>
<ul>
<li>RecordTypeId = 0125A0000013RxeQAE</li>
<li>AreaNegocio__c = Leves</li>
</ul>
<li>Operação esperada: <b>UPSERT via CPF__pc</b></li>
</ul>

---

### 📄 Contract

<ul>
<li>Vinculado automaticamente via <b>AccountId</b></li>
<li>Campos padrão definidos:</li>
<ul>
<li>Status = Draft</li>
<li>IRIS_Categoria_Contrato__c = 2</li>
<li>RecordTypeId = 012U6000000OTnFIAW</li>
</ul>
<li>Datas convertidas automaticamente</li>
<li>Flags obrigatórias definidas como TRUE</li>
<li>Operação esperada: <b>INSERT</b></li>
</ul>

---

### 🚗 Asset

<ul>
<li>Vinculado automaticamente via <b>AccountId</b></li>
<li>Conversão automática de datas</li>
<li>Mapeamento de RecordType aplicado</li>
<li>RecordTypeId fixo:</li>
<ul>
<li>012HY0000004NyFYAU</li>
</ul>
<li>Operação esperada: <b>UPSERT via chave externa (ex: Placa__c)</b></li>
</ul>

---

### 🔧 Ajustes técnicos automáticos

<ul>
<li>Renomeação de campos que bloqueiam atualização (prefixo "_")</li>
<li>Correção de inconsistências de dados</li>
<li>Validação de quantidade de registros vs IDs</li>
<li>Remoção automática de CSVs antigos antes de novo processamento</li>
</ul>

---

## 🚀 Como usar

1. Insira os Account IDs (um por linha)  
2. Clique em **Anexar Arquivo**  
3. (Opcional) Clique em **Gerar SOQL por CPF**  
4. Clique em **Processar e Salvar CSV**  
5. Utilize os botões para copiar os CSVs  

---

## 📸 Preview

<p align="center">
  <img width="500" src="https://via.placeholder.com/500x300?text=Preview+do+Sistema" />
</p>

---

## 📥 Download

<p align="center">
  <a href="#">
    <img src="https://img.shields.io/badge/Download-CSV%20Converter-blue?style=for-the-badge">
  </a>
</p>

---

<p align="center">
Automatizando processos que normalmente seriam feitos manualmente no Excel
</p>

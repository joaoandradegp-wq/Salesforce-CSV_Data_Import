<h1 align="center">📊 Salesforce XLSX Data Import</h1>

<p align="center">
Ferramenta desktop desenvolvida para transformar planilhas Excel em arquivos CSV prontos para importação no Salesforce,
aplicando automaticamente regras de negócio, vínculos entre objetos e ajustes necessários para evitar erros no Data Loader.
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

### 📥 LEITURA DE PLANILHA

<ul>
<li>Importação de arquivos Excel (.xlsx / .xls)</li>
<li>Detecção automática das abas necessárias:</li>
<ul>
<li>Account</li>
<li>Contract</li>
<li>Ativo (Asset)</li>
</ul>
<li>Validação de estrutura antes do processamento</li>
</ul><br>

</td>

<td width="50%" valign="top" style="border: none; padding: 15px;">

### 🔗 VINCULAÇÃO AUTOMÁTICA

<ul>
<li>Relacionamento automático entre objetos</li>
<li>Distribuição dos Account IDs informados</li>
<li>Garantia de consistência entre os dados</li>
</ul>

</td>
</tr>

<tr>
<td width="50%" valign="top" style="border: none; padding: 15px;">

### 🔄 TRANSFORMAÇÃO DE DADOS

<ul>
<li>Conversão de datas para padrão Salesforce</li>
<li>Padronização de CPF</li>
<li>Renomeação automática de campos</li>
<li>Correção de inconsistências comuns</li>
</ul>

</td>

<td width="50%" valign="top" style="border: none; padding: 15px;">

### 📊 EXPORTAÇÃO

<ul>
<li>Geração automática de:</li>
<ul>
<li>Account.csv</li>
<li>Contract.csv</li>
<li>Asset.csv</li>
</ul>
<li>Arquivos prontos para Data Loader</li>
<li>Codificação UTF-8</li><br>
</ul>

</td>
</tr>
</table>

---

## ⚙️ Regras de Negócio

### 🧾 ACCOUNT

<ul>
<li>Campo <b>Id</b> é preenchido com os Account IDs informados</li>

<li>Campo <b>Email</b> é automaticamente renomeado para <b>Email__c</b></li>

<li>Campo <b>CPF__pc</b>:</li>
<ul>
<li>Remove espaços</li>
<li>Remove formatação (não numéricos)</li>
<li>Garante 11 dígitos (padding com zero à esquerda)</li>
</ul>

<li>Campo <b>RecordTypeId</b> fixo:</li>
<ul>
<li>0125A0000013RxeQAE</li>
</ul>

<li>Campo <b>AreaNegocio__c</b>:</li>
<ul>
<li>Definido como "Leves" quando existir na planilha</li>
</ul>

<li>Operação esperada:</li>
<ul>
<li><b>UPSERT via CPF__pc</b></li>
</ul>

</ul>

---

### 📄 CONTRACT

<ul>
<li>Campo <b>AccountId</b> vinculado automaticamente aos IDs informados</li>

<li>Campo <b>Status</b> fixado como:</li>
<ul>
<li>Draft</li>
</ul>

<li>Campo <b>IRIS_Categoria_Contrato__c</b>:</li>
<ul>
<li>Valor fixo: 2</li>
</ul>

<li>Campos de data:</li>
<ul>
<li>Convertidos para formato <b>YYYY-MM-DD</b></li>
</ul>

<li>Campos booleanos específicos:</li>
<ul>
<li>IRIS_CapturaReservaPrimeiraParcela__c = TRUE</li>
<li>IRIS_ReservaPrimeiraParcela__c = TRUE</li>
</ul>

<li>Campo <b>RecordTypeId</b> fixo:</li>
<ul>
<li>012U6000000OTnFIAW</li>
</ul>

<li>Operação esperada:</li>
<ul>
<li><b>INSERT</b></li>
</ul>

</ul>

---

### 🚗 ASSET

<ul>
<li>Campo <b>AccountId</b> vinculado automaticamente aos IDs informados</li>

<li>Campos de data:</li>
<ul>
<li>Convertidos para formato <b>YYYY-MM-DD</b></li>
</ul>

<li>Campo <b>RecordType.Name</b>:</li>
<ul>
<li>Convertido automaticamente para <b>RecordTypeId</b></li>
</ul>

<li>Campo <b>RecordTypeId</b> fixo:</li>
<ul>
<li>012HY0000004NyFYAU</li>
</ul>

<li>Operação esperada:</li>
<ul>
<li><b>UPSERT via chave externa (ex: Placa__c)</b></li>
</ul>

</ul>

---

### 🔧 RENOMEAÇÕES AUTOMÁTICAS

Alguns campos são renomeados automaticamente para evitar conflitos ou bloqueios de atualização no Salesforce:

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

## 🔍 Geração de SOQL

<ul>
<li>Extrai automaticamente CPFs da planilha</li>
<li>Remove formatação e padroniza valores</li>
<li>Gera query pronta:</li>
</ul>

<pre>
SELECT Id, Name, CPF__pc
FROM Account
WHERE CPF__pc IN (...)
ORDER BY Name
</pre>

<ul>
<li>Resultado copiado automaticamente para a área de transferência</li>
</ul>

---

## 🚀 Como usar

1. Insira os Account IDs (um por linha)  
2. Clique em <b>Anexar Arquivo</b>  
3. (Opcional) Clique em <b>Gerar SOQL por CPF</b>  
4. Clique em <b>Processar e Salvar CSV</b>  
5. Utilize os botões para copiar os arquivos  

---

## 📥 Download

<p align="center">
  <a href="#">
    <img src="https://img.shields.io/badge/Download-CSV%20Converter-blue?style=for-the-badge">
  </a>
</p>

---

<p align="center">
Automatizando processos de importação que normalmente seriam manuais no Salesforce ☁️
</p>

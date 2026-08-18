<h1 align="center">📊 Salesforce CSV Data Import Suite</h1>

<p align="center">
Ferramenta desktop desenvolvida para transformar planilhas Excel em arquivos CSV prontos para importação no Salesforce,
aplicando automaticamente regras de negócio, vínculos entre objetos e ajustes necessários para evitar erros no Data Loader ou Data Import do Salesforce Inspector.
</p>

<p align="center">
A suíte possui duas versões independentes: <b>PF (Pessoa Física)</b> e <b>PJ (Pessoa Jurídica)</b>.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Ativo-success">
  <img src="https://img.shields.io/badge/Plataforma-Windows-blue">
  <img src="https://img.shields.io/badge/Tipo-Validador%20de%20Dados-purple">
  <img src="https://img.shields.io/badge/Linguagem-Python-orange">
  <img src="https://img.shields.io/badge/Interface-Tkinter-lightgrey">
</p>

---

## ⬇️ Releases

| Versão | Módulo | Descrição | Download |
|--------|--------|-----------|----------|
| 1.6.3 | PF | Pessoa Física | [Clique aqui](https://github.com/joaoandradegp-wq/Salesforce-CSV_Data_Import/releases/download/1.6.3/SF-DataImport_1.6.3-Multi.rar) |
| 1.6.2.1 | PJ | Pessoa Jurídica | [Clique aqui](https://github.com/joaoandradegp-wq/Salesforce-CSV_Data_Import/releases/download/1.7/SF-DataImport_PF-PJ.rar) |
| 1.0 | SOQL Generator | Gerador de consultas SOQL por múltiplos IDs | [Clique aqui](https://github.com/joaoandradegp-wq/Salesforce-CSV_Data_Import/releases/download/1.0/SOQL.exe) |
| 1.0 | Update Contract Database | Preparação de dados para atualização de Contracts | [Clique aqui](https://github.com/joaoandradegp-wq/Salesforce-CSV_Data_Import/releases/download/1.0/Update_Contract_PF.exe) |

> **SOQL Generator** e **Update Contract Database** são ferramentas independentes.

---

## 🧭 Comparativo PF × PJ

| | 👤 PF — Pessoa Física | 🏢 PJ — Pessoa Jurídica |
|---|---|---|
| **Foco** | Preparação de dados de clientes Pessoa Física | Preparação de Contracts e Assets |
| **Objetos** | Account, Contract, Asset | Account, Contract, Asset |
| **Relacionamento** | 1 Account → 1 Contract / 1 Asset | 1 Account → N Contracts / N Assets |
| **Recursos** | · UPDATE opcional de Account <br>· UPSERT de Asset por `Placa__c` <br>· SOQL por CPF <br>· Tratamento de CPF | · Distribuição automática de `AccountId` <br>· Validação Contract × Asset <br>· UPSERT de Asset por `Placa__c` |

---

## 🚀 Como usar

| Passo | Ação |
|---|---|
| 1 | Inserir os Account IDs da ORG |
| 2 | Anexar o arquivo Excel |
| 3 | Clicar em **Processar e Salvar CSV** |
| 4 | Selecionar o objeto desejado |
| 5 | O CSV é copiado para a Área de Transferência |
| 6 | Abrir o Data Import do Salesforce Inspector ou o Data Loader |
| 7 | Colar com **CTRL+V** |
| 8 | Ajustar o que for solicitado pelo Salesforce |

---

## 👤 Módulo Pessoa Física

### Leitura de planilha
Importação **.xlsx / .xls** com abas obrigatórias `Account`, `Contract`, `Ativo`, validação de abas e de quantidade de registros.

### Vinculação automática
Account ID informado pelo usuário · **1 Account → 1 Contract** · **1 Account → 1 Asset** · vínculo automático pelo `AccountId`.

### Transformação de dados
Conversão de datas · padronização de CPF · renomeação de campos · conversão de Status do Asset · aplicação de `RecordTypeId`.

### Exportação
`Account.csv` · `Contract.csv` · `Asset.csv` — codificação UTF-8.

### Regras por objeto

| Objeto | Campo | Regra |
|---|---|---|
| **Account** | `Id` | Recebe os Account IDs informados (quantidade deve bater com os registros da aba) |
| | `Email` → `Email__c` | Renomeação |
| | `CPF__pc` | Remove não numéricos, garante 11 dígitos, zeros à esquerda |
| | `RecordTypeId` | `0125A0000013RxeQAE` |
| | `AreaNegocio__c` | `Leves` |
| | Operação | UPDATE opcional |
| **Contract** | `Id` | Recebe ID da Conta |
| | `AccountId` | Recebe os IDs informados (1 Account → 1 Contract) |
| | `Status` | `Draft` |
| | `IRIS_Categoria_Contrato__c` | `2` |
| | Datas | Convertidas para `YYYY-MM-DD` |
| | `IRIS_CapturaReservaPrimeiraParcela__c` | `TRUE` |
| | `IRIS_ReservaPrimeiraParcela__c` | `TRUE` |
| | `RecordTypeId` | `012U6000000OTnFIAW` |
| | Operação | INSERT |
| **Asset** | `Id` | Recebe ID da Conta |
| | `AccountId` | Recebe os IDs informados (1 Account → 1 Asset) |
| | Datas | Convertidas para `YYYY-MM-DD` |
| | `RecordType.Name` → `RecordTypeId` | Renomeação |
| | `RecordTypeId` | `012HY0000004NyFYAU` |
| | Status | `Disponível` → `Locado`; `Alugado` → `Locado` |
| | Operação | UPSERT via `Placa__c` |

### 🔎 SOQL por CPF
Localiza a aba `Account`/`Clientes`, usa o campo `CPF__pc`, remove não numéricos, padroniza para 11 dígitos, remove duplicidades e copia a consulta para a Área de Transferência.

```sql
SELECT Id, Name, CPF__pc
FROM Account
WHERE CPF__pc IN (...)
ORDER BY Name
```

---

## 🏢 Módulo Pessoa Jurídica

### Leitura de planilha
Importação **.xlsx / .xls** com abas obrigatórias `Account`, `Contract`, `Ativo`, com validação de abas.

### Vinculação automática
**1 Account → N Contracts** · **1 Account → N Assets** · distribuição automática de `AccountId` · validação Contract × Asset.

### Transformação de dados
Conversão de datas · tratamento de `ContractTerm` · renomeação de campos · aplicação de `RecordTypeId` · conversões específicas.

### Exportação
`Account.csv` · `Contract.csv` · `Asset.csv` — codificação UTF-8.

### Regras por objeto

| Objeto | Campo | Regra |
|---|---|---|
| **Account** | `Id` | Recebe o Account ID informado |
| | `Email` → `Email__c` | Renomeação |
| | `CPF__pc` | Tratamento específico |
| | `RecordTypeId` | `0125A0000013RibQAE` |
| | `AreaNegocio__c` | `Leves` |
| **Contract** | `Id` | Recebe ID da Conta |
| | `AccountId` | Distribuído automaticamente (1 Account → N Contracts) |
| | `Status` | `Draft` |
| | `IRIS_Categoria_Contrato__c` | `2` |
| | Datas | Convertidas para `YYYY-MM-DD` |
| | `ContractTerm` | Tratado automaticamente |
| | Valor `0` | Convertido para vazio |
| | `IRIS_CapturaReservaPrimeiraParcela__c` | `false` |
| | `IRIS_ReservaPrimeiraParcela__c` | `false` |
| | `RecordTypeId` | `012U6000009ru5eIAA` |
| | Operação | INSERT |
| **Asset** | `Id` | Recebe ID da Conta |
| | `AccountId` | Distribuído automaticamente (1 Account → N Assets) |
| | Datas | Convertidas para `YYYY-MM-DD` |
| | `RecordType.Name` → `RecordTypeId` | Renomeação |
| | `RecordTypeId` | `012U6000009ru5JIAQ` |
| | Operação | UPSERT via `Placa__c` |

### 🔍 Validação Contract × Asset
Compara `IRIS_Contrato__r.IRIS_CodigoContratoMasterLocavia__c` com `IRIS_CodigoContratoMasterLocavia__c`. Se um Asset referenciar um contrato inexistente, o processamento é interrompido.

### 🔧 Renomeações automáticas

| Origem | Destino |
|---|---|
| `ContractNumber` | `_ContractNumber` |
| `Account.Name` | `_Account.Name` |
| `IDExternoAX__c` | `_IDExternoAX__c` |
| `EndDate` | `_EndDate` |
| `RecordType.DeveloperName` | `_RecordType.DeveloperName` |
| `IRIS_Codigo_Status_do_Tanque__c` | `_IRIS_Codigo_Status_do_Tanque__c` |
| `IRIS_Codigo_Situacao_do_Agendamento__c` | `_IRIS_Codigo_Situacao_do_Agendamento__c` |

### 🔎 SOQL por CNPJ
Opção **Gerar SOQL por CNPJ**: localiza a aba `Account`/`Clientes`, usa o campo `CPF__pc`, remove não numéricos, padroniza para 11 dígitos, remove duplicidades e copia para a Área de Transferência.

> A interface apresenta a opção como CNPJ, porém o código atual utiliza o campo `CPF__pc`.

### ⚠️ Status do Contract
O programa gera `Status = Draft`. A conversão posterior de Draft para Ativo **não** é realizada pelo programa.

---

## 🔎 SOQL Generator

Ferramenta independente para geração de consultas SOQL.

| Passo | Ação |
|---|---|
| 1 | Inserir os IDs |
| 2 | Definir o limite por consulta |
| 3 | Clicar em **GERAR PARTES** |
| 4 | Selecionar a parte desejada |
| 5 | Copiar a consulta gerada |

**Recursos:** interface gráfica em Tkinter · IDs separados por espaços, vírgulas ou ponto e vírgula · limite configurável (padrão de 500 IDs) · divisão automática das consultas · botões individuais por parte · cópia automática para a Área de Transferência.

**Consulta:** utiliza o objeto `Contract` e o relacionamento com `Opportunity`, com campos `IRIS_Opportunity__r.Id` e `Id`, filtrando e ordenando por `IRIS_Opportunity__r.Id`.

---

## 🔄 Update Contract Database

Ferramenta independente para preparação de dados do objeto Contract.

| Passo | Ação |
|---|---|
| 1 | Selecionar o arquivo XLSX |
| 2 | Processar a planilha |
| 3 | Os dados são tratados automaticamente |
| 4 | Uma aba `Salesforce` é criada |
| 5 | O arquivo tratado é salvo |

### De/Para de campos

| Origem | Salesforce |
|--------|------------|
| SF Id Contrato | `id` |
| Locavia Data de início do contrato | `StartDate` |
| Locavia Status Contrato | `Status` |
| Data Cancelamento | `IRIS_DataCancelamento__c` |

Datas convertidas para `YYYY-MM-DD`.

### Mapeamento de Status

| Origem | Salesforce |
|--------|------------|
| Em Vigência | `Activated` |
| Aberto | `Draft` |
| Assinado | `Draft` |
| Em Assinatura | `Draft` |
| *(demais valores)* | Permanecem inalterados |

A aba `Salesforce` gerada contém: `id`, `StartDate`, `Status`, `IRIS_DataCancelamento__c`.

### Comparação com execução anterior
Quando existe uma execução anterior, os registros são comparados pelo `id`, considerando `StartDate`, `Status` e `IRIS_DataCancelamento__c`. São apresentados: total de registros, novos registros e registros atualizados.

### Log
Registrado em `log_atualizacoes.txt`: data da execução, total de registros, novos registros e registros atualizados.

### Arquivo de saída
Salvo no formato `DD-MM-AAAA.xlsx`.

---

### 📦 Dependências

| Ferramenta | Dependências |
|---|---|
| Data Import (PF/PJ) | Python · Tkinter · Pandas |
| SOQL Generator | Python · Tkinter |
| Update Contract Database | Python · Tkinter · openpyxl |

---

<p align="center">
Automatizando higienização, preparação, consulta e atualização de dados para cargas Salesforce. ☁️
</p>

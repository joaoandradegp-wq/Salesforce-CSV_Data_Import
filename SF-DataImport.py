import re
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import os

# ==================== VARIÁVEIS GLOBAIS ====================

caminho_arquivo = None
pasta_saida = None
processado = False
VERSAO = "1.7.0"

# Diferenças entre os produtos concentradas aqui
PRODUTOS = {
    "LIVRE": {
        "rt_account": "0125A0000013RxeQAE",
        "rt_contract": "012U6000000OTnFIAW",
        "rt_asset": "012HY0000004NyFYAU",
        "reserva_parcela": "TRUE",
        "rotulo_doc": "CPF",
        "label_ids": "Insira os Account IDs (1 por linha):",
        "botoes_csv": ["Account", "Contract", "Asset"],
        "obs": (
            "1- Account  -> UPDATE (Opcional)\n"
            "2- Contract -> INSERT\n"
            "3- Asset    -> UPSERT -> Placa__c\n\n"
        ),
    },
    "FLEET": {
        "rt_account": "0125A0000013RibQAE",
        "rt_contract": "012U6000009ru5eIAA",
        "rt_asset": "012U6000009ru5JIAQ",
        "reserva_parcela": "false",
        "rotulo_doc": "CNPJ",
        "label_ids": "Insira os Account IDs (1 por linha, na mesma ordem da aba Account):",
        "botoes_csv": ["Contract", "Asset"],
        "obs": (
            "1- Contract -> INSERT\n"
            "2- Asset    -> UPSERT -> Placa__c\n\n"
            "Obs: FLEET converte automático a inserção do Status 'Draft' para\n"
            "'Ativo', no Contrato (Contract).\n"
            "Obs: com mais de 1 conta, as abas Account e Contract precisam\n"
            "estar na mesma ordem."
        ),
    },
}

TERMOS_VALIDOS = {12, 24, 36, 48}

# Placa antiga (AAA-1234 / AAA1234) ou Mercosul (AAA1B23)
RE_PLACA = re.compile(r"^[A-Z]{3}-?[0-9]{4}$|^[A-Z]{3}[0-9][A-Z][0-9]{2}$")
RE_SO_NUMERO = re.compile(r"^[0-9]+$")

# ==================== FUNÇÕES DE UTILIDADE ====================

def produto_atual():
    p = combo_produto.get().strip()
    return p if p in PRODUTOS else None


def exigir_produto():
    p = produto_atual()
    if not p:
        messagebox.showerror("Erro", "Selecione o produto (LIVRE ou FLEET).")
    return p


def titulo_janela():
    p = produto_atual()
    parte = f" {p} - {VERSAO}" if p else f" {VERSAO}"
    root.title("Data Import" + parte + " - Aggrandize - João Márcio Bicalho Andrade")


def resetar_pos_digitacao():
    global processado
    limpar_csvs()
    processado = False
    for w in frame_botoes_csv.winfo_children():
        w.destroy()


def gerar_soql_por_cpf():
    if not caminho_arquivo:
        return

    prod = exigir_produto()
    if not prod:
        return
    rotulo = PRODUTOS[prod]["rotulo_doc"]

    try:
        xls = pd.ExcelFile(caminho_arquivo)

        aba_alvo = None
        for nome in xls.sheet_names:
            if "account" in nome.lower() or "clientes" in nome.lower():
                aba_alvo = nome
                break

        if not aba_alvo:
            messagebox.showerror(
                "Erro",
                "Nenhuma aba contendo 'Account' ou 'Clientes' foi encontrada."
            )
            return

        df = pd.read_excel(xls, sheet_name=aba_alvo)

        if "CPF__pc" not in df.columns:
            messagebox.showerror(
                "Erro",
                "A coluna CPF__pc não foi encontrada na aba selecionada."
            )
            return

        docs = (
            df["CPF__pc"]
            .dropna()
            .astype(str)
            .str.replace(r"\D", "", regex=True)
            .apply(lambda x: x.zfill(11))
            .unique()
            .tolist()
        )

        if not docs:
            messagebox.showerror("Erro", f"Nenhum {rotulo} válido encontrado.")
            return

        lista_docs = ", ".join(f"'{c}'" for c in docs)

        soql = (
            "SELECT Id, Name, CPF__pc\n"
            "FROM Account\n"
            f"WHERE CPF__pc IN ({lista_docs})\n"
            "ORDER BY Name"
        )

        root.clipboard_clear()
        root.clipboard_append(soql)
        root.update()

        messagebox.showinfo(
            "SOQL copiado",
            f"SOQL gerado com {len(docs)} {rotulo}(s) e copiado para a área de transferência."
        )

    except Exception as e:
        messagebox.showerror("Erro ao gerar SOQL", str(e))


def atualizar_botao_soql():
    if "btn_soql_cpf" not in globals():
        return

    ids_preenchidos = any(
        l.strip() for l in text_contas.get("1.0", tk.END).splitlines()
    )

    if produto_atual() and caminho_arquivo and not ids_preenchidos:
        if not btn_soql_cpf.winfo_ismapped():
            btn_soql_cpf.pack(side=tk.LEFT, padx=5)
    else:
        if btn_soql_cpf.winfo_ismapped():
            btn_soql_cpf.pack_forget()


def atualizar_contador_ids(event=None):
    root.after(1, lambda: _contar_ids())

def _contar_ids():
    linhas = text_contas.get("1.0", tk.END).splitlines()
    total = sum(1 for l in linhas if l.strip())
    label_contador.config(text=str(total))

def centralizar_janela(root, largura, altura):
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (largura // 2)
    y = (root.winfo_screenheight() // 2) - (altura // 2)
    root.geometry(f"{largura}x{altura}+{x}+{y}")

def limpar_csvs():
    if not pasta_saida:
        return
    for nome in ["Account.csv", "Contract.csv", "Asset.csv"]:
        caminho = os.path.join(pasta_saida, nome)
        if os.path.exists(caminho):
            try:
                os.remove(caminho)
            except:
                pass

def resetar_interface(*args):
    global caminho_arquivo, pasta_saida, processado
    limpar_csvs()
    caminho_arquivo = None
    pasta_saida = None
    processado = False
    label_status.config(text="Nenhum arquivo anexado", fg="red")
    label_contador.config(text="0")
    for w in frame_botoes_csv.winfo_children():
        w.destroy()
    atualizar_botao_soql()

def ao_fechar():
    limpar_csvs()
    root.destroy()

def ao_trocar_produto(event=None):
    global processado
    limpar_csvs()
    processado = False
    for w in frame_botoes_csv.winfo_children():
        w.destroy()

    prod = produto_atual()
    if prod:
        cfg = PRODUTOS[prod]
        label_ids.config(text=cfg["label_ids"])
        btn_soql_cpf.config(text=f"Gerar SOQL por {cfg['rotulo_doc']}")
        texto_obs = cfg["obs"]
    else:
        texto_obs = ""

    text_obs.config(state=tk.NORMAL)
    text_obs.delete("1.0", tk.END)
    text_obs.insert(tk.END, texto_obs)
    text_obs.config(state=tk.DISABLED)

    titulo_janela()
    atualizar_botao_soql()

# ==================== REGRAS DE VALIDAÇÃO DE CAMPOS ====================

def _texto_limpo(v):
    """Valor da célula como texto; 12.0 vira '12'; vazio/NaN vira ''."""
    if pd.isna(v):
        return ""
    if isinstance(v, float) and v.is_integer():
        return str(int(v))
    return str(v).strip()


def _final_placa_invalido(v):
    t = _texto_limpo(v).upper()
    if t == "":
        return False
    return not (RE_SO_NUMERO.match(t) or RE_PLACA.match(t))


def _mensalidade_invalida(v):
    t = _texto_limpo(v)
    if t == "" or t.upper() in ("NULL", "NAN", "NONE"):
        return True
    t = t.replace("R$", "").strip()
    if "," in t:
        t = t.replace(".", "").replace(",", ".")
    try:
        return float(t) == 0
    except ValueError:
        return False


def _data_pagamento_invalida(serie):
    """Preenchida e (não é data ou ano < 2000)."""
    dt = pd.to_datetime(serie, errors="coerce")
    preenchido = serie.apply(lambda v: _texto_limpo(v) != "")
    return preenchido & (dt.isna() | (dt.dt.year < 2000))


def ignorar_se_invalido(df, coluna, func_serie, motivo, nome_aba, avisos):
    """Se qualquer linha for inválida, renomeia a coluna inteira para _<coluna>."""
    if coluna not in df.columns:
        return
    if func_serie(df[coluna]).any():
        df.rename(columns={coluna: "_" + coluna}, inplace=True)
        avisos.append(f"{nome_aba}: {coluna} ({motivo}) -> renomeado para _{coluna}")


def tratar_contract_term(df, avisos):
    """ContractTerm precisa ser 12/24/36/48. Se não for, tenta copiar de
    IRIS_Periodo_Total__c (se for válido lá). Se mesmo assim sobrar linha
    inválida, renomeia a coluna para _ContractTerm."""
    if "ContractTerm" not in df.columns:
        return

    termo = pd.to_numeric(df["ContractTerm"], errors="coerce")
    valido = termo.isin(TERMOS_VALIDOS)
    copiados = 0

    if "IRIS_Periodo_Total__c" in df.columns:
        periodo = pd.to_numeric(df["IRIS_Periodo_Total__c"], errors="coerce")
        copiar = ~valido & periodo.isin(TERMOS_VALIDOS)
        copiados = int(copiar.sum())
        termo = termo.where(~copiar, periodo)
        valido = termo.isin(TERMOS_VALIDOS)

    if valido.all():
        df["ContractTerm"] = termo.astype("Int64")
        if copiados:
            avisos.append(
                f"Contract: ContractTerm copiado de IRIS_Periodo_Total__c em {copiados} linha(s)"
            )
    else:
        df.rename(columns={"ContractTerm": "_ContractTerm"}, inplace=True)
        avisos.append(
            "Contract: ContractTerm fora de 12/24/36/48 e sem valor válido em "
            "IRIS_Periodo_Total__c -> renomeado para _ContractTerm"
        )


def aplicar_regras_de_campos(df, nome_aba, avisos):
    ignorar_se_invalido(
        df, "IRIS_DataPrimeiroPagamento__c", _data_pagamento_invalida,
        "data inválida/anterior a 2000", nome_aba, avisos
    )
    ignorar_se_invalido(
        df, "IRIS_Final_da_Placa__c", lambda s: s.apply(_final_placa_invalido),
        "fora do formato número/placa", nome_aba, avisos
    )
    ignorar_se_invalido(
        df, "IRIS_Valor_Mensalidade__c", lambda s: s.apply(_mensalidade_invalida),
        "branco/nulo/zerado/NULL", nome_aba, avisos
    )

# ==================== FLEET: VÍNCULO CONTA X CONTRATO ====================

def mapear_account_ids_pj(df_account, df_contract, ids):
    """Devolve o AccountId de cada linha da aba Contract.
    As contas são identificadas por Account.Name, na ordem em que aparecem
    na aba Contract, e essa ordem precisa ser a mesma da aba Account."""
    n = len(df_contract)

    if len(ids) == 1:
        return [ids[0]] * n

    if "Account.Name" not in df_contract.columns:
        # sem Account.Name não há como agrupar: mantém a distribuição antiga
        return (ids * (n // len(ids) + 1))[:n]

    nomes_contract = [_texto_limpo(v) for v in df_contract["Account.Name"]]
    chaves = [x.casefold() for x in nomes_contract]
    ordem = list(dict.fromkeys(chaves))

    if len(ordem) != len(ids):
        raise ValueError(
            f"A aba Contract tem {len(ordem)} conta(s) distinta(s) em Account.Name, "
            f"mas foram informados {len(ids)} Account ID(s)."
        )

    if "Name" in df_account.columns:
        nomes_account = [_texto_limpo(v) for v in df_account["Name"]]
        if [x.casefold() for x in nomes_account] != ordem:
            primeiros_contract = list(dict.fromkeys(nomes_contract))
            linhas = []
            for i, (a, c) in enumerate(zip(nomes_account, primeiros_contract)):
                if a.casefold() != c.casefold():
                    linhas.append(f"Posição {i + 1}: Account = '{a}' | Contract = '{c}'")
                if len(linhas) >= 8:
                    break
            raise ValueError(
                "As abas Account e Contract não estão na mesma ordem de conta.\n\n"
                + "\n".join(linhas)
            )

    mapa = dict(zip(ordem, ids))
    return [mapa[k] for k in chaves]

# ==================== FUNÇÕES PRINCIPAIS ====================

def anexar_arquivo():
    global caminho_arquivo
    limpar_csvs()
    caminho = filedialog.askopenfilename(
        title="Selecione o arquivo Excel",
        filetypes=[("Arquivos Excel", "*.xlsx *.xls")]
    )
    if caminho:
        caminho_arquivo = caminho
        label_status.config(text="✅ OK", fg="green")
        atualizar_botao_soql()

def abrir_csv(nome):
    caminho = os.path.join(pasta_saida, nome)
    with open(caminho, "r", encoding="utf-8-sig") as f:
        root.clipboard_clear()
        root.clipboard_append(f.read())
        root.update()
    messagebox.showinfo("Copiado", f"{nome} copiado para a área de transferência.")

# ==================== PROCESSAMENTO ====================

def processar_planilha():
    global pasta_saida, processado

    prod = exigir_produto()
    if not prod:
        return
    cfg = PRODUTOS[prod]

    ids = [i.strip() for i in text_contas.get("1.0", tk.END).splitlines() if i.strip()]
    if not ids:
        messagebox.showerror("Erro", "Informe ao menos um Account ID.")
        return

    if not caminho_arquivo:
        messagebox.showerror("Erro", "Anexe o arquivo Excel.")
        return

    avisos = []

    try:
        xls = pd.ExcelFile(caminho_arquivo)

        abas = xls.sheet_names

        for aba in ["Account", "Contract", "Ativo"]:
            if not any(aba.lower() in nome.lower() for nome in abas):
                messagebox.showerror(
                    "Erro",
                    f"Aba '{aba}' não foi encontrada no arquivo Excel."
                )
                return

        mapa_renomeacao = {
            "ContractNumber": "_ContractNumber",
            "Account.Name": "_Account.Name",
            "IDExternoAX__c": "_IDExternoAX__c",
            "EndDate": "_EndDate",
            "RecordType.DeveloperName": "_RecordType.DeveloperName",
            # INSERIDO ABAIXO POR CAUSA DESTES CAMPOS TRAVAREM A ATUALIZAÇÃO, PORÉM VIA UPDATE POSTERIOR SE RESOLVE.
            "IRIS_Codigo_Status_do_Tanque__c": "_IRIS_Codigo_Status_do_Tanque__c",
            "IRIS_Codigo_Situacao_do_Agendamento__c": "_IRIS_Codigo_Situacao_do_Agendamento__c"
        }

        # ================= ACCOUNT =================
        df_account = pd.read_excel(
            xls, sheet_name=[s for s in xls.sheet_names if "account" in s.lower()][0]
        )

        if len(df_account) != len(ids):
            messagebox.showerror(
                "Erro",
                "Quantidade de Account IDs diferente da quantidade de registros da aba Account."
            )
            return

        df_account["Id"] = ids
        df_account["Id"] = df_account["Id"].astype(str)

        df_account.rename(
            columns=lambda c: "Email__c" if isinstance(c, str) and c.strip().lower() == "email" else c,
            inplace=True
        )

        if "CPF__pc" in df_account.columns:
            if prod == "LIVRE":
                df_account["CPF__pc"] = (
                    df_account["CPF__pc"]
                    .fillna("")
                    .astype(str)
                    .str.replace(r"\D", "", regex=True)
                    .str.zfill(11)
                )
            else:
                df_account["CPF__pc"] = df_account["CPF__pc"].astype(str).str.strip()
                df_account["CPF__pc"] = df_account["CPF__pc"].apply(
                    lambda x: ("0" + x) if len(x) == 13 else x
                )

        df_account["RecordTypeId"] = cfg["rt_account"]

        if "AreaNegocio__c" in df_account.columns:
            df_account["AreaNegocio__c"] = "Leves"

        df_account.rename(columns=mapa_renomeacao, inplace=True)

        # ================= CONTRACT =================
        df_contract = pd.read_excel(
            xls, sheet_name=[s for s in xls.sheet_names if "contract" in s.lower()][0]
        )

        df_contract.drop(columns=["Id"], inplace=True, errors="ignore")

        if prod == "LIVRE":
            # 1 Account -> 1 Contract (mesma ordem dos IDs)
            if len(df_contract) != len(ids):
                messagebox.showerror(
                    "Erro",
                    "Quantidade de Account IDs diferente da quantidade de registros da aba Contract."
                )
                return
            df_contract["AccountId"] = ids
        else:
            # 1 Account -> N Contracts (aba Contract na mesma ordem da aba Account)
            try:
                df_contract["AccountId"] = mapear_account_ids_pj(df_account, df_contract, ids)
            except ValueError as e:
                messagebox.showerror("Erro", str(e))
                return

        df_contract = df_contract[["AccountId"] + [c for c in df_contract.columns if c != "AccountId"]]
        df_contract["AccountId"] = df_contract["AccountId"].astype(str)

        df_contract["Status"] = "Draft"
        df_contract["IRIS_Categoria_Contrato__c"] = "2"

        # Novas regras de campos (antes da formatação de datas)
        tratar_contract_term(df_contract, avisos)
        aplicar_regras_de_campos(df_contract, "Contract", avisos)

        for col in df_contract.columns:
            if "date" in col.lower() or "data" in col.lower():
                df_contract[col] = pd.to_datetime(
                    df_contract[col], errors="coerce"
                ).dt.strftime("%Y-%m-%d")

        for campo in [
            "IRIS_CapturaReservaPrimeiraParcela__c",
            "IRIS_ReservaPrimeiraParcela__c"
        ]:
            if campo in df_contract.columns:
                df_contract[campo] = cfg["reserva_parcela"]

        df_contract["RecordTypeId"] = cfg["rt_contract"]

        df_contract.rename(columns=mapa_renomeacao, inplace=True)

        # ================= ASSET =================
        df_asset = pd.read_excel(
            xls, sheet_name=[s for s in xls.sheet_names if "ativo" in s.lower()][0]
        )

        df_asset.drop(columns=["Id"], inplace=True, errors="ignore")

        if prod == "LIVRE":
            if len(df_asset) != len(ids):
                messagebox.showerror(
                    "Erro",
                    "Quantidade de Account IDs diferente da quantidade de registros da aba Assets."
                )
                return
            df_asset["AccountId"] = ids

        else:
            if len(ids) == 1:
                df_asset["AccountId"] = ids[0]
            else:
                df_asset["AccountId"] = (
                    ids * (len(df_asset) // len(ids) + 1)
                )[:len(df_asset)]

            # RELAÇÃO CONTRATO X ASSET
            campo_asset = "IRIS_Contrato__r.IRIS_CodigoContratoMasterLocavia__c"
            campo_contract = "IRIS_CodigoContratoMasterLocavia__c"

            if campo_asset in df_asset.columns and campo_contract in df_contract.columns:

                df_asset[campo_asset] = df_asset[campo_asset].astype(str).str.strip()
                df_contract[campo_contract] = df_contract[campo_contract].astype(str).str.strip()

                contratos_asset = set(df_asset[campo_asset].dropna())
                contratos_contract = set(df_contract[campo_contract].dropna())

                faltantes = contratos_asset - contratos_contract

                if faltantes:
                    messagebox.showerror(
                        "Erro",
                        "Assets possuem contratos inexistentes:\n\n" + "\n".join(sorted(faltantes))
                    )
                    return

                # O AccountId do Asset segue o AccountId do Contract ao qual ele pertence
                mapa_contrato_conta = dict(
                    zip(df_contract[campo_contract], df_contract["AccountId"])
                )
                df_asset["AccountId"] = df_asset[campo_asset].map(mapa_contrato_conta)

        df_asset["AccountId"] = df_asset["AccountId"].astype(str)
        df_asset = df_asset[["AccountId"] + [c for c in df_asset.columns if c != "AccountId"]]

        # Novas regras de campos (antes da formatação de datas)
        aplicar_regras_de_campos(df_asset, "Asset", avisos)

        for col in df_asset.columns:
            if "date" in col.lower() or "data" in col.lower():
                df_asset[col] = pd.to_datetime(
                    df_asset[col], errors="coerce"
                ).dt.strftime("%Y-%m-%d")

        if "RecordType.Name" in df_asset.columns:
            df_asset.rename(columns={"RecordType.Name": "RecordTypeId"}, inplace=True)

        df_asset.rename(columns=mapa_renomeacao, inplace=True)

        if prod == "FLEET" or "RecordTypeId" in df_asset.columns:
            df_asset["RecordTypeId"] = cfg["rt_asset"]

        # ================= SALVAR =================
        pasta_saida = os.path.dirname(caminho_arquivo)

        df_account.to_csv(os.path.join(pasta_saida, "Account.csv"), index=False, encoding="utf-8-sig")
        df_contract.to_csv(os.path.join(pasta_saida, "Contract.csv"), index=False, encoding="utf-8-sig")
        df_asset.to_csv(os.path.join(pasta_saida, "Asset.csv"), index=False, encoding="utf-8-sig")

        processado = True

        msg = "Processamento concluído e CSVs gerados com sucesso!"
        if avisos:
            msg += "\n\nAjustes aplicados:\n- " + "\n- ".join(avisos)
        messagebox.showinfo("Sucesso", msg)

        for w in frame_botoes_csv.winfo_children():
            w.destroy()

        for i in range(3):
            frame_botoes_csv.grid_columnconfigure(i, weight=1)

        nomes_botoes = cfg["botoes_csv"]
        coluna_inicial = 3 - len(nomes_botoes)
        for i, nome in enumerate(nomes_botoes):
            tk.Button(
                frame_botoes_csv,
                text=nome,
                command=lambda n=nome: abrir_csv(n + ".csv"),
                bg="#2196F3",
                fg="white"
            ).grid(row=0, column=coluna_inicial + i, padx=10)

    except Exception as e:
        messagebox.showerror("Erro ao processar", str(e))

# ==================== INTERFACE ====================

root = tk.Tk()
centralizar_janela(root, 700, 520)
root.protocol("WM_DELETE_WINDOW", ao_fechar)

# ----- Seleção do produto -----
frame_produto = tk.Frame(root)
frame_produto.pack(pady=8)

tk.Label(frame_produto, text="Produto:", font=("Verdana", 10, "bold")).pack(side=tk.LEFT, padx=5)

combo_produto = ttk.Combobox(
    frame_produto,
    values=list(PRODUTOS.keys()),
    state="readonly",
    width=12
)
combo_produto.pack(side=tk.LEFT, padx=5)
combo_produto.bind("<<ComboboxSelected>>", ao_trocar_produto)

label_ids = tk.Label(root, text="Insira os Account IDs (1 por linha):")
label_ids.pack(pady=5)

frame_ids = tk.Frame(root)
frame_ids.pack(pady=5)

# ----- Frame do Text + Scroll -----
frame_text = tk.Frame(frame_ids)
frame_text.pack(side=tk.LEFT)

scroll_ids = tk.Scrollbar(frame_text)
scroll_ids.pack(side=tk.RIGHT, fill=tk.Y)

text_contas = tk.Text(
    frame_text,
    height=6,
    width=60,
    yscrollcommand=scroll_ids.set
)
text_contas.pack(side=tk.LEFT)

scroll_ids.config(command=text_contas.yview)

# ----- Contador -----
label_contador = tk.Label(
    frame_ids,
    text="0",
    font=("Verdana", 10, "bold"),
    width=4
)
label_contador.pack(side=tk.LEFT, padx=6)

text_contas.bind(
    "<Control-v>",
    lambda e: (atualizar_contador_ids(e), text_contas.after(1, lambda: text_contas.see(tk.END)))
)
text_contas.bind(
    "<Control-V>",
    lambda e: (atualizar_contador_ids(e), text_contas.after(1, lambda: text_contas.see(tk.END)))
)

text_contas.bind("<Return>", atualizar_contador_ids)

def on_keypress(event):
    resetar_pos_digitacao()
    atualizar_botao_soql()

text_contas.bind("<KeyPress>", on_keypress)

frame_anexo = tk.Frame(root)
frame_anexo.pack(pady=5)

btn_anexar = tk.Button(
    frame_anexo,
    text="Anexar Arquivo",
    command=anexar_arquivo
)
btn_anexar.pack(side=tk.LEFT, padx=5)

btn_soql_cpf = tk.Button(
    frame_anexo,
    text="Gerar SOQL por CPF",
    command=gerar_soql_por_cpf,
    bg="#673AB7",
    fg="white"
)

label_status = tk.Label(root, text="Nenhum arquivo anexado", fg="red")
label_status.pack(pady=5)

tk.Label(root, text="Observações:").pack(pady=5)

text_obs = tk.Text(root, height=7, width=70)
text_obs.pack(pady=5)
text_obs.config(state=tk.DISABLED)

tk.Button(
    root,
    text="Processar e Salvar CSV",
    bg="#4CAF50",
    fg="white",
    command=processar_planilha
).pack(pady=15)

frame_botoes_csv = tk.Frame(root)
frame_botoes_csv.pack(pady=10, fill="x")

titulo_janela()

root.mainloop()

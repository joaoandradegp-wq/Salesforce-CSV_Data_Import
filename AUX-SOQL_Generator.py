import tkinter as tk
from tkinter import ttk, messagebox
import re
import math

# ==================== VARIÁVEIS GLOBAIS ====================

versao = "1.1"

# Configuração por objeto: campos do SELECT e campo usado no "IN"
OBJETOS = {
    "IRIS_Cupom__c": {
        "campos": "id, IRIS_Cupom__c, name",
        "filtro": "name",
    },
    "Opportunity": {
        "campos": "id, Name, IRIS_CodigoContratoLocavia__c, StageName",
        "filtro": "id",
    },
    "Contract": {
        "campos": "id, IRIS_CodigoContratoLocavia__c, Status",
        "filtro": "IRIS_CodigoContratoLocavia__c",
    },
    "Asset": {
        "campos": "id, IRIS_NomedoAtivo__c, Placa__c",
        "filtro": "Placa__c",
    },
}

# ===========================================================

soql_partes = []

def gerar_partes():
    global soql_partes
    soql_partes.clear()

    objeto = combo_objeto.get()
    if objeto not in OBJETOS:
        messagebox.showwarning("Aviso", "Selecione o objeto.")
        return

    cfg = OBJETOS[objeto]

    texto = txt_ids.get("1.0", tk.END).strip()

    if not texto:
        messagebox.showwarning("Aviso", "Cole pelo menos um valor.")
        return

    try:
        limite = int(entry_limite.get())
        if limite <= 0:
            raise ValueError
    except:
        messagebox.showwarning("Aviso", "Informe um número válido de valores por parte.")
        return

    ids = re.split(r'[\s,;]+', texto)
    ids = [i.strip() for i in ids if i.strip()]

    if not ids:
        messagebox.showwarning("Aviso", "Nenhum valor válido encontrado.")
        return

    total_partes = math.ceil(len(ids) / limite)

    for i in range(total_partes):
        inicio = i * limite
        fim = inicio + limite
        parte_ids = ids[inicio:fim]

        ids_formatados = ",".join(f"'{x}'" for x in parte_ids)

        soql = (
            f"SELECT {cfg['campos']} "
            f"FROM {objeto} "
            f"WHERE {cfg['filtro']} IN ({ids_formatados}) "
            "ORDER BY CreatedDate DESC"
        )

        soql_partes.append(soql)

    criar_botoes()
    messagebox.showinfo("Sucesso", f"{total_partes} parte(s) criada(s)!")

def criar_botoes():
    for widget in frame_botoes.winfo_children():
        widget.destroy()

    for idx, _ in enumerate(soql_partes):
        btn = tk.Button(
            frame_botoes,
            text=f"PARTE {idx+1}",
            bg="#6A0DAD",
            fg="white",
            activebackground="#5A0099",
            command=lambda i=idx: copiar_parte(i),
            width=15,
            height=2
        )
        btn.grid(row=idx//4, column=idx%4, padx=5, pady=5)

def copiar_parte(indice):
    root.clipboard_clear()
    root.clipboard_append(soql_partes[indice])
    root.update()
    messagebox.showinfo("Copiado", f"SOQL da PARTE {indice+1} copiado!")

def ao_trocar_objeto(event=None):
    # Atualiza o texto do label e limpa botões antigos (evita copiar SOQL do objeto anterior)
    objeto = combo_objeto.get()
    lbl_ids.config(text=f"Cole os valores de {OBJETOS[objeto]['filtro']}:")
    soql_partes.clear()
    for widget in frame_botoes.winfo_children():
        widget.destroy()

# =============================
# Interface
# =============================

root = tk.Tk()
root.title("SOQL Generator "+versao+" - Aggrandize - João Márcio Bicalho Andrade")
root.geometry("750x580")

# Seleção do objeto
frame_objeto = tk.Frame(root)
frame_objeto.pack(pady=10)

tk.Label(frame_objeto, text="Objeto:").pack(side="left", padx=5)

combo_objeto = ttk.Combobox(
    frame_objeto,
    values=list(OBJETOS.keys()),
    state="readonly",
    width=25
)
combo_objeto.current(0)
combo_objeto.pack(side="left")
combo_objeto.bind("<<ComboboxSelected>>", ao_trocar_objeto)

lbl_ids = tk.Label(root, text="")
lbl_ids.pack(pady=5)

# Frame para Text + Scrollbar
frame_texto = tk.Frame(root)
frame_texto.pack(fill="x", padx=15, pady=5)

scrollbar = tk.Scrollbar(frame_texto)
scrollbar.pack(side="right", fill="y")

txt_ids = tk.Text(
    frame_texto,
    height=15,
    yscrollcommand=scrollbar.set
)
txt_ids.pack(side="left", fill="both", expand=True)

scrollbar.config(command=txt_ids.yview)

# Configuração limite
frame_config = tk.Frame(root)
frame_config.pack(pady=10)

tk.Label(frame_config, text="Quantidade máxima por parte:").pack(side="left", padx=5)

entry_limite = tk.Entry(frame_config, width=10)
entry_limite.insert(0, "500")
entry_limite.pack(side="left")

btn_gerar = tk.Button(
    root,
    text="GERAR PARTES",
    command=gerar_partes,
    bg="#6A0DAD",
    fg="white",
    activebackground="#5A0099",
    height=2
)
btn_gerar.pack(pady=10)

frame_botoes = tk.Frame(root)
frame_botoes.pack(pady=10)

ao_trocar_objeto()

root.mainloop()

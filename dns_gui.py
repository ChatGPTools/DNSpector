import dns.resolver
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

def get_dns_records(domain):
    records = {}
    try:
        for record_type in ['A', 'AAAA', 'MX', 'TXT', 'NS']:
            answers = dns.resolver.resolve(domain, record_type)
            records[record_type] = [answer.to_text() for answer in answers]
    except Exception as e:
        messagebox.showerror("Errore", f"Impossibile ottenere i record DNS: {e}")
    return records

def analyze_domain():
    domain = domain_entry.get()
    if domain:
        records = get_dns_records(domain)
        results_text.delete(1.0, tk.END)
        for record_type, answers in records.items():
            results_text.insert(tk.END, f"{record_type} Records:\n")
            for answer in answers:
                results_text.insert(tk.END, f" - {answer}\n")
            results_text.insert(tk.END, "\n")
    else:
        messagebox.showinfo("Informazione", "Inserisci un dominio valido.")

# Creazione della finestra principale
root = tk.Tk()
root.title("Detective DNS")

# Layout
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

domain_label = tk.Label(frame, text="Inserisci il dominio:")
domain_label.pack()

domain_entry = tk.Entry(frame, width=50)
domain_entry.pack(pady=5)

analyze_button = tk.Button(frame, text="Analizza", command=analyze_domain)
analyze_button.pack(pady=10)

results_text = scrolledtext.ScrolledText(frame, width=70, height=20)
results_text.pack()

root.mainloop()

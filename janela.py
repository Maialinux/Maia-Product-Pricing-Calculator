from tkinter import *
import customtkinter as ctk
import math

class Janela():
    def __init__(self) -> None:
        self.janelaMain = ctk.CTk()
        self.aparencia = ctk.AppearanceModeTracker()
        self.aparencia.set_appearance_mode("System")  # Modes: system (default), light, dark
        self.tema = ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
        self.janelaMain.geometry("1280x900")
        self.title = self.janelaMain.title("Calculadora de Precificação de Produtos")
        self.classificacao=ctk.StringVar(value="off")
        
        pass
    
    
    def Criar_janela(self):
        self.Titulo_da_Pagina()
        self.BotaoQueTrocaClassificacao()
        self.Painel_Left()
        self.Botao()
        self.Painel_Right()
        self.BotaoLimpar()
        self.janelaMain.mainloop()

    
    def Titulo_da_Pagina(self):
        titulo_da_Pagina = ctk.CTkLabel(self.janelaMain,text="Calculadora de Precificação de Produtos",font=ctk.CTkFont(family="Verdana",size=24,weight="bold"))        
        titulo_da_Pagina.place(relx=0.5,rely=0.04, anchor=ctk.CENTER)


    def BotaoQueTrocaClassificacao(self):
        self.botao_trocar = ctk.CTkSwitch(self.janelaMain, text="Produtos Nacionais", command=self.TrocarClassificacao,variable=self.classificacao, onvalue="on", offvalue="off")
        self.botao_trocar.place(relx=0.85, rely=0.08)

    def TrocarClassificacao(self):
        self.classificacao = not self.classificacao
        if self.classificacao == False:
            self.botao_trocar.configure(text="Produtos Importados")
        else:
            self.botao_trocar.configure(text="Produtos Nacionais")

    def Painel_Left(self):
        self.painel_left = ctk.CTkFrame(self.janelaMain,width=580, height=740)
        self.painel_left.place(relx=0.0, rely=0.55, anchor=W)

        label_titulo1 = ctk.CTkLabel(self.painel_left,text="Descrição dos Custos",font=ctk.CTkFont(family="Verdana",size=24,weight="bold"))
        label_titulo1.place(relx=0.5,rely=0.04, anchor=ctk.CENTER)
        
        label_preco_fornecedor = ctk.CTkLabel(self.painel_left,text="Preço dos Fornecedores        R$",font=ctk.CTkFont(family="Verdana",size=20,weight="normal"))
        label_preco_fornecedor.place(relx=0.04,rely=0.1, anchor=W)
        self.txt_preco_fornecedor = ctk.CTkEntry(self.painel_left,width=180, height=32, font=ctk.CTkFont(family="Verdana",size=20,weight="normal"),text_color="#D4D4D4")
        self.txt_preco_fornecedor.place(relx=0.6,rely=0.1, anchor=W)
        self.txt_preco_fornecedor.insert(END, "0.00")
        self.txt_preco_fornecedor.bind("<Button-1>", self.Click_txt_preco_fornecedor)
         
        label_frete_fornecedor = ctk.CTkLabel(self.painel_left,text="Frete dos Fornecedores        R$",font=ctk.CTkFont(family="Verdana",size=20,weight="normal"))
        label_frete_fornecedor.place(relx=0.04,rely=0.16, anchor=W)
        self.txt_frete_fornecedor = ctk.CTkEntry(self.painel_left,width=180, height=32, font=ctk.CTkFont(family="Verdana",size=20,weight="normal"),text_color="#D4D4D4")
        self.txt_frete_fornecedor.place(relx=0.6,rely=0.16, anchor=W)
        self.txt_frete_fornecedor.insert(END, "0.00")
        self.txt_frete_fornecedor.bind("<Button-1>", self.Click_txt_frete_fornecedor)
        self.txt_frete_fornecedor.bind("<Return>", self.CustoComFornecedor)
        

        label_titulo2 = ctk.CTkLabel(self.painel_left,text="Custo Total com o Fornecedor",font=ctk.CTkFont(family="Verdana",size=24,weight="bold"))
        label_titulo2.place(relx=0.5,rely=0.3, anchor=ctk.CENTER)
        self.label_preco_produto_mais_frete = ctk.CTkLabel(self.painel_left,text="Preço do Produto + Frete",font=ctk.CTkFont(family="Verdana",size=20,weight="normal"))
        self.label_preco_produto_mais_frete.place(relx=0.04,rely=0.36, anchor=W)

        self.label_resultado_produto_mais_frete = ctk.CTkLabel(self.painel_left,text="R$ 0,00", font=ctk.CTkFont(family="Verdana",size=20,weight="bold"))
        self.label_resultado_produto_mais_frete.place(relx=0.6,rely=0.36, anchor=W)
        
        label_titulo3 = ctk.CTkLabel(self.painel_left,text="Preço de Venda na Loja",font=ctk.CTkFont(family="Verdana",size=24,weight="bold"))
        label_titulo3.place(relx=0.5,rely=0.5, anchor=ctk.CENTER)
        label_preco_na_loja = ctk.CTkLabel(self.painel_left,text="Valor de Venda na Loja        R$",font=ctk.CTkFont(family="Verdana",size=20,weight="normal"))
        label_preco_na_loja.place(relx=0.04,rely=0.56, anchor=W)
        self.txt_preco_na_loja = ctk.CTkEntry(self.painel_left,width=180, height=32, font=ctk.CTkFont(family="Verdana",size=20,weight="normal"),text_color="#D4D4D4")
        self.txt_preco_na_loja.place(relx=0.6,rely=0.56, anchor=W)
        self.txt_preco_na_loja.insert(END, "0.00")
        self.txt_preco_na_loja.bind("<Button-1>", self.Click_txt_preco_de_venda_na_loja)
        self.txt_preco_na_loja.bind("<Return>", self.Custos_gerais_de_taxas_gateway_de_pagamentos)
        
        label_titulo4 = ctk.CTkLabel(self.painel_left,text="Despesas Extras",font=ctk.CTkFont(family="Verdana",size=24,weight="bold"))
        label_titulo4.place(relx=0.5,rely=0.68, anchor=ctk.CENTER)
        # Taxa Gateway - normalmente 4.99%
        label_gateway_de_pagamentos = ctk.CTkLabel(self.painel_left,text="Gateway de Pagamentos         4.99%",font=ctk.CTkFont(family="Verdana",size=20,weight="normal"))
        label_gateway_de_pagamentos.place(relx=0.04,rely=0.74, anchor=W)
        self.txt_gateway_de_pagamentos = ctk.CTkEntry(self.painel_left,width=100, height=32, font=ctk.CTkFont(family="Verdana",size=20,weight="normal"),text_color="#D4D4D4")
        self.txt_gateway_de_pagamentos.place(relx=0.74,rely=0.74, anchor=W)
        self.txt_gateway_de_pagamentos.insert(END, "0.00")
        # Taxa irpf sobre lucro 15%
        label_irpf = ctk.CTkLabel(self.painel_left,text="Imposto sobre Lucro Bruto         15%",font=ctk.CTkFont(family="Verdana",size=20,weight="normal"))
        label_irpf.place(relx=0.04,rely=0.80, anchor=W)
        self.txt_irpf = ctk.CTkEntry(self.painel_left,width=100, height=32, font=ctk.CTkFont(family="Verdana",size=20,weight="normal"),text_color="#D4D4D4")
        self.txt_irpf.place(relx=0.74,rely=0.80, anchor=W)
        self.txt_irpf.insert(END, "0.00")
        # Taxa sobre o produto importado 20%
        label_taxa_produto_importado = ctk.CTkLabel(self.painel_left,text="Taxa do Produto Importado        20%",font=ctk.CTkFont(family="Verdana",size=20,weight="normal"))
        label_taxa_produto_importado.place(relx=0.04,rely=0.86, anchor=W)
        self.txt_taxa_produto_importado = ctk.CTkEntry(self.painel_left,width=100, height=32, font=ctk.CTkFont(family="Verdana",size=20,weight="normal"),text_color="#D4D4D4")
        self.txt_taxa_produto_importado.place(relx=0.74,rely=0.86, anchor=W)
        self.txt_taxa_produto_importado.insert(END, "0.00")
        # Taxa sobre o icms do produto
        label_taxa_icms = ctk.CTkLabel(self.painel_left,text="Taxa do ICMS                           17%",font=ctk.CTkFont(family="Verdana",size=20,weight="normal"))
        label_taxa_icms.place(relx=0.04,rely=0.92, anchor=W)
        self.txt_taxa_icms = ctk.CTkEntry(self.painel_left,width=100, height=32, font=ctk.CTkFont(family="Verdana",size=20,weight="normal"),text_color="#D4D4D4")
        self.txt_taxa_icms.place(relx=0.74,rely=0.92, anchor=W)
        self.txt_taxa_icms.insert(END, "0.00")
        
    def Botao(self):
        botao = ctk.CTkButton(self.janelaMain,text=">>>",font=ctk.CTkFont(family="Verdana",size=30),width=100,height=50,command=self.ResultadoFinal)
        botao.place(relx=0.5,rely=0.5, anchor=ctk.CENTER)
    
    def BotaoLimpar(self):
        botaoLimpar = ctk.CTkButton(self.janelaMain,text="Limpar",font=ctk.CTkFont(family="Verdana",size=24),width=100,height=50,command=self.Func_Limpar)
        botaoLimpar.place(relx=0.5,rely=0.6, anchor=ctk.CENTER)

    def Painel_Right(self):
        self.painel_right = ctk.CTkFrame(self.janelaMain,width=580, height=740)
        self.painel_right.place(relx=1.0, rely=0.55, anchor=E)

        label_titulo1 = ctk.CTkLabel(self.painel_right,text="Resultados",font=ctk.CTkFont(family="Verdana",size=24,weight="bold"))
        label_titulo1.place(relx=0.5,rely=0.04, anchor=ctk.CENTER)
        
        label_margem_liquida = ctk.CTkLabel(self.painel_right,text="Margem Líquida                                 R$",font=ctk.CTkFont(family="Verdana",size=20,weight="normal"))
        label_margem_liquida.place(relx=0.04,rely=0.1, anchor=W)
        self.label_resultado_margem_liquida = ctk.CTkLabel(self.painel_right,text="0.00",font=ctk.CTkFont(family="Verdana",size=20,weight="bold"), text_color="#00C500")
        self.label_resultado_margem_liquida.place(relx=0.86,rely=0.1, anchor=W)

        label_lucro_liquido = ctk.CTkLabel(self.painel_right,text="Lucro Líquido                                     R$",font=ctk.CTkFont(family="Verdana",size=20,weight="normal"))
        label_lucro_liquido.place(relx=0.04,rely=0.16, anchor=W)
        self.label_resultado_lucro_liquido = ctk.CTkLabel(self.painel_right,text="0.00",font=ctk.CTkFont(family="Verdana",size=20,weight="bold"), text_color="#00C500")
        self.label_resultado_lucro_liquido.place(relx=0.86,rely=0.16, anchor=W)
      
        # EXEMPLO DE NÚMEROS DE VENDAS
        label_titulo2 = ctk.CTkLabel(self.painel_right,text="Exemplo de Nº de Vendas",font=ctk.CTkFont(family="Verdana",size=24,weight="bold"))
        label_titulo2.place(relx=0.5,rely=0.5, anchor=ctk.CENTER)
        # ESTIMATIVA DE 7 VENDAS 
        label_vendas1 = ctk.CTkLabel(self.painel_right,text="7 Vendas                                           R$",font=ctk.CTkFont(family="Verdana",size=20,weight="normal"))
        label_vendas1.place(relx=0.04,rely=0.56, anchor=W)
        self.label_resultado_vendas1 = ctk.CTkLabel(self.painel_right,text="0.00",font=ctk.CTkFont(family="Verdana",size=20,weight="bold"), text_color="#00C500")
        self.label_resultado_vendas1.place(relx=0.86,rely=0.56, anchor=W)
        # ESTIMATIVA DE 15 VENDAS 
        label_vendas2 = ctk.CTkLabel(self.painel_right,text="15 Vendas                                         R$",font=ctk.CTkFont(family="Verdana",size=20,weight="normal"))
        label_vendas2.place(relx=0.04,rely=0.62, anchor=W)
        self.label_resultado_vendas2 = ctk.CTkLabel(self.painel_right,text="0.00",font=ctk.CTkFont(family="Verdana",size=20,weight="bold"), text_color="#00C500")
        self.label_resultado_vendas2.place(relx=0.86,rely=0.62, anchor=W)
        # ESTIMATIVA DE 30 VENDAS 
        label_vendas3 = ctk.CTkLabel(self.painel_right,text="30 Vendas                                         R$",font=ctk.CTkFont(family="Verdana",size=20,weight="normal"))
        label_vendas3.place(relx=0.04,rely=0.68, anchor=W)
        self.label_resultado_vendas3 = ctk.CTkLabel(self.painel_right,text="0.00",font=ctk.CTkFont(family="Verdana",size=20,weight="bold"), text_color="#00C500")
        self.label_resultado_vendas3.place(relx=0.86,rely=0.68, anchor=W)

    def Click_txt_preco_fornecedor(self,event):
        self.txt_preco_fornecedor.delete("0",END)
        self.txt_preco_fornecedor.configure(text_color="#555555")
        self.txt_preco_fornecedor.focus()

         
    def Click_txt_frete_fornecedor(self,event):
        #self.txt_frete_fornecedor.delete("0",END)
        self.txt_frete_fornecedor.configure(text_color="#555555")
        self.txt_frete_fornecedor.focus()
   

    def CustoComFornecedor(self,event):
        self.txt_preco_na_loja.focus()
        self.txt_preco_na_loja.delete("0",END)
        self.txt_preco_na_loja.configure(text_color="#555555")
        total = float(self.txt_preco_fornecedor.get()) + float(self.txt_frete_fornecedor.get())
        self.label_resultado_produto_mais_frete.configure(text=f"R$ {round(total.real,2)}")
        
    
    def Click_txt_preco_de_venda_na_loja(self, event):
        self.txt_preco_na_loja.delete("0",END)
        self.txt_preco_na_loja.configure(text_color="#555555")
        self.txt_preco_na_loja.focus()
        
    
    def Custos_gerais_de_taxas_gateway_de_pagamentos(self, event):
        # Cálculo da Taxa Gateway de Pagamento
        self.txt_gateway_de_pagamentos.delete("0",END)
        self.txt_gateway_de_pagamentos.configure(text_color="#555555")
        self.txt_gateway_de_pagamentos.focus()
        totalPrecoFornecedorFrete = float(self.txt_preco_fornecedor.get()) + float(self.txt_frete_fornecedor.get())
        totalLucroBruto = float(self.txt_preco_na_loja.get()) - totalPrecoFornecedorFrete
        porcento_gateway_pagamento = float(4.99 / 100)
        total_gateway_pagamento = float(totalLucroBruto) * porcento_gateway_pagamento
        self.txt_gateway_de_pagamentos.insert(END,round(total_gateway_pagamento,2))
        
        # Cálculo do Imposto de Renda Sobre Renda Bruta
        self.txt_irpf.delete("0",END)
        self.txt_irpf.configure(text_color="#555555")
        self.txt_irpf.focus()
        totalPrecoFornecedorFrete = float(self.txt_preco_fornecedor.get()) + float(self.txt_frete_fornecedor.get())
        totalLucroBruto = float(self.txt_preco_na_loja.get()) - totalPrecoFornecedorFrete
        porcento_irpf = float(15 / 100)
        total_irpf = float(totalLucroBruto) * porcento_irpf
       # print(total_irpf)
        self.txt_irpf.insert(END,round(total_irpf,2))
        
        # Cálculo do Imposto para Produtos Importados
        self.txt_taxa_produto_importado.delete("0",END)
        self.txt_taxa_produto_importado.configure(text_color="#555555")
        self.txt_taxa_produto_importado.focus()
        totalPrecoFornecedorFrete = float(self.txt_preco_fornecedor.get()) + float(self.txt_frete_fornecedor.get())
        totalLucroBruto = float(self.txt_preco_na_loja.get()) - totalPrecoFornecedorFrete
        porcento_taxa_produto_importado = 20/100
        total_taxa_produto_importado = float(totalLucroBruto) * porcento_taxa_produto_importado
        self.txt_taxa_produto_importado.insert(END,round(total_taxa_produto_importado,2))
        # Cálculo da Taxa ICMS
        self.txt_taxa_icms.delete("0",END)
        self.txt_taxa_icms.configure(text_color="#555555")
        self.txt_taxa_icms.focus()
        totalPrecoFornecedorFrete = float(self.txt_preco_fornecedor.get()) + float(self.txt_frete_fornecedor.get())
        totalLucroBruto = float(self.txt_preco_na_loja.get()) - totalPrecoFornecedorFrete
        porcento_taxa_icms = 17/100
        total_txt_taxa_icms = float(totalLucroBruto) * porcento_taxa_icms
        self.txt_taxa_icms.insert(END,round(total_txt_taxa_icms,2))
        
        pass

    def ResultadoFinal(self):
        if self.classificacao == True:
            totalPrecoFornecedorFrete = float(self.txt_preco_fornecedor.get()) + float(self.txt_frete_fornecedor.get())
            totalLucroBruto = float(self.txt_preco_na_loja.get()) - totalPrecoFornecedorFrete
            self.label_resultado_margem_liquida.configure(text=f"{round(totalLucroBruto.real,2)}")
            total_lucro_liquido = float(totalLucroBruto) - float(self.txt_gateway_de_pagamentos.get()) - float(self.txt_irpf.get())
            self.label_resultado_lucro_liquido.configure(text=f"{round(total_lucro_liquido,2)}")
        

        else:
            totalPrecoFornecedorFrete = float(self.txt_preco_fornecedor.get()) + float(self.txt_frete_fornecedor.get())
            totalLucroBruto = float(self.txt_preco_na_loja.get()) - totalPrecoFornecedorFrete
            self.label_resultado_margem_liquida.configure(text=f"{round(totalLucroBruto.real,2)}")
            porcento_gateway_pagamento = float(4.99 / 100)
            porcento_irpf = float(15 / 100)
            porcento_taxa_produto_importado = float(20 / 100)
            porcento_taxa_icms = float(17 / 100)
            total_gateway_pagamento = float(totalLucroBruto) * porcento_gateway_pagamento
            total_irpf = float(totalLucroBruto) * porcento_irpf
            total_taxa_produto_importado = float(totalLucroBruto) * porcento_taxa_produto_importado
            total_txt_taxa_icms = float(totalLucroBruto) * porcento_taxa_icms
            total_lucro_liquido = float(totalLucroBruto) - total_gateway_pagamento - total_irpf - total_taxa_produto_importado - total_txt_taxa_icms
            self.label_resultado_lucro_liquido.configure(text=f"{round(total_lucro_liquido,2)}")
          
        # Exemplo de 7 vendas  
        self.label_resultado_vendas1.configure(text=f"{round(total_lucro_liquido * 7,2)}")
        # Exemplo de 15 vendas  
        self.label_resultado_vendas2.configure(text=f"{round(total_lucro_liquido * 15,2)}")
        # Exemplo de 30 vendas  
        self.label_resultado_vendas3.configure(text=f"{round(total_lucro_liquido * 30,2)}")
    

    def Func_Limpar(self):
       self.txt_preco_fornecedor.delete("0",END)
       self.txt_preco_fornecedor.insert(END, "0.00")
       self.txt_preco_fornecedor.configure(text_color="#D4D4D4")
       self.txt_frete_fornecedor.delete("0",END)
       self.txt_frete_fornecedor.insert(END, "0.00")
       self.txt_frete_fornecedor.configure(text_color="#D4D4D4")
       self.label_resultado_produto_mais_frete.configure(text="R$ 0.00")
       self.txt_preco_na_loja.delete("0",END)
       self.txt_preco_na_loja.insert(END, "0.00")
       self.txt_preco_na_loja.configure(text_color="#D4D4D4")
       self.txt_gateway_de_pagamentos.delete("0",END)
       self.txt_gateway_de_pagamentos.insert(END, "0.00")
       self.txt_gateway_de_pagamentos.configure(text_color="#D4D4D4")
       self.txt_irpf.delete("0",END)
       self.txt_irpf.insert(END, "0.00")
       self.txt_irpf.configure(text_color="#D4D4D4")
       self.txt_taxa_produto_importado.delete("0",END)
       self.txt_taxa_produto_importado.insert(END, "0.00")
       self.txt_taxa_produto_importado.configure(text_color="#D4D4D4")
       self.txt_taxa_icms.delete("0",END)
       self.txt_taxa_icms.insert(END, "0.00")
       self.txt_taxa_icms.configure(text_color="#D4D4D4")
       self.label_resultado_margem_liquida.configure(text="0.00")
       self.label_resultado_lucro_liquido.configure(text="0.00")
       self.label_resultado_vendas1.configure(text="0.00")
       self.label_resultado_vendas2.configure(text="0.00")
       self.label_resultado_vendas3.configure(text="0.00")
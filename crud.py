import psycopg2

class AppBD:
    def __init__(self):
        print('Método construtor')
        
    def abrirConexao(self):
        try:
            self.connection = psycopg2.connect(user = "postgres",
                                               password = "86733",
                                               host = "127.0.0.1",
                                               port = "5432",
                                               database = "postgres")
        except(Exception, psycopg2.Error) as error:
            if(self.connection):
                print("Falha ao conectar ao Banco de Dados.", error)
                    
    def selecionarDados(self):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            
            print("Selecionando todos os produtos:")
            sql_select_query = """SELECT * FROM public."PRODUTO" """
            
            cursor.execute(sql_select_query)
            registros = cursor.fetchall()
            print(registros)
        except(Exception, psycopg2.Error) as error:
            print("Erro na operação de seleção.", error)
        finally:
            if(self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o Banco de Dados foi encerrada.")
        return registros
    
    def inserirDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            postgres_insert_query = """INSERT INTO public."PRODUTO" ("CODIGO", "NOME", "PRECO") VALUES (%s, %s, %s)"""
            record_to_insert = (codigo, nome, preco)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro inserido com sucesso na tabela PRODUTO")
        except(Exception, psycopg2.Error) as error:
            if(self.connection):
                print("Falha ao inserir registro na tabela PRODUTO.", error)
        finally:
            if(self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o Banco de Dados foi encerrada.")
    
    def atualizarDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            
            print("Resgistro antes da atualização:")
            sql_select_query = """SELECT * FROM public."PRODUTO" WHERE "CODIGO" = %s"""
            cursor.execute(sql_select_query, (codigo,))
            record = cursor.fetchone()
            print(record)
            sql_update_query = """UPDATE public."PRODUTO" SET "NOME" = %s, "PRECO" = %s WHERE "CODIGO" = %s"""
            cursor.execute(sql_update_query, (nome, preco, codigo))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro atualizado com sucesso!")
            print("Registro depois da autalização:")
            sql_select_query = """SELECT * FROM public."PRODUTO"  WHERE "CODIGO" = %s"""
            cursor.execute(sql_select_query, (codigo,))
            record = cursor.fetchone()
            print(record)
        except(Exception, psycopg2.Error) as error:
            print("Falha na atualização da tabela PRODUTO.", error)
        finally:
            if(self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o Banco de Dados foi encerrada.")
                
    def excluirDados(self, codigo):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            
            sql_delete_query = """DELETE FROM public."PRODUTO" WHERE "CODIGO" = %s"""
            cursor.execute(sql_delete_query, (codigo,))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro excluído com sucesso!")
        except(Exception, psycopg2.Error) as error:
            print("Erro na exclusão do registro da tabela PRODUTO.", error)
        finally:
            if(self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o Banco de Dados foi encerrada.")
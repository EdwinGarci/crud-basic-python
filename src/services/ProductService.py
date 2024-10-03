import traceback

# Database
from src.database.db_mysql import get_connection
# Models
from src.models.ProductModel import Product

class ProductService():
    @classmethod
    def get_products(cls):
        connection = None
        try:
            connection = get_connection()
            products = []
            with connection.cursor() as cursor:
                query = 'SELECT id, name, description, price, stock FROM products'
                cursor.execute(query)
                resultset = cursor.fetchall() 
                for row in resultset:
                    product = Product(
                        int(row[0]), 
                        row[1],
                        row[2],
                        float(row[3]),
                        int(row[4])
                    )
                    products.append(product.to_json())
            return products
        except Exception as ex:
            print(f"Error en ProductService.get_products: {str(ex)}")
            print(f"Traceback:\n{traceback.format_exc()}")
            raise Exception(f"Error al obtener productos: {str(ex)}") from ex
        finally:
            if connection:
                connection.close()

    @classmethod
    def get_product_by_id(cls, product_id):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                query = 'SELECT id, name, description, price, stock FROM products WHERE id = %s'
                cursor.execute(query, (product_id,))
                row = cursor.fetchone()

                if row:
                    product = Product(
                        int(row[0]),
                        row[1],
                        row[2],
                        float(row[3]),
                        int(row[4])
                    )
                    return product.to_json()
                else:
                    return None
        except Exception as ex:
            print(f"Error en ProductService.get_product_by_id: {str(ex)}")
            print(f"Traceback:\n{traceback.format_exc()}")
            raise Exception(f"Error al obtener el producto por ID: {str(ex)}") from ex
        finally:
            if connection:
                connection.close()

    @classmethod
    def create_product(cls, name, description, price, stock):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                query = '''
                INSERT INTO products (name, description, price, stock)
                VALUES (%s, %s, %s, %s)
                '''
                cursor.execute(query, (name, description, price, stock))
                connection.commit()
                return cursor.lastrowid
        except Exception as ex:
            print(f"Error en ProductService.create_product: {str(ex)}")
            print(f"Traceback:\n{traceback.format_exc()}")
            raise Exception(f"Error al crear el producto: {str(ex)}") from ex
        finally:
            if connection:
                connection.close()

    @classmethod
    def update_product(cls, product_id, name, description, price, stock):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                query = '''
                UPDATE products
                SET name = %s, description = %s, price = %s, stock = %s
                WHERE id = %s
                '''
                cursor.execute(query, (name, description, price, stock, product_id))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            print(f"Error en ProductService.update_product: {str(ex)}")
            print(f"Traceback:\n{traceback.format_exc()}")
            raise Exception(f"Error al actualizar el producto: {str(ex)}") from ex
        finally:
            if connection:
                connection.close()

    @classmethod
    def delete_product(cls, product_id):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                query = 'DELETE FROM products WHERE id = %s'
                cursor.execute(query, (product_id,))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            print(f"Error en ProductService.delete_product: {str(ex)}")
            print(f"Traceback:\n{traceback.format_exc()}")
            raise Exception(f"Error al eliminar el producto: {str(ex)}") from ex
        finally:
            if connection:
                connection.close()


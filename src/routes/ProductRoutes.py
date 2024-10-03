from flask import Blueprint, request, jsonify

import traceback

# Services
from src.services.ProductService import ProductService

main = Blueprint('product_blueprint', __name__)

@main.route('/')
def get_products():
    try:
        products = ProductService.get_products()
        if products:
            return jsonify({
                'products': products, 
                'message': "Success", 
                'success': True
            }), 200
        else:
            return jsonify({
                'message': "No se encontraron productos", 
                'success': True
            }), 200
    except Exception as ex:
        print(f"Error al obtener productos: {str(ex)}")
        return jsonify({
            'message': "Error al obtener productos",
            'success': False
            }), 500

@main.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    try:
        product = ProductService.get_product_by_id(product_id)
        if product:
            return jsonify({
                'product': product, 
                'message': "Success", 
                'success': True
            }), 200
        else:
            return jsonify({
                'message': "Producto no encontrado", 
                'success': False
            }), 404
    except Exception as ex:
        print(f"Error al obtener el producto: {str(ex)}")
        return jsonify({
            'message': "Error al obtener el producto",
            'success': False
            }), 500

@main.route('/', methods=['POST'])
def create_product():
    try:
        data = request.json
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')
        stock = data.get('stock')

        if not all([name, description, price, stock]):
            return jsonify({
                'message': "Faltan datos", 
                'success': False
            }), 400

        product_id = ProductService.create_product(name, description, price, stock)
        return jsonify({
            'message': "Producto creado con éxito", 
            'product_id': product_id, 
            'success': True
        }), 201
    except Exception as ex:
        print(f"Error al crear producto: {str(ex)}")
        return jsonify({
            'message': "Error al crear producto",
            'success': False
            }), 500

@main.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    try:
        data = request.json
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')
        stock = data.get('stock')

        if not all([name, description, price, stock]):
            return jsonify({
                'message': "Faltan datos", 
                'success': False
            }), 400

        rows_affected = ProductService.update_product(product_id, name, description, price, stock)
        if rows_affected == 0:
            return jsonify({
                'message': "Producto no encontrado", 
                'success': False
            }), 404
        return jsonify({
            'message': "Producto actualizado con éxito", 
            'success': True
        }), 200
    except Exception as ex:
        print(f"Error al actualizar producto: {str(ex)}")
        return jsonify({
            'message': "Error al actualizar producto",
            'success': False
            }), 500

@main.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        rows_affected = ProductService.delete_product(product_id)
        if rows_affected == 0:
            return jsonify({
                'message': "Producto no encontrado", 
                'success': False
            }), 404
        return jsonify({
            'message': "Producto eliminado con éxito", 
            'success': True
        }), 200
    except Exception as ex:
        print(f"Error al eliminar producto: {str(ex)}")
        return jsonify({
            'message': "Error al eliminar producto",
            'success': False
            }), 500


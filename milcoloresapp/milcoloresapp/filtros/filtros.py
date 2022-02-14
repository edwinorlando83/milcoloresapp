import frappe

def get_permission_query_conditions_cliente(user):
    if not user: 
        user = frappe.session.user 

    if 'EMPRESA' in frappe.get_roles(user):
            return ""
               
    if 'CLIENTE' in frappe.get_roles(user):
        return """(tabCliente.correo = '{0}')""".format(user)

def get_permission_query_conditions_pedidos(user):
    if not user: 
        user = frappe.session.user 
    
    if 'System Manager' in frappe.get_roles(user):
        return ""
    
    if 'EMPRESA' in frappe.get_roles(user):
            return ""
 
    cli = frappe.get_doc("Cliente", {"correo":user })

    if 'CLIENTE' in frappe.get_roles(user):
        return """(tabPedido.cliente= '{0}')""".format(cli.name)
 
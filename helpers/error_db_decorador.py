from db.conexion import session


def error_transaccion(fn):
    def error_rollback(*args):
        try:
            fn(*args)
        except:
            session.rollback()
        finally:
            session.close()
    return error_rollback


def cerrar_sesion(fn):
    def cerrar(*args):
        try:
            return fn(*args)
        except:
            pass
        finally:
            session.close()
    return cerrar

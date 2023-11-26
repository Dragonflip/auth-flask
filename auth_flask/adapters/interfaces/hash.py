class HashManager:
    def hash_password(self, password):
        error_string = (
            f'Metodo ainda nao implementado para o parametro {password}'
        )
        raise NotImplementedError(error_string)

    def check_password(self, password, hashed_password):
        error_string = f'Metodo ainda nao implementado para os parametros {password, hashed_password}'
        raise NotImplementedError(error_string)

import hashlib
import time

# ==========================================
# 1. Criptografia por Substituição (Cifra de César)
# ==========================================

def cifrar_cesar(mensagem: str, deslocamento: int) -> str:
    """Codifica uma mensagem deslocando os caracteres no alfabeto."""
    resultado = ""
    for char in mensagem:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Aplica o deslocamento circular dentro do alfabeto (26 letras)
            novo_char = chr((ord(char) - base + deslocamento) % 26 + base)
            resultado += novo_char
        else:
            resultado += char
    return resultado

def decifrar_cesar(mensagem_cifrada: str, deslocamento: int) -> str:
    """Decodifica uma mensagem revertendo o deslocamento."""
    return cifrar_cesar(mensagem_cifrada, -deslocamento)


# ==========================================
# 2. Funções Hash e Segurança de Senhas
# ==========================================

def gerar_hash_senha(senha: str, salt: str = "seguranca_2026") -> str:
    """
    Gera o hash SHA-256 de uma senha.
    Boa prática: Inclui 'salt' (dados aleatórios adicionais) para evitar 
    ataques por tabelamento (Rainbow Tables).
    """
    senha_com_salt = senha + salt
    return hashlib.sha256(senha_com_salt.encode('utf-8')).hexdigest()


# ==========================================
# 3. Simulação de Ataque de Força Bruta
# ==========================================

def simular_forca_bruta(hash_alvo: str, dicionario_senhas: list[str], salt: str = "seguranca_2026"):
    """
    Simula a quebra de uma senha testando combinações até encontrar o hash correspondente.
    Usa estruturas de repetição (for) e condicionais (if).
    """
    print("\n[!] Iniciando simulação de ataque por Força Bruta / Dicionário...")
    inicio = time.time()
    
    tentativas = 0
    for candidato in dicionario_senhas:
        tentativas += 1
        hash_candidato = gerar_hash_senha(candidato, salt)
        
        # Condicional de verificação
        if hash_candidato == hash_alvo:
            tempo_decorrido = time.time() - inicio
            print(f"[✓] SENHA ENCONTRADA: '{candidato}'")
            print(f"    Tentativas: {tentativas} | Tempo: {tempo_decorrido:.4f}s")
            return candidato
            
    print("[X] Senha não encontrada no dicionário de teste.")
    return None


# ==========================================
# 4. Boas Práticas de Segurança da Informação
# ==========================================

def avaliar_forca_senha(senha: str) -> bool:
    """
    Aplica regras básicas de complexidade para proteger dados:
    - Mínimo de 8 caracteres
    - Pelo menos uma letra maiúscula e uma minúscula
    - Pelo menos um número
    """
    tem_tamanho = len(senha) >= 8
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_minuscula = any(c.islower() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)

    if tem_tamanho and tem_maiuscula and tem_minuscula and tem_numero:
        return True
    return False


# ==========================================
# Execução da Demonstração
# ==========================================

if __name__ == "__main__":
    print("=== 1. TESTE DE CRIPTOGRAFIA POR SUBSTITUIÇÃO ===")
    mensagem_original = "Mensagem Secreta de Segurança"
    chave_deslocamento = 5
    
    cifrada = cifrar_cesar(mensagem_original, chave_deslocamento)
    decifrada = decifrar_cesar(cifrada, chave_deslocamento)
    
    print(f"Original : {mensagem_original}")
    print(f"Cifrada  : {cifrada}")
    print(f"Decifrada: {decifrada}\n")

    print("=== 2. AVALIAÇÃO DE SENHA E HASH ===")
    senha_usuario = "Senha123"
    
    if avaliar_forca_senha(senha_usuario):
        print(f"A senha '{senha_usuario}' atende às boas práticas de complexidade.")
    else:
        print(f"A senha '{senha_usuario}' é FRACA! Use letras maiúsculas, minúsculas, números e mínimo 8 dígitos.")
        
    hash_armazenado = gerar_hash_senha(senha_usuario)
    print(f"Hash SHA-256 gerado (com salt): {hash_armazenado}\n")

    print("=== 3. SIMULAÇÃO DE VULNERABILIDADE (FORÇA BRUTA) ===")
    # Lista de senhas comuns para o teste do ataque
    lista_wordlist = ["123456", "admin", "password", "senha", "Senha123", "mudar123"]
    
    simular_forca_bruta(hash_armazenado, lista_wordlist)
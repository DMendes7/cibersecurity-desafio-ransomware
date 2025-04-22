import os
import pyaes

chave = b"diocybersecurity"

print("==== MENU ====")
print("1 - Criptografar arquivo")
print("2 - Descriptografar arquivo")
opcao = input("Escolha uma opção (1 ou 2): ")
chave_digitada = input("Digite a chave de criptografia: ")

if opcao == "1":
    if chave_digitada.encode() == chave:
        file_name = "teste.txt"
        file = open(file_name, "rb")
        file_data = file.read()
        file.close()

        ## remover o arquivo
        os.remove(file_name)

        aes = pyaes.AESModeOfOperationCTR(chave)

        ## criptografar o arquivo
        crypto_data = aes.encrypt(file_data)

        ## salvar o arquivo criptografado
        new_file = file_name + ".criptografado"
        new_file = open(f'{new_file}','wb')
        new_file.write(crypto_data)
        new_file.close()

        print(f"Arquivo {file_name} criptografado com sucesso!")

elif opcao == "2":
    if chave_digitada.encode() == chave:
        file_name = "teste.txt.criptografado"
        file = open(file_name, "rb")
        file_data = file.read()
        file.close()

        aes = pyaes.AESModeOfOperationCTR(chave)
        decrypt_data = aes.decrypt(file_data)

        ## remover o arquivo criptografado
        os.remove(file_name)

        ## criar o arquivo descriptografado
        new_file = "teste.txt"
        new_file = open(f'{new_file}', "wb")
        new_file.write(decrypt_data)
        new_file.close()

        print(f"Arquivo {file_name} descriptografado com sucesso!")

else:
    print("Opção inválida!")
    
        
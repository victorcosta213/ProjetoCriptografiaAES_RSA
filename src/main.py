from aes_crypto import gerar_chave_iv, aes_encrypt, aes_decrypt
from rsa_crypto import gerar_chaves_rsa, rsa_encrypt, rsa_decrypt
from benchmark import medir_tempo
import matplotlib.pyplot as plt
import os

mensagem_aes = b"A" * 190  
mensagem_rsa = b"A" * 190  

print("Tamanho mensagem AES:", len(mensagem_aes))
print("Tamanho mensagem RSA:", len(mensagem_rsa))

key, iv = gerar_chave_iv()
priv, pub = gerar_chaves_rsa()

aes_enc_tempo, aes_enc_std = medir_tempo(aes_encrypt, mensagem_aes, key, iv)
aes_data = aes_encrypt(mensagem_aes, key, iv)

aes_dec_tempo, aes_dec_std = medir_tempo(aes_decrypt, aes_data, key, iv)

rsa_enc_tempo, rsa_enc_std = medir_tempo(rsa_encrypt, pub, mensagem_rsa)
rsa_data = rsa_encrypt(pub, mensagem_rsa)

rsa_dec_tempo, rsa_dec_std = medir_tempo(rsa_decrypt, priv, rsa_data)

print(f"AES - Criptografia: {aes_enc_tempo * 1000:.3f} ms ± {aes_enc_std * 1000:.3f} ms")
print(f"AES - Descriptografia: {aes_dec_tempo * 1000:.3f} ms ± {aes_dec_std * 1000:.3f} ms")
print(f"RSA - Criptografia: {rsa_enc_tempo * 1000:.3f} ms ± {rsa_enc_std * 1000:.3f} ms")
print(f"RSA - Descriptografia: {rsa_dec_tempo * 1000:.3f} ms ± {rsa_dec_std * 1000:.3f} ms")

output_folder = os.path.join(os.path.dirname(__file__), "..", "plots")
os.makedirs(output_folder, exist_ok=True)

labels = ['AES (190B)', 'RSA (190B)']
medias_enc = [aes_enc_tempo * 1000, rsa_enc_tempo * 1000]
stds_enc = [aes_enc_std * 1000, rsa_enc_std * 1000]
stds_enc = [min(s, m) for s, m in zip(stds_enc, medias_enc)]

plt.bar(labels, medias_enc, yerr=stds_enc, capsize=10)
plt.title("Tempo de Criptografia (média em ms) - AES vs RSA")
plt.ylabel("Tempo (ms)")
plt.savefig(os.path.join(output_folder, "comparacao_tempos_criptografia.png"))
plt.clf()


medias_dec = [aes_dec_tempo * 1000, rsa_dec_tempo * 1000]
stds_dec = [aes_dec_std * 1000, rsa_dec_std * 1000]
stds_dec = [min(s, m) for s, m in zip(stds_dec, medias_dec)]

plt.bar(labels, medias_dec, yerr=stds_dec, capsize=10)
plt.title("Tempo de Descriptografia (média em ms) - AES vs RSA")
plt.ylabel("Tempo (ms)")
plt.savefig(os.path.join(output_folder, "comparacao_tempos_descriptografia.png"))
plt.show()

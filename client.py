from langserve import RemoteRunnable

chain_remota = RemoteRunnable(" http://localhost:8000/tradutor")
texto = chain_remota.invoke({"idioma":"inglês", "texto":"Vamos desenvolver o futuro!"})
print(texto)
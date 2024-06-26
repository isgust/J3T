from django.shortcuts import render  

# Renderiza o template para a página inicial
def index(request):
    return render(request, 'index.html') 

# Renderiza o template para a página de serviços
def servicos(request):
    return render(request, 'servicos.html')

# Renderiza o template para a página "Equipe"
def equipe(request):
    return render(request, 'equipe.html')

# Renderiza o template para a página de contato
def contato(request):
    return render(request, 'contato.html')

# Renderiza o template para a página de antesDepois
def antesDepois(request):
    return render(request, 'antesDepois.html')
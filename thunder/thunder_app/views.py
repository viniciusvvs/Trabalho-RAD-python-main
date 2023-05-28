from .forms import CadastroForm
from django.shortcuts import render


def index(request):
    form = CadastroForm()
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            # Processar os dados do formulário e salvar no banco de dados, se necessário
            # Redirecionar para outra página ou exibir uma mensagem de sucesso
            pass
    return render(request,'index.html', {'form': form})

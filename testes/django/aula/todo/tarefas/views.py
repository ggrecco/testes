from django.shortcuts import render
from .forms import CategoriaForm, TarefaForm
# Create your views here.

def nova_categoria(request):
	if request.method == 'POST':
		# recebe do usuário o formulário que foi preenchido
		form = CategoriaForm(request.POST)
		# verfica se o formulário é valido e salva
		if form.is_valid():
			form.save()
			return HttpResponse('Categoria adicionada com sucesso')
		else:
			print(form.erors)
	else:
		#exibe para o usuário o formlário em branco
		form = CategoriaForm()
	return render(request, 'tarefas/nova_categoria.html', {'form', form})


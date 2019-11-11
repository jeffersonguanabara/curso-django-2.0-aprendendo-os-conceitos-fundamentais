from django.shortcuts import render, redirect
from django.views import View
from .models import Transacao
from .forms import TransacaoForm

# Create your views here.

class Home(View):

    def get(self, request):
        return render(request, 'contas/home.html')


class Listagem(View):

    def get(self, request):
        data = {}
        data['transacoes'] = Transacao.objects.all()

        return render(request, 'contas/listagem.html', data)

class NovaTransacao(View):

    def get(self, request):
        data = {}
        form = TransacaoForm()
        data['form'] = form
        return render(request, 'contas/nova_transacao.html', data)

    def post(self, request):
        form = TransacaoForm(request.POST or None)

        if form.is_valid():
            form.save()
            return redirect('listagem')
        else:
            return self.get(self, request)

class EditarTransacao(View):

    def get(self, request, pk):
        
        data = {}
        transacao = Transacao.objects.get(pk=pk)
        form = TransacaoForm(instance=transacao)
        data['form'] = form
        data['transacao'] = transacao
        data['tipo'] = 'editar'
        return render(request, 'contas/nova_transacao.html', data)

    def post(self, request, pk):
        print('entrou no editar')
        transacao = Transacao.objects.get(pk=pk)
        form = TransacaoForm(request.POST or None, instance=transacao)

        if form.is_valid():
            form.save()
            return redirect('listagem')
        else:
            return self.get(self, request, pk)

class DeletarTransacao(View):

    def post(self, request, pk):
        print('entrou no deletar')
        transacao = Transacao.objects.get(pk=pk)
        transacao.delete()
        return redirect('listagem')


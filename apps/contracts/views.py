from django.shortcuts import render, redirect, get_object_or_404

from .forms import ContractForm
from .models import Contract


def add_contract(request):
    template_name = 'contracts/add_contract.html'
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect('contracts:list_contracts')
    else:
        form = ContractForm()
    return render(request, template_name, {'form': form})


def list_contracts(request):
    template_name = 'contracts/list_contracts.html'
    contracts = Contract.objects.filter()
    context = {'contracts': contracts}
    return render(request, template_name, context)


def edit_contract(request, id_contract):
    template_name = 'contracts/add_contract.html'
    contract = get_object_or_404(Contract, id=id_contract)
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('contracts:list_contracts')
    else:
        form = ContractForm(instance=contract)
    return render(request, template_name, {'form': form})


def delete_contract(request, id_contract):
    contract = get_object_or_404(Contract, id=id_contract)
    contract.delete()
    return redirect('contracts:list_contracts')

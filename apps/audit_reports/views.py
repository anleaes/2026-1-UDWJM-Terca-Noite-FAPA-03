from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .forms import AuditReportForm
from .models import AuditReport
from .serializer import AuditReportSerializer


def add_audit_report(request):
    template_name = 'audit_reports/add_audit_report.html'
    if request.method == 'POST':
        form = AuditReportForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('audit_reports:list_audit_report')
    else:
        form = AuditReportForm()
    return render(request, template_name, {'form': form})


def list_audit_report(request):
    template_name = 'audit_reports/list_audit_report.html'
    itens = AuditReport.objects.all()
    context = {'itens': itens}
    return render(request, template_name, context)


def edit_audit_report(request, id_audit_report):
    template_name = 'audit_reports/add_audit_report.html'
    audit_report = get_object_or_404(AuditReport, id=id_audit_report)
    if request.method == 'POST':
        form = AuditReportForm(request.POST, instance=audit_report)
        if form.is_valid():
            form.save()
            return redirect('audit_reports:list_audit_report')
    else:
        form = AuditReportForm(instance=audit_report)
    return render(request, template_name, {'form': form})


def delete_audit_report(request, id_audit_report):
    audit_report = get_object_or_404(AuditReport, id=id_audit_report)
    audit_report.delete()
    return redirect('audit_reports:list_audit_report')


class AuditReportViewSet(viewsets.ModelViewSet):
    queryset = AuditReport.objects.all()
    serializer_class = AuditReportSerializer

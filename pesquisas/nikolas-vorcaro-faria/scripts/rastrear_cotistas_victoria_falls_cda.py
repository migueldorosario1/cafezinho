#!/usr/bin/env python3
"""Procura um CNPJ investido nos CSVs do bloco 2 da CDA/CVM.

Não baixa bases, não consulta páginas restritas e não identifica beneficiário final.
Uso: python rastrear_cotistas_victoria_falls_cda.py bases/*.zip --saida resultado.json
Teste realizado apenas com dados sintéticos antes da entrega. Confirmar o dicionário
vigente da CVM e a cobertura de cada arquivo antes de interpretar os resultados.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import io
import json
import re
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

INVESTIDO = ('CNPJ_FUNDO_CLASSE_COTA', 'CNPJ_FUNDO_COTA')
DECLARANTE = ('CNPJ_FUNDO_CLASSE', 'CNPJ_FUNDO')
CAMPOS = ('TP_FUNDO', 'TP_FUNDO_CLASSE', 'CNPJ_FUNDO', 'CNPJ_FUNDO_CLASSE',
          'DENOM_SOCIAL', 'DT_COMPTC', 'CNPJ_FUNDO_COTA', 'CNPJ_FUNDO_CLASSE_COTA',
          'NM_FUNDO_COTA', 'NM_FUNDO_CLASSE_SUBCLASSE_COTA', 'VL_MERC_POS_FINAL',
          'QT_POS_FINAL', 'VL_CUSTO_POS_FINAL', 'CD_ATIVO')


def digitos(value: str) -> str:
    return re.sub(r'\D', '', value or '')


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def escolher(fields: list[str], options: tuple[str, ...]) -> str:
    return next((x for x in options if x in fields), '')


def ler_csv(binary, origem: str, alvo: str, encoding: str) -> tuple[dict, list[dict]]:
    text = io.TextIOWrapper(binary, encoding=encoding, errors='strict', newline='')
    reader = csv.DictReader(text, delimiter=';')
    fields = [(x or '').strip().lstrip('\ufeff') for x in (reader.fieldnames or [])]
    reader.fieldnames = fields
    invested = escolher(fields, INVESTIDO)
    owner = escolher(fields, DECLARANTE)
    info = {'membro': origem, 'cabecalho': fields, 'linhas_lidas': 0,
            'coluna_investido': invested, 'coluna_declarante': owner,
            'registros_correspondentes': 0, 'status': 'ok'}
    hits: list[dict] = []
    if not invested or not owner:
        info['status'] = 'cabecalho_nao_reconhecido_nao_pesquisado'
        return info, hits
    for line, row in enumerate(reader, 2):
        if None in row:
            raise ValueError(f'CSV malformado em {origem}, linha {line}')
        info['linhas_lidas'] += 1
        if digitos(row.get(invested, '')) != alvo:
            continue
        # Não reter outras colunas que possam conter dados pessoais desnecessários.
        hits.append({'membro': origem, 'linha_csv': line,
                     'cnpj_declarante': digitos(row.get(owner, '')),
                     'cnpj_investido': alvo,
                     'campos_publicados': {k: row.get(k, '') for k in CAMPOS if k in fields}})
    info['registros_correspondentes'] = len(hits)
    return info, hits


def processar(path: Path, alvo: str, encoding: str) -> dict:
    result = {'arquivo': path.name, 'sha256': sha256(path), 'membros': [], 'achados': [], 'erros': []}
    try:
        if zipfile.is_zipfile(path):
            with zipfile.ZipFile(path) as z:
                names = [i for i in z.infolist() if not i.is_dir()
                         and re.search(r'blc[_-]?2(?:_|\.)', i.filename, re.I)
                         and i.filename.lower().endswith('.csv')]
                if not names:
                    result['erros'].append('nenhum_csv_bloco_2_identificado')
                for member in names:
                    with z.open(member) as stream:
                        meta, hits = ler_csv(stream, member.filename, alvo, encoding)
                    result['membros'].append(meta)
                    result['achados'].extend(hits)
        elif path.suffix.lower() == '.csv':
            with path.open('rb') as stream:
                meta, hits = ler_csv(stream, path.name, alvo, encoding)
            result['membros'].append(meta)
            result['achados'].extend(hits)
        else:
            result['erros'].append('formato_nao_suportado')
    except (OSError, UnicodeError, csv.Error, ValueError, zipfile.BadZipFile, RuntimeError) as exc:
        result['erros'].append(f'{type(exc).__name__}: {exc}')
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('arquivos', type=Path, nargs='+')
    parser.add_argument('--cnpj', default='10566011000197')
    parser.add_argument('--encoding', default='utf-8-sig', help='Usar latin-1 apenas se necessário e registrar.')
    parser.add_argument('--saida', type=Path, default=Path('resultado_cotistas_victoria_falls.json'))
    args = parser.parse_args()
    alvo = digitos(args.cnpj)
    if len(alvo) != 14:
        parser.error('CNPJ deve ter 14 dígitos, sem preenchimento automático.')
    for file in args.arquivos:
        if not file.is_file():
            parser.error(f'Arquivo inexistente: {file}')
    report = {'consulta_utc': datetime.now(timezone.utc).isoformat(), 'cnpj_alvo': alvo,
              'encoding': args.encoding, 'arquivos': [],
              'ressalva': 'Resultado limitado aos arquivos e campos efetivamente lidos. '
                          'Posição declarada não identifica beneficiário final ou prova negócio com Faria. '
                          'Sem correspondências não significa ausência de cotista. '
                          'Preservar reapresentações, datas-base e distinção fundo/classe.'}
    for file in args.arquivos:
        report['arquivos'].append(processar(file, alvo, args.encoding))
    report['total_correspondencias'] = sum(len(x['achados']) for x in report['arquivos'])
    incomplete = any(x['erros'] or any(y['status'] != 'ok' for y in x['membros']) for x in report['arquivos'])
    report['status_leitura'] = 'incompleta' if incomplete else 'concluida_no_escopo_dos_arquivos'
    args.saida.parent.mkdir(parents=True, exist_ok=True)
    args.saida.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"{report['total_correspondencias']} correspondência(s). {report['status_leitura']}. Saída: {args.saida}")
    return 2 if incomplete else 0


if __name__ == '__main__':
    sys.exit(main())

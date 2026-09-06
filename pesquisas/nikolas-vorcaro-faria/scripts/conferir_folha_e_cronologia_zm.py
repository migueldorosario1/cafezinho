#!/usr/bin/env python3
"""Confere o CSV preservado e cálculos da revisão ZM, sem acesso à internet.

Uso no repositório:
    python scripts/conferir_folha_e_cronologia_zm.py folha-camara-thiago-rodrigues-de-faria.csv

Não atesta a integralidade da folha nem transforma dados cadastrais em autorização de operação.
"""
from __future__ import annotations
import argparse
import csv
from datetime import date
from decimal import Decimal, InvalidOperation
import hashlib
import io
import json
from pathlib import Path

EXPECTED_BLOB = 'e337ba35b86eab373fb12fcaa843debed6bd7c19'
FIELDS = ('cargo_comissao_brl', 'ferias_terco_brl', 'auxilios_brl')


def calculate(path: Path) -> dict:
    raw = path.read_bytes()
    blob_sha = hashlib.sha1(b'blob ' + str(len(raw)).encode('ascii') + b'\0' + raw).hexdigest()
    rows = list(csv.DictReader(io.StringIO(raw.decode('utf-8-sig'))))
    months = [(int(row['ano']), int(row['mes'])) for row in rows]
    expected = [(year, month) for year in range(2023, 2027) for month in range(1, 13)
                if (2023, 3) <= (year, month) <= (2026, 3)]
    if sorted(months) != expected or len(set(months)) != len(months):
        raise ValueError('Competências ausentes, repetidas ou fora do período esperado.')
    components = {field: sum((Decimal(row[field]) for row in rows), Decimal('0')) for field in FIELDS}
    total = sum(components.values(), Decimal('0'))
    areas = {'800.214/1978': '163.48', '804.805/1976': '44.37', '830.687/1980': '22.77',
             '830.689/1980': '4.29', '827.501/1972': '62.78', '800.645/1971': '349.10',
             '291.701/1936': '78.78'}
    return {
        'csv_git_blob_sha': blob_sha,
        'corresponde_ao_csv_original': blob_sha == EXPECTED_BLOB,
        'competencias': len(rows),
        'componentes_brl': {key: str(value) for key, value in components.items()},
        'total_csv_brl': str(total),
        'total_condicional_com_eventual_informada_brl': str(total + Decimal('598.80')),
        'ressalva_total': 'A parcela eventual foi informada pela equipe e não pertence ao CSV. O resultado não abrange todas as folhas ou rubricas.',
        'dias_publicacao_embargo_ate_audio': (date(2025, 3, 30) - date(2025, 2, 20)).days,
        'dias_publicacao_oito_autos_ate_audio': (date(2025, 3, 30) - date(2025, 3, 24)).days,
        'areas_cadastrais_ha': areas,
        'soma_areas_cadastrais_ha': str(sum(map(Decimal, areas.values()))),
        'ressalva_area': 'Soma dos campos cadastrais. Não mede a união espacial de polígonos nem prova área contínua sem sobreposições.'
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('csv_path', type=Path)
    args = parser.parse_args()
    try:
        result = calculate(args.csv_path)
    except (OSError, UnicodeError, KeyError, ValueError, InvalidOperation) as exc:
        parser.exit(1, f'Erro na conferência: {exc}\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if not result['corresponde_ao_csv_original']:
        parser.exit(2, 'Aviso: o arquivo mudou em relação ao CSV original. Os cálculos acima refletem o arquivo fornecido.\n')


if __name__ == '__main__':
    main()

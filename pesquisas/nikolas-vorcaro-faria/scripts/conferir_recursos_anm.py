#!/usr/bin/env python3
"""Confere as listas transcritas da ANM. Não consulta a rede nem valida julgamentos."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

NUP = re.compile(r"^\d{5}\.\d{6}/\d{4}-\d{2}$")


def conferir(path: Path) -> dict[str, object]:
    data = json.loads(path.read_text(encoding="utf-8"))
    pauta = data["processos_pauta"]
    anterior = data["processos_certidao_anterior"]
    for nome, lista in (("pauta", pauta), ("certidão", anterior)):
        if not isinstance(lista, list) or not all(isinstance(x, str) for x in lista):
            raise ValueError(f"Lista inválida em {nome}")
        if len(lista) != len(set(lista)):
            raise ValueError(f"Identificadores duplicados em {nome}")
        if any(not NUP.fullmatch(x) for x in lista):
            raise ValueError(f"Formato de NUP inválido em {nome}")
    p, a = set(pauta), set(anterior)
    adicionais = [x for x in pauta if x not in a]
    resultado = {
        "quantidade_pauta": len(p),
        "quantidade_certidao_anterior": len(a),
        "quantidade_comuns": len(p & a),
        "quantidade_adicionais": len(p - a),
        "ausentes_na_pauta": sorted(a - p),
    }
    for chave, valor in resultado.items():
        if data.get(chave) != valor:
            raise ValueError(f"Divergência entre resumo e listas em {chave}")
    if data.get("processos_adicionais") != adicionais:
        raise ValueError("Lista de processos adicionais não corresponde à diferença")
    return resultado


def main() -> None:
    default = Path(__file__).resolve().parents[1] / "dados" / "anm-topazio-pauta-88-2026.json"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("arquivo", nargs="?", type=Path, default=default)
    args = parser.parse_args()
    try:
        resultado = conferir(args.arquivo)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        parser.exit(1, f"Falha na conferência: {exc}\n")
    print(json.dumps(resultado, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

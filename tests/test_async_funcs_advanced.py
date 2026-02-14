import pytest
import asyncio
from koruspy import Some, nothing, async_option


async def db_find_user(user_id):
    await asyncio.sleep(0.01)
    if user_id == 1:
        return Some({"id": 1, "name": "Koruspy Dev", "admin": True})
    return nothing


async def log_success(user):
    await asyncio.sleep(0.01)
    return f"Log: Usuário {user} processado."


async def log_failure():
    await asyncio.sleep(0.01)
    return "Log: Tentativa de acesso inválida."


@pytest.mark.asyncio
async def test_full_async_pipeline_with_new_features():
    # --- SUCESSO ---
    success_tracker = []

    res_success = await (
        async_option(db_find_user(1))
        .filter_async(lambda u: u["admin"] is True)
        .map_async(lambda u: u["name"].upper())
        .map_async(lambda name: (success_tracker.append(f"Presente: {name}"), name)[1])
        .and_then_async(log_success)
        .unwrap_or_async("Desconhecido")
    )

    assert res_success == "Log: Usuário KORUSPY DEV processado."
    assert "Presente: KORUSPY DEV" in success_tracker

    # --- FALHA ---
    failure_tracker = []

    res_failure = await (
        async_option(db_find_user(99))
        .map_async(lambda x: failure_tracker.append("Não devia estar aqui"))
        .on_nothing_async(lambda: failure_tracker.append("Nada encontrado"))
        .on_nothing_async(log_failure)
        .unwrap_or_async(lambda: asyncio.sleep(0.01, result="Fallback Assíncrono"))
    )

    assert res_failure == "Fallback Assíncrono"
    assert "Nada encontrado" in failure_tracker
    assert "Não devia estar aqui" not in failure_tracker